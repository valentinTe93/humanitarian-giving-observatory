# Humanitarian Giving Observatory

## Reported funding coverage and recorded requirements

**Author:** Valentin Te Selone  
**Analytical window:** 2000–2026, the years with nonblank requirement records in the checked-in extract  
**Source:** OCHA Financial Tracking Service (FTS), Global Requirements and Funding Data

> **Purpose and boundary.** This report analyzes recorded financial requirements and funding reported in the OCHA FTS extract. It is a descriptive financial analysis—not a measure of humanitarian need, severity, people affected, suffering, funding impact, or a recommendation for allocating aid.

## Executive summary

The Humanitarian Giving Observatory asks:

**How well does reported funding cover global humanitarian funding requirements?**

The answer depends on keeping the time window and the denominator visible.

For a like-for-like annual comparison across **2000–2026**, the checked-in data sum to **USD 531.38 billion** in recorded requirements and **USD 428.92 billion** in reported funding. The documented aggregate formula—summed reported funding divided by summed requirements—returns **80.72%**; requirements less reported funding produce a **USD 102.47 billion** aggregate gap.

The Power BI all-record validation context instead shows **USD 531.38 billion** in requirements, **USD 430.83 billion** in funding, a **USD 100.55 billion** gap, and **81.08%** coverage. The difference is attributable to reported funding outside the comparable 2000–2026 window: the extract includes funding-only records in 1999 and 2027–2031, without requirement values in those years. The all-record cards are valid as a reproduction of the documented dashboard context, but they should not be presented as the same-period comparison.

Three findings follow:

1. **A material financial gap remains in the aligned period.** The aggregate gap is USD 102.47 billion under the stated calculation. It is a signal in the reported extract, not proof of unmet human need.
2. **Annual coverage varies substantially.** The aggregate of reported funding divided by requirements ranges from 52.4% in 2025 to 204.5% in 2005. Values above 100% are retained. The 2026 reading is provisional: requirements are populated for only 45 of 164 records for that year in the checked-in file.
3. **Geographic coverage and absolute shortfall tell different stories.** The map shows the coverage ratio, while the Top 10 ranks the positive dollar difference. In the aligned period, Lebanon has the largest country-level positive shortfall in the extract, at about USD 16.8 billion.

A further qualification is important: within 2000–2026, **USD 140.37 billion of reported funding appears on rows whose requirement field is blank**. Under the documented DAX logic, those values are included in the funding numerator while blank requirements do not contribute to the denominator. The 80.72% measure is therefore an extract-level ratio, not a row-matched rate of funding against a fully observed requirement. It should be interpreted alongside the completeness findings below.

## Scope, source, and period

The analysis uses the two data files committed with the Power BI project:

- `data/fts_requirements_funding_global.csv` — the OCHA FTS annual requirements-and-funding extract.
- `data/country_codes_iso3.csv` — the country-code lookup used for readable country labels and ISO Alpha-3 mapping.

The checked-in extract contains **3,848 rows** and reporting-year values from **1999 to 2031**. In this snapshot, requirement values are present only for **2000–2026**. Funding values also occur in 1999 and 2027–2031, where requirement values are blank. Accordingly, the annual chart, geographic comparison, and shortfall ranking in this report use 2000–2026. The Power BI all-record validation figures are shown separately for reconciliation.

OCHA describes FTS as tracking and publishing humanitarian funding flows, including funding reported against or mapped to requirements stated in response plans. FTS data are updated continuously, and reporting can lag funding decisions or be incomplete at a given point in time [1, 2]. The report calculations were reproduced from the repository snapshot reviewed on 27 September 2026; the live HDX dataset may since have changed.

## Headline measures

| Measure | Comparable period: 2000–2026 | Power BI all-record validation context |
| --- | ---: | ---: |
| Recorded requirements | USD 531.38bn | USD 531.38bn |
| Reported funding | USD 428.92bn | USD 430.83bn |
| Requirements less reported funding | USD 102.47bn | USD 100.55bn |
| Reported funding ÷ requirements | 80.72% | 81.08% |

The two columns are **different filter contexts**, not competing calculations. Both use the documented aggregation—sum funding divided by sum requirements—but the all-record context also includes funding-only years outside the requirement period. The report uses the 2000–2026 column for its annual, geographic, and shortfall analyses.

## Finding 1 — the aggregate gap is material, but the ratio has a denominator caveat

In the comparable period, recorded requirements exceed reported funding by **USD 102.47 billion**. That difference describes the financial records in this extract and should not be converted into a claim about unmet needs or humanitarian outcomes.

