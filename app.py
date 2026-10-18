import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

HERE = Path(__file__).parent
metrics = json.loads(
    (HERE / "dashboard_metrics.json").read_text(encoding="utf-8")
)

st.set_page_config(
    page_title="Political Opinion Mining",
    page_icon="📊",
    layout="wide"
)

st.title("Explainable, Context-Aware Political Opinion Mining")
st.caption("Indian social media | Exploratory research prototype")

st.warning(
    "Research prototype: stance results are based on a small, provisionally "
    "labelled dataset and repeated cross-validation. They are not independent "
    "test results."
)

a, b, c, d = st.columns(4)
a.metric("Eligible stance records", metrics["eligible_records"])
b.metric("Aggregate OOF accuracy", f'{metrics["accuracy"]:.1%}')
c.metric("Aggregate OOF macro-F1", f'{metrics["macro_f1"]:.3f}')
d.metric("Macro precision", f'{metrics["macro_precision"]:.3f}')

st.subheader("Stance label distribution")
st.bar_chart(pd.Series(metrics["label_distribution"], name="Records"))

st.subheader("Political target distribution")
st.bar_chart(pd.Series(metrics["target_distribution"], name="Records"))

st.subheader("Live political-content detection")
st.write(
    "Enter a message to estimate whether its content is political. "
    "This model does not predict support or opposition toward a party."
)

@st.cache_resource
def load_political_detector():
    model_path = HERE / "political_detection_word_char_logreg.joblib"
    return joblib.load(model_path)

text_input = st.text_area(
    "Message to analyse",
    placeholder="Paste a short social-media post here...",
    height=130,
    key="political_text_input"
)

if st.button("Predict political content", type="primary"):
    if not text_input.strip():
        st.warning("Enter a message first.")
    else:
        try:
            detector = load_political_detector()
            prediction = int(detector.predict([text_input])[0])
            classes = list(detector.classes_)

            if hasattr(detector, "predict_proba"):
                probabilities = detector.predict_proba([text_input])[0]
                class_probabilities = {
                    int(label): float(prob)
                    for label, prob in zip(classes, probabilities)
                }
                score = class_probabilities.get(prediction)

            label_text = (
                "Political" if prediction == 1 else "Non-political"
            )

            st.markdown(f"### Prediction: {label_text}")

            if score is not None:
                st.metric("Predicted-class probability", f"{score:.1%}")

            st.caption(
                "This is an automated estimate, not a verified interpretation. "
                "The probability is not necessarily calibrated and can be "
                "unreliable for sarcasm, code-mixed text, short messages, "
                "or text unlike the training data."
            )
        except Exception as exc:
            st.error(
                "Prediction failed. Check that the saved model and compatible "
                "scikit-learn/joblib dependencies are available."
            )
            st.exception(exc)

st.subheader("Stance baseline interpretation")
st.write(
    "The stance baseline combines word-level and character-level TF-IDF "
    "features with Logistic Regression. Character n-grams can help capture "
    "spelling variation and transliterated or code-mixed text. This baseline "
    "does not by itself resolve sarcasm, missing conversational context, "
    "or ambiguous targets."
)

st.subheader("Limitations and responsible use")
for item in metrics["limitations"]:
    st.write("- " + item)

st.info(
    "Do not interpret predictions as verified political opinions or political "
    "affiliations of individuals. Human review and context are necessary for "
    "ambiguous examples."
)
