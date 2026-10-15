# Ethics, Limitations, and Responsible Use

## Historical and geographic scope

The dataset describes credit-card clients in Taiwan and repayment history from 2005. It is not a representative sample of current applicants, current lending practices, or other countries.

## Sensitive attributes and proxies

The source includes sex, age, and marital-status attributes. Other financial and repayment variables may also act as proxies for protected or sensitive characteristics. A high predictive score does not demonstrate fairness.

## Outcome limitations

Historical default is an observed outcome shaped by past lending policies, credit limits, economic conditions, and customer circumstances. It is not a complete measure of an individual's financial reliability or ability to repay.

## Model limitations

The baseline models and holdout evaluation are educational. They are not independently validated, calibrated for operational use, audited for fairness, or assessed for legal/regulatory suitability. Performance can vary with data splits and modelling choices.

## Responsible-use rules

- Do not use these models to make real credit approvals, denials, credit-limit decisions, or pricing decisions.
- Do not claim that results generalize to today's borrowers or to another country.
- Do not treat feature importance or coefficients as causal explanations.
- Report class-specific metrics and limitations, not only accuracy.
- Keep data provenance and attribution with the project.
- Any real-world application would require appropriate legal review, data governance, explainability, fairness testing, monitoring, and human oversight.

## Source

Yeh, I. (2009). *Default of Credit Card Clients* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H. CC BY 4.0.
