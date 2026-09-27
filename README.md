# Humanitarian Giving Observatory

**Author:** Valentin Te Selone  
**Tooling:** Microsoft Power BI | Power Query | DAX | Data Modeling  
**Data Source:** [UN OCHA Financial Tracking Service (FTS)](https://fts.unocha.org/)

---

## Executive Summary
The **Humanitarian Giving Observatory** is a financial analysis portfolio dashboard designed to examine how reported funding compares with recorded humanitarian funding requirements across reporting years and geographic locations. 

The primary governing analytical question is:  
> **How well does reported funding cover global humanitarian funding requirements?**

> **Disclaimer:** This dashboard describes recorded financial requirements and reported funding coverage. It is a financial observatory and **must not** be interpreted as a direct measure of humanitarian need, severity, affected populations, or human suffering.

---

## Data Model & Architecture

The analytical engine relies on a **Requirements-focused Snowflake Schema** engineered via Power Query and DAX:

```text
[dim_requirements_location] (1) ───< (N) [dim_requirements_plan] (1) ───< (N) [fact_requirements_funding]
