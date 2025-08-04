
import streamlit as st
import numpy as np
import joblib

linear_model = joblib.load("linear_model.pkl")
rf_model = joblib.load("rf_model.pkl")

st.title("🛸 UFO Galaxy RNG Tahmin Paneli")

user_input = st.text_input("Son 10 sayıyı gir (virgülle ayır):", "1.00, 1.00, 1.00, 44.27, 1.69, 96.30, 2.11, 3.00, 1.00, 2.55")

if st.button("TAHMİN ET"):
    try:
        numbers = [float(x.strip()) for x in user_input.split(",")]
        if len(numbers) != 10:
            st.warning("Lütfen tam 10 sayı gir.")
        else:
            arr = np.array(numbers).reshape(1, -1)
            st.write("🔄 Tahmin ediliyor...")
            st.success(f"🔮 Linear Regression Tahmini: {linear_model.predict(arr)[0]:.2f}")
            st.success(f"🌲 Random Forest Tahmini: {rf_model.predict(arr)[0]:.2f}")
    except:
        st.error("Lütfen geçerli sayılar gir.")
