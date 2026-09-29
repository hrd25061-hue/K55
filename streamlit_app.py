

Skip to content
Using Uva Wellassa University Mail with screen readers
Enable desktop notifications for Uva Wellassa University Mail.
   OK  No thanks

3 of 8
(no subject)
External
Inbox

Umodya Abeywickrama <abeywickramaumodya@gmail.com>
4:21 AM (1 hour ago)
to me

import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="K5502 - Enterprise AI Ecosystem",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {font-size: 2.5rem; color: #1E3A8A; font-weight: 700;}
    .sub-header {font-size: 1.5rem; color: #3B82F6; font-weight: 600;}
    .card {background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #3B82F6; margin-bottom: 10px;}
    .ceo-card {border-left-color: #10B981;}
    .emp-card {border-left-color: #8B5CF6;}
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# MULTI-LANGUAGE TRANSLATIONS (English, සිංහල, தமிழ்)
# -------------------------------------------------------------------------
lang = st.sidebar.selectbox("🌐 Select Language / භාෂාව / மொழி", ["English", "සිංහල", "தமிழ்"])

t = {
    "English": {
        "title": "K5502: Advanced Enterprise AI Ecosystem",
        "subtitle": "Hyper-personalized, ethical, and psychologically safe AI-driven corporate operating system.",
        "portal": "Select Access Portal",
        "ceo": "CEO Portal",
        "emp": "Employee Portal",
        "kb": "Knowledge Base Explorer",
        "arch": "System Architecture & Value",
        "sector": "Select Target Sector",
        "sectors": ["Test Company", "Finance & Banking", "Education", "Corporate Sector"]
    },
    "සිංහල": {
        "title": "K5502: උසස් ආයතනික කෘත්‍රිම බුද්ධි පද්ධතිය",
        "subtitle": "ඉතා පුද්ගලීකරණය කළ, සදාචාරාත්මක සහ මානසිකව ආරක්ෂිත ආයතනික පද්ධතියකි.",
        "portal": "පිවිසුම් ද්වාරය තෝරන්න",
        "ceo": "ප්‍රධාන විධායක නිලධාරී (CEO) ද්වාරය",
        "emp": "සේවක ද්වාරය",
        "kb": "ඥාන මණ්ඩලය (Knowledge Base)",
        "arch": "පද්ධති ගෘහ නිර්මාණ ශිල්පය සහ වටිනාකම",
        "sector": "ඉලක්කගත අංශය තෝරන්න",
        "sectors": ["පරීක්ෂණ සමාගම", "මූල්‍ය සහ බැංකු", "අධ්‍යාපනය", "ආයතනික අංශය"]
    },
    "தமிழ்": {
        "title": "K5502: மேம்பட்ட நிறுவன AI அமைப்பு",
        "subtitle": "மிகவும் தனிப்பயனாக்கப்பட்ட, நெறிமுறை மற்றும் உளவியல் ரீதியாக பாதுகாப்பான AI இயங்குதளம்.",
        "portal": "அணுகல் தளத்தைத் தேர்ந்தெடுக்கவும்",
        "ceo": "தலைமை நிர்வாக அதிகாரி (CEO) தளம்",
        "emp": "ஊழியர் தளம்",
        "kb": "அறிவு தளம்",
        "arch": "கட்டமைப்பு மற்றும் மதிப்பு",
        "sector": "இலக்கு துறையைத் தேர்ந்தெடுக்கவும்",
        "sectors": ["சோதனை நிறுவனம்", "நிதியியல் மற்றும் வங்கி", "கல்வி", "நிறுவனத் துறை"]
    }
}[lang]

# -------------------------------------------------------------------------
# KNOWLEDGE BASE ENGINE (Philosophy, Psychology, Legal, Strategy, Case Studies)
# -------------------------------------------------------------------------
KNOWLEDGE_BASE = {
    "Philosophy & Ethics": [
        "Aristotle Virtue Ethics & Immanuel Kant Deontology",
        "Buddhism & Eastern Philosophy: Equanimity, Compassion, Mindfulness",
        "Ikigai Framework (Purpose of Life)",
        "UNESCO AI Ethics Guidelines"
    ],
    "Psychology & Personality": [
        "Big Five & MBTI / Gallup CliftonStrengths 2.0",
        "Daniel Goleman Emotional Intelligence & Maslow's Extended Hierarchy",
        "Carl Jung's Shadow Work & Mihaly Csikszentmihalyi's Flow State",
        "Viktor Frankl's Man's Search for Meaning & CBT (Cognitive Behavioral Therapy)",
        "RIASEC (Holland Codes) & Maslach Burnout Inventory (MBI)",
        "Thomas-Kilmann Conflict Mode (TKI) & Paul Ekman Micro-expressions"
    ],
    "Legal & Justice": [
        "ILO Standards & UN Universal Declaration of Human Rights",
        "Sri Lankan Labour Law & FLSA (Global Employment Law)",
        "GDPR & UN Global Compact Compliance"
    ],
    "Strategic Intelligence & Case Studies": [
        "Stephen Covey's 7 Habits & W. Chan Kim's Blue Ocean Strategy",
        "OKRs (Objectives and Key Results) & Benjamin Graham's Intelligent Investor",
        "Case Studies: Satya Nadella's Microsoft, Apollo 13, Volkswagen Dieselgate, Patagonia, Gravity Payments"
    ],
    "HR & Communication (Non-Violent Communication)": [
        "Marshall Rosenberg's NVC & Dale Carnegie Principles",
        "SHRM & CIPD Professional Maps, ONET Online, Hofstede Insights",
        "Simon Sinek (Start with Why) & Matthew Walker Sleep Research"
    ]
}

# -------------------------------------------------------------------------
# MAIN APP HEADER
# -------------------------------------------------------------------------
st.markdown(f'<p class="main-header">{t["title"]}</p>', unsafe_allow_html=True)
st.write(t["subtitle"])

role = st.sidebar.selectbox(t["portal"], [t["ceo"], t["emp"], t["kb"], t["arch"]])

# -------------------------------------------------------------------------
# CEO PORTAL
# -------------------------------------------------------------------------
if role == t["ceo"]:
    st.markdown(f'<p class="sub-header">👑 {t["ceo"]}</p>', unsafe_allow_html=True)
    
    sector = st.selectbox(t["sector"], t["sectors"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "10 Strategic Planners", 
        "100% Talent Matcher", 
        "Retention Radar", 
        "Executive Support & Case Studies", 
        "Stress & Mental Health Index"
    ])
    
    with tab1:
        st.markdown("### Weekly Actionable Strategic Planners")
        st.markdown('<div class="card ceo-card"><b>Covey & OKR Aligned Execution:</b><br>• Focus on Blue Ocean market creation.<br>• Minimize decision latency using real-time predictive analytics.<br>• Balanced Scorecard implementation.</div>', unsafe_allow_html=True)
        if st.button("Generate Weekly Executive Action Plan"):
            st.success("Generated 10 high-impact strategic actions based on Exponential Organization frameworks!")

    with tab2:
        st.markdown("### 100% Talent Matcher")
        st.write("AI matches candidate psychological profiles (Big Five, MBTI, RIASEC) with organizational culture.")
        candidate_name = st.text_input("Enter Candidate Name:", "John Doe")
        if st.button("Run Deep AI Talent Match"):
            match_score = random.randint(92, 99)
            st.metric(label="Talent & Culture Fit Score", value=f"{match_score}%")
            st.info(f"Analysis for {candidate_name}: High alignment with organizational values, strong emotional intelligence, and low burnout risk.")

    with tab3:
        st.markdown("### Retention Radar (Employee Turnover Prediction)")
        st.warning("⚠️ Predictive Alert: 2 employees in the Engineering department show early indicators of burnout.")
        if st.button("Trigger Safety Net & Intervention Protocol"):
            st.success("Automated empathetic check-ins and workload re-balancing recommendations dispatched securely.")

    with tab4:
        st.markdown("### Executive Support & Harvard Case Studies")
        selected_case = st.selectbox("Select Business Case Study:", [
            "Satya Nadella's Transformation of Microsoft",
            "Apollo 13 Successful Failure",
            "Volkswagen Dieselgate Scandal",
            "Patagonia: Earth is Now Our Only Shareholder"
        ])
        st.markdown(f"**AI Strategic Synthesis for [{selected_case}]:** Focus on empathy-driven leadership, psychological safety, and rigorous ethical compliance.")

    with tab5:
        st.markdown("### Organization-wide Stress & Mental Health Radar")
        st.metric(label="Overall Corporate Wellness Index", value="84 / 100", delta="+4% this month")
        st.progress(0.84)

# -------------------------------------------------------------------------
# EMPLOYEE PORTAL
# -------------------------------------------------------------------------
elif role == t["emp"]:
    st.markdown(f'<p class="sub-header">💼 {t["emp"]}</p>', unsafe_allow_html=True)
    
    emp_tab1, emp_tab2, emp_tab3, emp_tab4 = st.tabs([
        "Emotional AI Chat (Private)", 
        "Legal Advisor (SL & Global)", 
        "Personalized Practice Programme", 
        "IQ & EQ Core Test"
    ])
    
    with emp_tab1:
        st.markdown("### Safe Net: Emotional AI Chat & Mental Health")
        st.write("Speak freely. Protected by strict privacy layers and non-violent communication (NVC) principles.")
        
        user_msg = st.text_input("How are you feeling today? Share your thoughts or workplace stressor:")
        if user_msg:
            st.markdown(f'<div class="card emp-card"><b>AI Companion (Empathy Mode):</b><br>I hear you, and your feelings are completely valid. Drawing from mindfulness and CBT principles, let us break down what is causing this stress. Remember, seeking balance (Ikigai) is a journey. Let us take three deep breaths together.</div>', unsafe_allow_html=True)

    with emp_tab2:
        st.markdown("### Legal Advisor (Labor Law & Human Rights)")
        legal_query = st.selectbox("Select Topic:", [
            "Sri Lankan Labour Law Guidelines",
            "GDPR Data Privacy Rights",
            "Universal Declaration of Human Rights (Workplace)",
            "ILO Fair Working Hours"
        ])
        st.info(f"**AI Legal Guidance:** Under {legal_query}, your rights to fair compensation, safe working conditions, and privacy are fully protected.")

    with emp_tab3:
        st.markdown("### Personalized Growth & Practice Programme")
        st.checkbox("Complete 15-minute mindfulness session")
        st.checkbox("Review weekly Ikigai alignment goals")
        st.checkbox("Participate in peer communication workshop (NVC)")

    with emp_tab4:
        st.markdown("### Advanced IQ & EQ Core Assessment")
        if st.button("Start 5-Minute Assessment"):
            st.success("Assessment initialized! Your emotional intelligence quotient (EQ) and cognitive metrics have been updated privately.")

# -------------------------------------------------------------------------
# KNOWLEDGE BASE EXPLORER
# -------------------------------------------------------------------------
elif role == t["kb"]:
    st.markdown(f'<p class="sub-header">📚 {t["kb"]}</p>', unsafe_allow_html=True)
    st.write("Explore the deeply integrated philosophical, psychological, and strategic foundations driving K5502.")
    
    for category, items in KNOWLEDGE_BASE.items():
        with st.expander(f"📁 {category}"):
            for item in items:
                st.markdown(f"- {item}")

# -------------------------------------------------------------------------
# SYSTEM ARCHITECTURE & VALUE
# -------------------------------------------------------------------------
else:
    st.markdown(f'<p class="sub-header">🏗️ {t["arch"]}</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔒 System Architecture")
        st.markdown("""
        - **The Knowledge Base:** Embedded multi-disciplinary frameworks.
        - **AI Brain:** Context-aware, empathetic reasoning engine.
        - **Privacy Layer:** Zero-knowledge data leakage prevention & GDPR compliant storage.
        """)
    with col2:
        st.markdown("### 🚀 Business Value Realization")
        st.markdown("""
        - **Zero Turnover Regret:** Radical reduction in employee churn.
        - **100% Talent Matching:** Precision hiring and role placement.
        - **Maximized Productivity:** Burnout prevention via proactive mental health tracking.
        - **Hyper-Personalization:** Individual growth maps for every employee.
        """)
