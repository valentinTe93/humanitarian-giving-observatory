from __future__ import annotations

import csv
import gzip
import json
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MplPath

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / 'docs' / 'figures'
DATA = ROOT / 'data' / 'fts_requirements_funding_global.csv'
LOOKUP = ROOT / 'data' / 'country_codes_iso3.csv'
GEOJSON = ROOT / 'data' / 'natural_earth_countries.geojson.gz'
PERIOD = (2000, 2026)
D = Decimal

COLORS = {
    'navy': '#142E40',
    'ink': '#17384A',
    'muted': '#5A6F7D',
    'grid': '#DCE5EA',
    'bg': '#F7FAFC',
    'red': '#F06B5B',
    'amber': '#F2B84B',
    'aqua': '#5FC8C3',
    'teal': '#25B7B0',
    'nodata': '#D9E2E8',
    'white': '#FFFFFF',
}
BANDS = [('<50%', D('0.50'), COLORS['red']),
         ('50–<80%', D('0.80'), COLORS['amber']),
         ('80–<100%', D('1.00'), COLORS['aqua']),
         ('100%+', None, COLORS['teal'])]

FIG.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 13,
    'axes.labelcolor': COLORS['muted'],
    'text.color': COLORS['ink'],
    'axes.edgecolor': COLORS['grid'],
    'xtick.color': COLORS['muted'],
    'ytick.color': COLORS['muted'],
    'savefig.facecolor': COLORS['white'],
    'figure.facecolor': COLORS['white'],
})

