import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

st.set_page_config(
    page_title="R.pacifica INDKK - Lipid ML Optimization",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = joblib.load("model/xgboost_lipid_model.pkl")
features = joblib.load("model/features.pkl")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("Model Dashboard")

st.sidebar.subheader("Model Statistics")
st.sidebar.write("Model: XGBoost Regressor")
st.sidebar.write("LOOCV R²: 0.91")
st.sidebar.write("Test R²: 0.94")
st.sidebar.write("RMSE: ~0.45")
st.sidebar.write("Features: 4")

st.sidebar.subheader("Input Parameters")

glucose = st.sidebar.slider("Glucose (% w/v)", 4.0, 8.0, 6.0)
ammonium = st.sidebar.slider("Ammonium sulphate (% w/v)", 0.1, 0.3, 0.2)
ph = st.sidebar.slider("Initial pH", 3.5, 7.0, 5.0)
time = st.sidebar.slider("Cultivation time (h)", 120, 220, 168)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("R.pacifica INDKK - Lipid Fermentation Optimization")
st.write("Machine Learning model for predicting and optimizing lipid production")

# --------------------------------------------------
# OPTIMIZATION FUNCTIONS
# --------------------------------------------------
def random_search_optimization(model, features, n_iter=5000):
    grid = pd.DataFrame({
        features[0]: np.random.uniform(4, 8, n_iter),
        features[1]: np.random.uniform(0.1, 0.3, n_iter),
        features[2]: np.random.uniform(3.5, 7, n_iter),
        features[3]: np.random.uniform(120, 220, n_iter)
    })

    preds = model.predict(grid)

    best_idx = np.argmax(preds)
    best_value = preds[best_idx]
    best_conditions = grid.iloc[best_idx]

    return best_value, best_conditions


def grid_refinement(model, features, center, step=0.2):
    g = np.linspace(center[0]-step, center[0]+step, 15)
    a = np.linspace(center[1]-step/5, center[1]+step/5, 15)
    p = np.linspace(center[2]-step, center[2]+step, 15)
    t = np.linspace(center[3]-10, center[3]+10, 15)

    G, A, P, T = np.meshgrid(g, a, p, t)

    grid = pd.DataFrame({
        features[0]: G.ravel(),
        features[1]: A.ravel(),
        features[2]: P.ravel(),
        features[3]: T.ravel()
    })

    preds = model.predict(grid)

    best_idx = np.argmax(preds)
    best_value = preds[best_idx]
    best_conditions = grid.iloc[best_idx]

    return best_value, best_conditions

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Single Prediction",
    "Batch Prediction",
    "Optimization",
    "Figures"
])

# --------------------------------------------------
# SINGLE PREDICTION
# --------------------------------------------------
with tab1:
    st.subheader("Single Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Input Values")
        st.write("Glucose:", glucose)
        st.write("Ammonium:", ammonium)
        st.write("pH:", ph)
        st.write("Time:", time)

    with col2:
        if st.button("Predict Lipid Titer"):
            X = pd.DataFrame([[glucose, ammonium, ph, time]], columns=features)
            pred = model.predict(X)[0]
            st.metric("Predicted Lipid Titer (g/L)", f"{pred:.2f}")

# --------------------------------------------------
# BATCH PREDICTION
# --------------------------------------------------
with tab2:
    st.subheader("Batch Prediction (Upload CSV)")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        data = data[features]

        predictions = model.predict(data)
        data["Predicted_Lipid_Titer"] = predictions

        st.dataframe(data)

        csv = data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Predictions CSV",
            data=csv,
            file_name="lipid_predictions.csv",
            mime="text/csv",
        )

# --------------------------------------------------
# OPTIMIZATION
# --------------------------------------------------
with tab3:
    st.subheader("Find Optimal Fermentation Conditions")

    if st.button("Run Optimization"):

        with st.spinner("Running Random Search Optimization..."):
            best_value, best_conditions = random_search_optimization(model, features)

        with st.spinner("Refining Optimization..."):
            refined_value, refined_conditions = grid_refinement(
                model,
                features,
                best_conditions.values
            )

        st.success("Optimization Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### Optimal Conditions")
            st.write(refined_conditions)

        with col2:
            st.metric("Maximum Predicted Lipid (g/L)", f"{refined_value:.2f}")

# --------------------------------------------------
# FIGURES
# --------------------------------------------------
with tab4:
    st.subheader("Model Figures")

    fig_folder = "figures"

    if os.path.exists(fig_folder):
        images = sorted(os.listdir(fig_folder))

        cols = st.columns(2)

        for i, img in enumerate(images):
            with cols[i % 2]:
                st.image(
                    os.path.join(fig_folder, img),
                    caption=img,
                    use_container_width=True
                )
    else:
        st.write("No figures folder found.")