import streamlit as st
import pickle


model = pickle.load(open('saved_model/spam_model.pkl', 'rb'))


st.set_page_config(page_title="Spam Email Classifier", page_icon="📧", layout="centered", initial_sidebar_state="collapsed")
st.title("Spam Email Classifier")
st.markdown("Paste your email content below to check if it's **SPAM** or **NOT SPAM**.")

email_text = st.text_area("Enter Email Content:")

if st.button("Check"):
    if email_text.strip():
        prediction = model.predict([email_text])[0]
        result = "**SPAM**" if prediction == 1 else "**NOT SPAM**"
        st.subheader(result)
    else:
        st.warning("⚠Please enter email content.")
