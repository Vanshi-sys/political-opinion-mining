
import json
from pathlib import Path
import pandas as pd
import streamlit as st

HERE = Path(__file__).parent
m = json.loads((HERE / "dashboard_metrics.json").read_text(encoding="utf-8"))

st.set_page_config(page_title="Political Opinion Mining", layout="wide")
st.title("Explainable, Context-Aware Political Opinion Mining")
st.caption("Indian social media | Exploratory research prototype")

st.warning(
    "Research prototype: results are based on a small, provisionally labelled "
    "dataset and repeated cross-validation. They are not independent test results."
)

a, b, c, d = st.columns(4)
a.metric("Eligible stance records", m["eligible_records"])
b.metric("Aggregate OOF accuracy", f'{m["accuracy"]:.1%}')
c.metric("Aggregate OOF macro-F1", f'{m["macro_f1"]:.3f}')
d.metric("Macro precision", f'{m["macro_precision"]:.3f}')

st.subheader("Stance label distribution")
st.bar_chart(pd.Series(m["label_distribution"], name="Records"))

st.subheader("Political target distribution")
st.bar_chart(pd.Series(m["target_distribution"], name="Records"))

st.subheader("Evaluation interpretation")
st.write(
    "The baseline combines word-level and character-level TF-IDF features "
    "with Logistic Regression. Character n-grams can help capture spelling "
    "variation and transliterated or code-mixed text. This baseline does not "
    "by itself resolve sarcasm, missing conversational context, or ambiguous targets."
)

st.subheader("Limitations and responsible use")
for item in m["limitations"]:
    st.write("- " + item)

st.info(
    "Do not interpret model predictions as verified political opinions. "
    "Human review and context are necessary for ambiguous examples."
)
