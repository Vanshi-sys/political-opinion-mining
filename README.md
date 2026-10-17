# Explainable, Context-Aware Political Opinion Mining for Indian Social Media

## Overview

This research prototype explores political-content identification and stance
classification for Indian social-media text. The project addresses challenges
such as Hindi text, transliteration, code-mixing, ambiguous political targets,
sarcasm, and the need for human review.

The current implementation combines a political-content detection workflow,
a TF-IDF and Logistic Regression stance baseline, error analysis, manual review
artifacts, and a Streamlit dashboard.

## Current capabilities

- Political-content detection baseline and evaluation artifacts.
- A provisional binary stance dataset with Support and Oppose labels.
- Word-level and character-level TF-IDF features with Logistic Regression.
- Repeated stratified cross-validation for exploratory baseline evaluation.
- Error analysis and a manual review queue.
- Separate adjudication records and checks protecting the original annotations.
- A Streamlit dashboard for viewing recorded evaluation results and limitations.

## Model and evaluation

The stance baseline uses word n-grams and character n-grams combined through
a feature union, followed by Logistic Regression with class balancing.

The current stance evaluation uses 66 eligible records: 36 Oppose and 30
Support. Repeated stratified 5-fold cross-validation was performed over
5 repeats. The aggregate repeated-CV predictions are not an independent
test set, and the dataset is small and provisionally labelled.

See `project_report.md` and `dashboard_metrics.json` for the recorded results.

## Run the dashboard

Install the dependencies in your Python environment:

```bash
pip install streamlit pandas
```

Run the app from the directory containing `app.py` and `dashboard_metrics.json`:

```bash
streamlit run app.py
```

In Google Colab, the app can be run through a forwarded port. The dashboard
files are intended as a research demonstration, not a production deployment.

## Project files

- `app.py` — Streamlit dashboard.
- `dashboard_metrics.json` — recorded evaluation metrics and limitations.
- `manual_review_results.csv` — exported manual-review records, when available.
- `error_analysis_results.csv` — exported error-analysis records, when available.
- `project_report.md` — methodology, results, and limitations.

## Limitations

- The stance dataset contains only 66 eligible records.
- Stance labels are provisional human annotations.
- Repeated cross-validation does not replace evaluation on an independent test set.
- Political targets are unevenly represented, so subgroup metrics are uncertain.
- Sarcasm, code-mixing, transliteration, and missing context remain difficult cases.
- A multilingual transformer experiment has not been verified in the current artifacts.
- The dashboard displays recorded results; it is not a live political-opinion detector.

## Responsible use

Predictions should not be treated as verified beliefs or political affiliations
of individual users. Ambiguous messages require context and human assessment.
This prototype is intended for research and educational demonstration.

## Reproducibility and data integrity

The protected master annotation file is maintained separately from dashboard
outputs. Review and evaluation artifacts are preserved without automatically
overwriting source labels. Verify dataset versions and checksums before
reproducing any experiment.

## Future work

- Evaluate a multilingual transformer using a sufficiently reviewed dataset.
- Improve target-aware and context-aware stance classification.
- Study language-specific and code-mixed performance.
- Conduct controlled ablation and robustness experiments.
- Add prediction-time explanations and a clearly separated inference interface.
- Evaluate on a genuinely independent test set.
