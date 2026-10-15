# Data Dictionary

Source: UCI Machine Learning Repository, [Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/defaultofcreditcardclients), DOI [10.24432/C55S3H](https://doi.org/10.24432/C55S3H).

The dataset has an identifier, 23 explanatory variables, and a binary target. The project normalizes UCI's coded feature names to the descriptive names below where needed.

| Source code | Project name | Meaning |
|---|---|---|
| ID | ID | Dataset row identifier; excluded from modelling |
| X1 | LIMIT_BAL | Credit limit in New Taiwan dollars |
| X2 | SEX | Sex code as documented by UCI |
| X3 | EDUCATION | Education category code |
| X4 | MARRIAGE | Marital status category code |
| X5 | AGE | Age in years |
| X6 | PAY_0 | Repayment status in September 2005 |
| X7 | PAY_2 | Repayment status in August 2005 |
| X8 | PAY_3 | Repayment status in July 2005 |
| X9 | PAY_4 | Repayment status in June 2005 |
| X10 | PAY_5 | Repayment status in May 2005 |
| X11 | PAY_6 | Repayment status in April 2005 |
| X12 | BILL_AMT1 | Bill statement amount, September 2005 |
| X13 | BILL_AMT2 | Bill statement amount, August 2005 |
| X14 | BILL_AMT3 | Bill statement amount, July 2005 |
| X15 | BILL_AMT4 | Bill statement amount, June 2005 |
| X16 | BILL_AMT5 | Bill statement amount, May 2005 |
| X17 | BILL_AMT6 | Bill statement amount, April 2005 |
| X18 | PAY_AMT1 | Previous payment amount, September 2005 |
| X19 | PAY_AMT2 | Previous payment amount, August 2005 |
| X20 | PAY_AMT3 | Previous payment amount, July 2005 |
| X21 | PAY_AMT4 | Previous payment amount, June 2005 |
| X22 | PAY_AMT5 | Previous payment amount, May 2005 |
| X23 | PAY_AMT6 | Previous payment amount, April 2005 |
| Y | default_next_month | Default payment outcome for the following month (1 = yes, 0 = no) |

## Coding notes

- Repayment-status codes include negative, zero, and positive values. Preserve the source meaning; do not assume that the values are a continuous measurement without justification.
- UCI's documented coding for SEX, EDUCATION, and MARRIAGE should be consulted before interpreting categories. Some category codes may represent "other" or undocumented/unknown categories.
- The target is renamed to `default_next_month` in this project for clarity.
- `ID` is a record identifier and must not be used as a predictive feature.

For the official definitions and coding details, see the [UCI dataset page](https://archive.ics.uci.edu/dataset/350/defaultofcreditcardclients).
