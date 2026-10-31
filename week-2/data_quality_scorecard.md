# Employee Attrition – Data Quality Scorecard

## 1. Dataset Overview
- Dataset: employee_attrition_2026_master.csv
- Total Records: 45,000
- Total Columns: 29

## 2. Six DAMA Data Quality Dimensions

| Dimension | Findings | Status |
|---|---|---|
| Completeness | 0 missing values | Pass |
| Accuracy | Values reviewed; source verification required | Needs Verification |
| Consistency | 0 inconsistencies in attrition-reason check | Pass |
| Timeliness | Freshness SLA not verified | Needs Verification |
| Uniqueness | 0 duplicate employee IDs | Pass |
| Validity | 0 invalid age records (18–100 rule) | Pass |

## 3. Great Expectations Testing

- Total Expectations: 8
- Passed: 5
- Failed: 3
- Three failures were intentional test errors.
- GX successfully detected all three injected errors.

## 4. PII Classification

Personal identifiers: employee_id

Personal data: age, generation, gender

Confidential employee data: salary_usd, salary_vs_market_pct, burnout_score, manager_relationship_score, engagement_score, career_growth_score, attrition_reason.

## 5. Improvement Recommendations

1. Verify employee information against trusted source records.
2. Define and monitor a data freshness SLA.
3. Run automated Great Expectations checks during every data pipeline execution.
4. Tokenise employee identifiers and mask personal information in reports.
5. Apply role-based access control to confidential employee data.

## 6. Conclusion

The dataset passed the four initial quality checks for completeness, uniqueness, validity and the tested consistency rule. Accuracy and timeliness require further verification. Great Expectations successfully detected all three intentionally injected data quality errors.