The **80.72%** ratio is calculated as total reported funding divided by total recorded requirements. It is not the average of the source’s `percentFunded` field. However, it is also not a row-matched coverage rate: **USD 140.37 billion** in reported funding is on records with blank requirement amounts in the same period. The source does not establish from these fields alone whether each such amount should be matched to a requirement elsewhere. The report therefore retains the documented dashboard measure, makes its construction explicit, and treats its interpretation as qualified rather than definitive.

The full-extract KPI context produces the familiar **81.08%** dashboard card. Its numerator includes about **USD 1.92 billion** in additional funding outside 2000–2026, where the extract has no requirement amounts. This is why the report distinguishes the dashboard validation context from the aligned-period findings.

## Finding 2 — annual coverage changes sharply over time

The annual chart compares summed requirements and reported funding, and calculates annual coverage as funding divided by requirements. On that basis, annual coverage reaches **204.5% in 2005** and falls to **52.4% in 2025**. A value above 100% means that reported funding exceeds the recorded requirement in the selected annual context; it is not capped or treated as an error.

![Annual requirements, reported funding, and coverage from 2000 through 2026](https://private-us-east-1.manuscdn.com/sessionFile/njWMJ9AhcKO5XzhTJlvpFc/sandbox/CZZyJQ1r59wrxPblDFkqFt-images_1790545475556_na1fn_L2hvbWUvdWJ1bnR1L3dvcmsvcmVwby9kb2NzL2ZpZ3VyZXMvYW5udWFsX2NvdmVyYWdl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvbmpXTUo5QWhjS081WHpoVEpsdnBGYy9zYW5kYm94L0NaWnlKUTFyNTl3cnhQYmxERmtxRnQtaW1hZ2VzXzE3OTA1NDU0NzU1NTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzZHZjbXN2Y21Wd2J5OWtiMk56TDJacFozVnlaWE12WVc1dWRXRnNYMk52ZG1WeVlXZGwucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzkyMDIyNDAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIHSOeUPKo2Zoj50ogt~EiopOigalVhzkrNC1QAeNBZa7AiEA~IKNhcPuSiouJcuyop8YHEkb2UAbnpyyjrQqNunAqU4_)

*Figure 1. Annual OCHA FTS requirements and reported funding, with the documented aggregate coverage ratio. Comparable window: 2000–2026. The 2026 value is provisional in this snapshot; funding-only records outside the window are excluded. Source: repository extract [1].*

The latest year is especially incomplete. In 2026, the file contains 164 records, but only 45 have a nonblank requirement amount; the calculated ratio should therefore be read as an early snapshot, not a settled annual outcome. More generally, annual changes can reflect source completeness, plan structure, and reporting timing as well as the underlying financial position.

## Finding 3 — geographic coverage and absolute shortfall are complementary

The map shows country-level coverage bands for 2000–2026. Country values are calculated by summing reported funding and requirements for each source location code, then dividing the two totals. The location lookup supplies ISO Alpha-3 codes; the polygons are a Natural Earth-derived reference layer [3, 4]. The map is retained because it answers a distinct question—**where reported coverage differs geographically**—rather than serving as decoration.

![Country-level reported funding coverage map, 2000–2026](https://private-us-east-1.manuscdn.com/sessionFile/njWMJ9AhcKO5XzhTJlvpFc/sandbox/CZZyJQ1r59wrxPblDFkqFt-images_1790545475556_na1fn_L2hvbWUvdWJ1bnR1L3dvcmsvcmVwby9kb2NzL2ZpZ3VyZXMvY292ZXJhZ2VfbWFwXzIwMDBfMjAyNg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvbmpXTUo5QWhjS081WHpoVEpsdnBGYy9zYW5kYm94L0NaWnlKUTFyNTl3cnhQYmxERmtxRnQtaW1hZ2VzXzE3OTA1NDU0NzU1NTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzZHZjbXN2Y21Wd2J5OWtiMk56TDJacFozVnlaWE12WTI5MlpYSmhaMlZmYldGd1h6SXdNREJmTWpBeU5nLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5MjAyMjQwMH19fV19&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQD9ORyFMQIGSMahJijUXnuPQUqvI~tYMPCuwXUa7-2RPgIgdUsQ7qDVr70JC1MYhqpxl5ZZHz0RcDa2AbtULLU4Er4_)

*Figure 2. Reconstructed country-level coverage map for the aligned period. Neutral shading means no matched positive requirement denominator or no source record; it does not mean zero funding or zero need. Natural Earth represents boundaries according to its documented boundary policy [4]. This map is a report figure derived from the checked-in data, not an unedited Power BI screenshot.*

Among the **113 source location codes** present in the aligned period, **110** have a positive requirement denominator and are classified as follows; three have no usable denominator. These are financial coverage bands, not severity categories.

| Reported funding ÷ requirements | Location codes |
| --- | ---: |
| Below 50% | 15 |
| 50% to below 80% | 29 |
| 80% to below 100% | 13 |
| 100% or above | 53 |
| No positive requirement denominator | 3 |

The Top 10 visual complements the map by ranking positive dollar shortfalls rather than coverage percentages. The checked-in lookup label “Congo – Kinshasa” refers to the Democratic Republic of the Congo.

![Top 10 country-level positive funding shortfalls, 2000–2026](https://private-us-east-1.manuscdn.com/sessionFile/njWMJ9AhcKO5XzhTJlvpFc/sandbox/CZZyJQ1r59wrxPblDFkqFt-images_1790545475556_na1fn_L2hvbWUvdWJ1bnR1L3dvcmsvcmVwby9kb2NzL2ZpZ3VyZXMvdG9wMTBfc2hvcnRmYWxsXzIwMDBfMjAyNg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvbmpXTUo5QWhjS081WHpoVEpsdnBGYy9zYW5kYm94L0NaWnlKUTFyNTl3cnhQYmxERmtxRnQtaW1hZ2VzXzE3OTA1NDU0NzU1NTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzZHZjbXN2Y21Wd2J5OWtiMk56TDJacFozVnlaWE12ZEc5d01UQmZjMmh2Y25SbVlXeHNYekl3TURCZk1qQXlOZy5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTIwMjI0MDB9fX1dfQ__&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEUCIQDirl46otl4a3G1TmrDwTEdyhPJtaUo2wBu4nmIBWAXjgIgRm7uNwFchU2uYMZS2HW-ulVH0cd7cuUPJxmZW3TRAjI_)

*Figure 3. Largest positive location-level shortfalls, calculated as max(0, summed requirements less summed reported funding) after aggregating each location across 2000–2026. Values are rounded to one decimal billion USD. Source: repository extract [1].*

Lebanon has the largest positive shortfall (USD 16.8 billion), followed by Syria (USD 13.5 billion), Sudan (USD 12.3 billion), and the Democratic Republic of the Congo (USD 11.0 billion). The remaining six ranked shortfalls range from USD 4.4 billion to USD 5.6 billion.

The ranking identifies locations for further financial review; it is not an allocation recommendation. A large absolute shortfall and a low coverage percentage are related but different signals, and neither measures the scale of humanitarian need.

## Method and model

The source fields are transformed in Power Query inside the Power BI file. The fact table is documented at **country–plan–reporting-year** grain. Location filters plans through country code; plans filter the fact through the stable `country_plan_key`. The dedicated `measurements` table holds the DAX measures. There is no direct location-to-fact relationship in the documented model [5].

![Requirements-focused model relationships](https://private-us-east-1.manuscdn.com/sessionFile/njWMJ9AhcKO5XzhTJlvpFc/sandbox/CZZyJQ1r59wrxPblDFkqFt-images_1790545475556_na1fn_L2hvbWUvdWJ1bnR1L3dvcmsvcmVwby9kb2NzL2ZpZ3VyZXMvbW9kZWxfcmVsYXRpb25zaGlwcw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvbmpXTUo5QWhjS081WHpoVEpsdnBGYy9zYW5kYm94L0NaWnlKUTFyNTl3cnhQYmxERmtxRnQtaW1hZ2VzXzE3OTA1NDU0NzU1NTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzZHZjbXN2Y21Wd2J5OWtiMk56TDJacFozVnlaWE12Ylc5a1pXeGZjbVZzWVhScGIyNXphR2x3Y3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzkyMDIyNDAwfX19XX0_&Key-Pair-Id=K2QY5QTL8JSY6C&Signature=MEQCID8Q8UnPBSoubeuJWg2-Lta61-XHh1uDn-03wkUYGopoAiBmotisPIG6XlfQT9xO3X8iHVb9itA~hamufLof3i-nhw__)

*Figure 4. The location dimension filters the plan dimension, and the plan dimension filters the requirements fact. The measures table supplies calculations to the report visuals; it is not a relationship endpoint.*

The main calculations are:

- **Requirements:** sum of `requirements_usd` in the current filter context.
- **Reported funding:** sum of `reported_funding_usd` in the current filter context.
- **Funding gap:** requirements less reported funding; the result may be negative.
- **Positive shortfall:** the positive part of the funding gap, with zero where funding meets or exceeds requirements.
- **Coverage:** reported funding divided by requirements; values above 100% remain visible.

The source `percentFunded` field is retained for reference; it is not summed or averaged to create the headline measure. The formulas, Power Query steps, relationships, color bands, and Power BI report details are in [`docs/Process_documentation.pdf`](https://github.com/valentinTe93/humanitarian-giving-observatory/blob/main/docs/Process_documentation.pdf) [5]. The repository [`README.md`](README.md) is the shorter project and file guide.

## Data quality and limitations

The checked-in extract contains substantial missingness:

| Source field | Blank rows | Share of 3,848 rows |
| --- | ---: | ---: |
| Requirements | 2,655 | 69.0% |
| Source `percentFunded` | 2,668 | 69.3% |
| Funding | 19 | 0.5% |

A blank requirement is not evidence that the true requirement is zero. As described above, funding values on blank-requirement rows enter the summed funding numerator under the documented measure. This limits how literally the calculated ratio can be read as the share of requirements funded. The report does not silently remove those funding values or invent a replacement denominator.

Additional limitations:

- The source is a reported financial dataset, not a complete accounting of all humanitarian financing.
- FTS records can be amended or delayed; the live dataset is updated regularly, so this report describes the checked-in snapshot rather than a permanent total [1, 2].
- The latest reporting year and the funding-only years outside the requirement period require particular caution.
- The country lookup and map geometry aid identification but do not add funding evidence. Unmatched codes remain a data-quality issue.
- Natural Earth boundary depictions are cartographic representations and should not be read as legal or political determinations [4].
- The analysis is descriptive. It does not establish causality, donor intent, arrival timing, disbursement, spending effectiveness, or humanitarian outcomes.

## Analytical implications

1. **Validate denominator completeness.** Review the records with missing requirements and the USD 140.37 billion in funding recorded on those rows before treating the aggregate ratio as a strict coverage rate.
2. **Keep periods aligned.** Use 2000–2026 for direct comparisons of annual requirements and funding; keep funding-only years visible in data-quality review rather than blending them into a like-for-like coverage trend.
3. **Use the map and ranking together.** The map screens percentage coverage; the shortfall ranking surfaces absolute amounts for further investigation. Inspect the underlying year and plan before drawing conclusions.
4. **Do not infer need or allocation priority.** Use the dashboard to identify financial records for review, not as a proxy for humanitarian severity or a standalone funding-allocation rule.
5. **Refresh and revalidate.** When the source extract or Power BI queries change, recompute the period, totals, missingness, map join, and report figures before reuse.

## References

1. OCHA Financial Tracking System (FTS), **Global – Requirements and Funding Data**, Humanitarian Data Exchange (HDX), dataset and `fts_requirements_funding_global.csv` resource. [Dataset page](https://data.humdata.org/dataset/global-requirements-and-funding-data) · [CSV resource](https://data.humdata.org/dataset/global-requirements-and-funding-data/resource/b3232da8-f1e4-41ab-9642-b22dae10a1d7). The calculations use the copy committed as `data/fts_requirements_funding_global.csv`, reviewed 27 September 2026.
2. OCHA Financial Tracking Service, **About FTS / Using FTS Data**. [https://fts.unocha.org/content/about-fts-using-fts-data](https://fts.unocha.org/content/about-fts-using-fts-data). Source context for what FTS records, ongoing updates, and reporting delays.
3. DataHub, **Comprehensive Country Codes: ISO 3166, ITU, ISO 4217 currency codes and many more**. [Dataset page](https://datahub.io/core/country-codes). Project lookup copy: `data/country_codes_iso3.csv`.
4. DataHub, **Country Polygons as GeoJSON**, sourced from Natural Earth; public-domain boundary data, DataHub page licensed under ODC PDDL. [DataHub dataset](https://datahub.io/core/geo-countries) · [Natural Earth Admin 0 – Countries](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/).
5. Valentin Te Selone, **Humanitarian Giving Observatory — Process Documentation**, repository file [`docs/Process_documentation.pdf`](https://github.com/valentinTe93/humanitarian-giving-observatory/blob/main/docs/Process_documentation.pdf). Source for the documented model, transformations, measures, visuals, and interpretation rules.

## Appendix A — Key terms

| Term | Meaning in this report |
| --- | --- |
| Recorded requirement | Financial requirement amount recorded in the selected OCHA FTS extract for a location, plan, and reporting year. |
| Reported funding | Funding amount recorded in the selected OCHA FTS extract; it may be present on a row whose requirement is blank. |
| Funding gap | Requirements less reported funding in the current aggregation context; it can be negative. |
| Positive shortfall | The positive part of the funding gap; zero when reported funding meets or exceeds requirements. |
| Reported coverage | Sum of reported funding divided by sum of recorded requirements in the chosen filter context; not capped at 100% and not necessarily row-matched when requirements are blank. |
| Country–plan–reporting-year grain | The analytical record level used by the documented fact table: one location, one plan, and one annual reporting year. |
