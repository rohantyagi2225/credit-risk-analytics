# Dataset Card — Default of Credit Card Clients

## Identity and source

- **Official title:** Default of Credit Card Clients
- **Repository:** UCI Machine Learning Repository, dataset ID 350
- **Dataset DOI:** https://doi.org/10.24432/C55S3H
- **Creator listed by UCI:** I-Cheng Yeh
- **Research paper:** Yeh, I. C., & Lien, C. H. (2009). *The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients*. Expert Systems with Applications.
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0). Preserve attribution and indicate project changes.
- **Official source:** https://archive.ics.uci.edu/dataset/350/defaultofcreditcardclients

## Contents

UCI documents 30,000 instances and 23 explanatory variables. The data describes credit-card clients in Taiwan, including credit limits, demographic attributes, repayment status, bill statements, and previous payments. The outcome is whether the client defaulted on payment in the following month.

The repayment and billing history covers April–September 2005. This is historical data; it should not be described as representative of today's credit market.

## Acquisition and reproducibility

The project retrieves the data from UCI using the `ucimlrepo` package:

```bash
pip install -r requirements.txt
```

```python
from ucimlrepo import fetch_ucirepo
dataset = fetch_ucirepo(id=350)
X = dataset.data.features
y = dataset.data.targets
```

An internet connection is required to download the dataset. The raw dataset is not duplicated in this repository; the notebook and script retrieve it from the official source.

## Intended use

Educational exploratory data analysis, baseline classification, model evaluation practice, and discussion of credit-risk modelling limitations.

## Out-of-scope use

Do not use this project to approve or reject actual applicants, set credit limits, price credit, or make other consequential financial decisions. The historical sample and baseline workflow are not validated for operational use.

## Known considerations

- Historical data and local context limit generalizability.
- The dataset contains sensitive/proxy attributes such as sex, age, and marital status.
- The target is an observed historical outcome, not a perfect measure of creditworthiness.
- Class imbalance means accuracy alone is insufficient.
- Data cleaning, feature choices, thresholds, and evaluation splits can materially affect conclusions.

## Attribution

Yeh, I. (2009). *Default of Credit Card Clients* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H. Licensed under CC BY 4.0.
