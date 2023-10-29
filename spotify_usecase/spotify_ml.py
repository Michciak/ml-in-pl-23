import streamlit as st

from utils import load_data
from utils import prepare_data
from utils import produce_confusion
from utils import produce_roc
from utils import round_p
from utils import train_model

st.set_page_config(page_title="Spotify ML", layout="wide")
st.title("Spotify: Predict in Spotify chart")

df, y = load_data()
X_train, X_test, y_train, y_test = prepare_data(df, y)

with st.expander("Data preview"):
    st.dataframe(df.head(15))

#######
# TUTORIAL -
# CREATE THE INPUTS FOR EACH HYPERPARAMETER
#######

with st.sidebar.form(key="hyperparameters_form"):
    st.header("Model Configuration")

    ###### Widgets in here won't rerun the app at every interaction
    random_state = st.slider("random state",0,100,42,1)
    criterion = st.selectbox("criterion", ["gini"])
    n_estimators = st.slider("n estimators",0,100,25,1)
    max_depth = st.slider("max depth",0,100,25,1)
    min_samples_split = st.slider("min samples split",2, 100, 50, 1)
    min_samples_leaf = st.slider("min samples leaf",1,100,50,1)
    max_features = st.slider("max features", 1,50,25,1)
    bootstrap = st.toggle("bootstarp", value = True)
    n_jobs = st.slider("n jobs",-1,10,-1,1)
    max_samples = st.slider("max samples",0.0,1.0,0.8,0.01)

    submit_button = st.form_submit_button("Click here to run model", type="primary")

if submit_button:
    hyperparameters = {
        "random_state": random_state,
        "criterion": criterion,
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "max_features": max_features,
        "bootstrap": bootstrap,
        "n_jobs": n_jobs,
        "max_samples": max_samples,
    }
    (
        train_score,
        test_score,
        precision,
        recall,
        f1,
        confusion,
        seconds_run,
        fpr,
        tpr,
        roc_auc,
    ) = train_model(hyperparameters, X_train, X_test, y_train, y_test)

    st.write(f"Model ran in: {round(seconds_run, 4)} seconds")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.metric(label="Training Score", value=round_p(train_score))

    with c2:
        st.metric(
            label="Test Score",
            value=round_p(test_score),
            delta=round_p(test_score - train_score),
        )

    with c3:
        st.metric(label="Precision", value=round_p(precision))

    with c4:
        st.metric(label="Recall", value=round_p(recall))

    with c5:
        st.metric(label="F1", value=round_p(f1))

    col1, col2 = st.columns(2)

    with col1:
        st.altair_chart(produce_confusion(confusion), use_container_width=True)

    with col2:
        st.altair_chart(produce_roc(fpr, tpr, roc_auc), use_container_width=True)
