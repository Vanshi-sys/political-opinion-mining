# Project Report
## Explainable, Context-Aware Political Opinion Mining for Indian Social Media

### 1. Abstract

This project investigates an NLP workflow for identifying political content and
classifying stance in Indian social-media text. The work includes political
content detection artifacts, a TF-IDF-based stance baseline, repeated
cross-validation, error analysis, manual review, adjudication records, and a
Streamlit dashboard. The current stance evaluation is exploratory because the
labelled dataset is small and provisional.

### 2. Problem statement

Political social-media messages can contain Hindi, English, transliteration,
code-mixing, sarcasm, implicit references, and targets that are unclear without
surrounding context. These properties make automated political-content and
stance classification challenging. The project explores a reproducible baseline
and a workflow that keeps model predictions separate from human annotation
decisions.

### 3. Objectives

1. Support identification of political content.
2. Establish a reproducible baseline for binary stance classification.
3. Examine errors and potential language- and target-related difficulties.
4. preserve annotation provenance through review and separate adjudication.
5. Present recorded results and limitations through a dashboard.
6. Identify the work needed for context-aware and multilingual extensions.

### 4. Methodology

#### 4.1 Political-content detection

The project contains a political-content detection baseline and associated
evaluation artifacts. Previously recorded baseline results report accuracy
0.8242 and macro-F1 0.8238. These values should be cited as the recorded
detection baseline, not as proof of production readiness.

#### 4.2 Stance dataset

The evaluated stance subset contains **66 records**:
**36 Oppose** and
**30 Support**.
The records are provisionally labelled. Target representation is uneven:
BJP: 41, INC: 21, AAP: 3, Trinamool Congress: 1.

#### 4.3 Stance baseline

The recorded baseline combines word-level TF-IDF n-grams and character-level
TF-IDF n-grams using a feature union. Logistic Regression is used with
class balancing. Feature extraction is fitted within the training folds.

#### 4.4 Evaluation protocol

Repeated stratified 5-fold cross-validation with 5 repeats and random seed 42
was used, yielding 25 fold evaluations. The report distinguishes mean fold
metrics from aggregate predictions formed by majority voting across repeated
held-out predictions. Aggregate repeated-CV predictions are correlated across
repeats and are not an independent test set.

### 5. Results

#### 5.1 Stance classification

| Metric | Aggregate repeated-CV result |
|---|---:|
| Accuracy | 0.6364 |
| Macro precision | 0.6339 |
| Macro recall | 0.6250 |
| Macro-F1 | 0.6239 |

The recorded fold-level mean accuracy is 0.6002
(SD, population convention: 0.0960) and the
mean fold macro-F1 is 0.5829
(SD, population convention: 0.1051).

The aggregate confusion matrix, with rows representing recorded labels and
columns representing predictions, is:

| Recorded label | Predicted Oppose | Predicted Support |
|---|---:|---:|
| Oppose | 27 | 9 |
| Support | 15 | 15 |

Support recall is lower than Oppose recall in the aggregate report. This
suggests that the current baseline misses a meaningful portion of Support
examples. The small dataset means these findings should be interpreted cautiously.

#### 5.2 Error analysis and human review

The recorded error-analysis artifacts identify 24 misclassified records out
of 66 aggregate repeated-CV predictions. The error-analysis report explicitly
treats automated error categories as review prompts rather than proof that
labels are incorrect. A manual-review file contains 24 review records:
21 marked Retain, 2 Need context, and 1 Propose change. A separate adjudication
record covers three cases and retains their original stances. No master labels
were changed by these review steps.

### 6. Dashboard

The Streamlit dashboard displays the recorded stance metrics, stance label
distribution, political-target distribution, and limitations. It is a
visualization of existing evaluation artifacts, not a live inference service.

### 7. Limitations

- The stance evaluation has only 66 eligible records.
- Labels are provisional and may contain ambiguity.
- Repeated cross-validation is not independent external validation.
- Target classes are highly imbalanced.
- Context, sarcasm, transliteration, and code-mixing remain challenging.
- A multilingual transformer experiment has not been verified in the available
  artifacts.
- A fully implemented context/entity model, explainability method, and
  comprehensive ablation study should not be claimed without corresponding
  verified implementation and results.

### 8. Ethical considerations

Political stance predictions should not be treated as definitive evidence of
a person's beliefs or political affiliation. The system should not be used to
profile individuals. Ambiguous or context-dependent messages should be referred
for human assessment, and dataset provenance and limitations should be disclosed.

### 9. Conclusion

The project establishes a baseline workflow and an audit trail for political
content detection and exploratory binary stance classification. The recorded
stance results demonstrate a workable experimental pipeline, but not reliable
deployment performance. The most important next steps are to expand and review
the labelled dataset, evaluate multilingual transformer models under a fair
protocol, add verified target/context analysis, and test on an independent set.

### 10. Reproducibility note

The project retains its protected master annotation file separately from
generated deliverables. Existing baseline metrics are reported as recorded;
this report does not retrain models or alter labels.

---
Generated from existing project artifacts on 2026-10-17.