with DATA.open(newline='', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
with LOOKUP.open(newline='', encoding='utf-8-sig') as f:
    lookup = {r['location_code'].strip().upper(): r for r in csv.DictReader(f)}
with gzip.open(GEOJSON, 'rt', encoding='utf-8') as f:
    geo = json.load(f)


def dec(v: str | None) -> Decimal:
    v = (v or '').strip()
    return D(v) if v else D(0)


def in_period(row: dict) -> bool:
    y = (row.get('year') or '').strip()
    return y.isdigit() and PERIOD[0] <= int(y) <= PERIOD[1]

period_rows = [r for r in rows if in_period(r)]
all_req = sum((dec(r.get('requirements')) for r in period_rows), D(0))
all_fund = sum((dec(r.get('funding')) for r in period_rows), D(0))
all_gap = all_req - all_fund

# Completeness and numerator/denominator pairing checks.
missing = {}
for col in ('requirements', 'funding', 'percentFunded'):
    n = sum(not (r.get(col) or '').strip() for r in rows)
    missing[col] = {'count': n, 'percent': 100 * n / len(rows)}
funding_on_blank_req = sum((dec(r.get('funding')) for r in period_rows
                            if not (r.get('requirements') or '').strip()), D(0))

# The documented coverage calculation uses summed reported funding / summed
# requirements. Keep this explicit, and separately quantify funding records
# with no requirement value rather than silently implying row-level matching.
by_year = defaultdict(lambda: [D(0), D(0), 0, 0])
for r in period_rows:
    y = int(r['year'])
    if (r.get('requirements') or '').strip():
        by_year[y][0] += dec(r.get('requirements'))
        by_year[y][2] += 1
    if (r.get('funding') or '').strip():
        by_year[y][1] += dec(r.get('funding'))
        by_year[y][3] += 1
annual = []
for y in range(PERIOD[0], PERIOD[1] + 1):
    req, fund, req_rows, fund_rows = by_year[y]
    cov = fund / req if req else None
    annual.append({'year': y, 'requirements': req, 'funding': fund,
                   'coverage': cov, 'requirement_rows': req_rows,
                   'funding_rows': fund_rows})

# Country/location-level sums in the aligned period; this is the numerator and
# denominator logic used to produce the map and ranking.
by_loc = defaultdict(lambda: [D(0), D(0)])
for r in period_rows:
    code = (r.get('countryCode') or '').strip().upper()
    if not code:
        continue
    by_loc[code][0] += dec(r.get('requirements'))
    by_loc[code][1] += dec(r.get('funding'))

band_counts = Counter()
for code, (req, fund) in by_loc.items():
    if req <= 0:
        band_counts['No requirement denominator'] += 1
    else:
        cov = fund / req
        if cov < D('0.50'):
            band_counts['Below 50%'] += 1
        elif cov < D('0.80'):
            band_counts['50% to below 80%'] += 1
        elif cov < D('1.00'):
            band_counts['80% to below 100%'] += 1
        else:
            band_counts['100% or above'] += 1

# A comparable-period aggregate is used for all geography and ranking visuals.
# Dashboard all-record validation metrics are reported separately in the text.

def band_color(coverage: Decimal | None) -> str:
    if coverage is None:
        return COLORS['nodata']
    if coverage < D('0.50'):
        return COLORS['red']
    if coverage < D('0.80'):
        return COLORS['amber']
    if coverage < D('1.00'):
        return COLORS['aqua']
    return COLORS['teal']

iso_agg = {}
for code, (req, fund) in by_loc.items():
    rec = lookup.get(code, {})
    iso = (rec.get('iso_alpha_3') or '').strip().upper()
    if not iso:
        continue
    coverage = fund / req if req > 0 else None
    iso_agg[iso] = {
        'code': code,
        'name': rec.get('country_name') or code,
        'requirements': req,
        'funding': fund,
        'coverage': coverage,
        'color': band_color(coverage),
    }

# Annual combo chart.
fig, ax = plt.subplots(figsize=(11.0, 4.7), constrained_layout=True)
fig.suptitle('Reported funding coverage varies by reporting year', x=0.08, y=1.035,
             ha='left', fontsize=16, fontweight='bold', color=COLORS['navy'])
xs = [r['year'] for r in annual]
reqs = [float(r['requirements'] / D(10**9)) for r in annual]
funds = [float(r['funding'] / D(10**9)) for r in annual]
covs = [float(r['coverage'] * 100) for r in annual]
width = 0.36
ax.bar([x - width/2 for x in xs], reqs, width, color=COLORS['amber'], label='Recorded requirements', zorder=3)
ax.bar([x + width/2 for x in xs], funds, width, color=COLORS['teal'], label='Reported funding', zorder=3)
ax.set_ylabel('USD billions')
ax.set_xlim(1999.1, 2026.9)
ax.set_xticks(xs[::2])
ax.set_xticklabels([str(x) for x in xs[::2]])
ax.grid(axis='y', color=COLORS['grid'], linewidth=0.8, zorder=0)
ax.spines[['top','right']].set_visible(False)
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
ax2 = ax.twinx()
ax2.plot(xs, covs, color=COLORS['red'], linewidth=2.3, marker='o', markersize=3.3,
         label='Funding ÷ requirements', zorder=4)
ax2.set_ylabel('Reported funding / requirements')
ax2.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
ax2.set_ylim(0, max(covs) * 1.12)
ax2.spines[['top','left']].set_visible(False)
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax.legend(handles1+handles2, labels1+labels2, loc='upper left', frameon=False, ncol=3,
          bbox_to_anchor=(0, 1.02), fontsize=10.5)
ax.text(0, -0.23, 'Comparable window: 2000–2026. The 2026 record is partial in this snapshot; funding-only records outside this window are excluded.',
        transform=ax.transAxes, ha='left', va='top', fontsize=9.5, color=COLORS['muted'])
fig.savefig(FIG / 'annual_coverage.png', dpi=300, bbox_inches='tight')
plt.close(fig)

# Country coverage map using DataHub's Natural Earth-derived polygons keyed to ISO Alpha-3.
fig, ax = plt.subplots(figsize=(12.2, 5.6), constrained_layout=True)
fig.suptitle('Country-level reported funding coverage, 2000–2026', x=0.075, y=1.035,
             ha='left', fontsize=16, fontweight='bold', color=COLORS['navy'])
ax.set_facecolor('#F2F6F8')
for feature in geo['features']:
    props = feature.get('properties') or {}
    iso = (props.get('ISO3166-1-Alpha-3') or '').upper()
    label = props.get('name') or 'Unmatched'
    record = iso_agg.get(iso)
    face = record['color'] if record else COLORS['nodata']
    geom = feature.get('geometry') or {}
    typ = geom.get('type')
    coords = geom.get('coordinates') or []
    polygons = [coords] if typ == 'Polygon' else coords if typ == 'MultiPolygon' else []
    for polygon in polygons:
        if not polygon:
            continue
        ring = polygon[0]
        if len(ring) < 3:
            continue
        verts = [(float(x), float(y)) for x, y, *rest in ring]
        codes = [MplPath.MOVETO] + [MplPath.LINETO] * (len(verts) - 2) + [MplPath.CLOSEPOLY]
        patch = PathPatch(MplPath(verts, codes), facecolor=face, edgecolor=COLORS['white'],
                          linewidth=0.22, antialiased=True)
        ax.add_patch(patch)
ax.set_xlim(-180, 180)
ax.set_ylim(-60, 85)
ax.set_aspect('auto')
ax.axis('off')
from matplotlib.patches import Patch
legend = [Patch(facecolor=color, edgecolor='none', label=label) for label, _, color in BANDS]
legend.append(Patch(facecolor=COLORS['nodata'], edgecolor='none', label='No matched denominator / no source record'))
ax.legend(handles=legend, loc='lower center', bbox_to_anchor=(0.5, -0.01), ncol=5,
          frameon=False, fontsize=11.5, handlelength=1.2, columnspacing=1.6)
ax.text(0.5, -0.105, 'Country rates are calculated as summed reported funding ÷ summed recorded requirements within the aligned period. Shading is not a measure of need.',
        transform=ax.transAxes, ha='center', va='top', fontsize=9.5, color=COLORS['muted'])
fig.savefig(FIG / 'coverage_map_2000_2026.png', dpi=300, bbox_inches='tight')
plt.close(fig)

# Top-10 positive shortfall by country/location for the same period.
ranked = sorted(((max(D(0), req - fund), code, req, fund)
                 for code, (req, fund) in by_loc.items()), reverse=True)[:10]
ranked = [x for x in ranked if x[0] > 0]
fig, ax = plt.subplots(figsize=(10.5, 5.5), constrained_layout=True)
fig.suptitle('Largest positive reported funding gaps by location', x=0.15, y=1.035,
             ha='left', fontsize=16, fontweight='bold', color=COLORS['navy'])
names = [lookup.get(code, {}).get('country_name', code) for _, code, _, _ in ranked]
values = [float(gap / D(10**9)) for gap, _, _, _ in ranked]
ypos = list(range(len(ranked)))
ax.barh(ypos, values, color=COLORS['red'], height=0.64)
ax.set_yticks(ypos, names)
ax.invert_yaxis()
ax.set_xlabel('Positive shortfall (USD billions)')
ax.grid(axis='x', color=COLORS['grid'], linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
ax.spines[['top','right','left']].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
for i, v in enumerate(values):
    ax.text(v + max(values)*0.012, i, f'${v:.1f}bn', va='center', ha='left', fontsize=11, color=COLORS['ink'])
ax.set_xlim(0, max(values)*1.18)
ax.text(0, -0.12, 'Ranked on max(0, requirements − reported funding) after summing each location across 2000–2026.',
        transform=ax.transAxes, ha='left', va='top', fontsize=9.5, color=COLORS['muted'])
fig.savefig(FIG / 'top10_shortfall_2000_2026.png', dpi=300, bbox_inches='tight')
plt.close(fig)

# Compact validation record for report authoring and independent checks.
all_req_src = sum((dec(r.get('requirements')) for r in rows), D(0))
all_fund_src = sum((dec(r.get('funding')) for r in rows), D(0))
covered_values = [r['coverage'] for r in annual if r['coverage'] is not None]
min_year = min((r for r in annual if r['coverage'] is not None), key=lambda r:r['coverage'])
max_year = max((r for r in annual if r['coverage'] is not None), key=lambda r:r['coverage'])
summary = {
    'snapshot': {'rows': len(rows), 'source_reporting_year_min': min(int(r['year']) for r in rows if (r.get('year') or '').isdigit()),
                  'source_reporting_year_max': max(int(r['year']) for r in rows if (r.get('year') or '').isdigit())},
    'all_source_dashboard_context': {'requirements_usd': str(all_req_src), 'funding_usd': str(all_fund_src),
        'gap_usd': str(all_req_src-all_fund_src), 'coverage_percent': float(all_fund_src/all_req_src*100)},
    'aligned_period': {'start_year': PERIOD[0], 'end_year': PERIOD[1], 'row_count': len(period_rows),
        'requirements_usd': str(all_req), 'funding_usd': str(all_fund), 'gap_usd': str(all_gap),
        'coverage_percent': float(all_fund/all_req*100),
        'funding_on_rows_with_blank_requirement_usd': str(funding_on_blank_req)},
    'missing_values': missing,
    'annual_coverage_extremes': {'min': {'year': min_year['year'], 'percent': float(min_year['coverage']*100)},
                                 'max': {'year': max_year['year'], 'percent': float(max_year['coverage']*100)}},
    'country_coverage_band_counts_2000_2026': dict(band_counts),
    'top10_shortfall_2000_2026': [
        {'location_code': code, 'location': lookup.get(code, {}).get('country_name', code),
         'shortfall_usd': str(gap), 'requirements_usd': str(req), 'reported_funding_usd': str(fund)}
        for gap, code, req, fund in ranked
    ],
}
print(json.dumps(summary, indent=2))
print('Figures written:', ', '.join(str(p) for p in sorted(FIG.glob('*.png'))))
