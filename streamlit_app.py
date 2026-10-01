import streamlit as st

# ── Shared assessment contracts (frontend ↔ backend equivalents) ──

LANGUAGES = [
    {"code": "en", "label": "English", "native": "English"},
    {"code": "si", "label": "Sinhala", "native": "සිංහල"},
    {"code": "ta", "label": "Tamil", "native": "தமிழ்"},
]

LANGUAGE_NAMES = {
    "en": "English",
    "si": "Sinhala",
    "ta": "Tamil",
}

# Streamlit App Interface Example
st.title("Aptitude — AI Career Guidance & Potential Assessment")

selected_lang = st.selectbox(
    "Select Language / භාෂාව තෝරන්න / மொழியைத் தேர்ந்தெடுக்கவும்",
    options=[lang["code"] for lang in LANGUAGES],
    format_func=lambda x: LANGUAGE_NAMES[x]
)

st.write(f"Selected Language code: {selected_lang}")

# User input & Assessment Profile structure simulation
name = st.text_input("Enter your name:")
interests = st.text_area("Your interests or career goals:")

if st.button("Start Assessment"):
    if name:
        st.success(f"Welcome, {name}! Assessment engine initialized successfully.")
    else:
        st.warning("Please enter your name to proceed.")

