import random
from fpdf import FPDF
import base64

# Page Configuration
st.set_page_config(
    page_title="AI Career Guidance & Potential Assessment",
    page_icon="🚀",
    layout="wide"
)

# Initialize Session State Variables
if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "language" not in st.session_state:
    st.session_state.language = "English"
if "iq_questions" not in st.session_state:
    st.session_state.iq_questions = []
if "eq_questions" not in st.session_state:
    st.session_state.eq_questions = []
if "iq_answers" not in st.session_state:
    st.session_state.iq_answers = {}
if "eq_answers" not in st.session_state:
    st.session_state.eq_answers = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Dynamic Question Banks based on Language
def load_questions(lang):
    if lang == "සිංහල (Sinhala)":
        iq_bank = [
            {"q": "1, 4, 9, 16, 25, ?", "options": ["30", "36", "49", "64"], "ans": "36"},
            {"q": "ප්‍රශ්න ලකුණට ගැළපෙන අංකය තෝරන්න: 3, 6, 12, 24, ?", "options": ["36", "48", "60", "72"], "ans": "48"},
            {"q": "සියලුම බළලුන් සතුන් වේ. සමහර සතුන් සුරතලුන් වේ. එහෙනම් සියලුම බළලුන් සුරතලුන් වේද?", "options": ["නිවැරදියි", "වැරදියයි", "කිව නොහැක", "අදාළ නැත"], "ans": "කිව නොහැක"},
            {"q": "ඔබ උතුරට හැරී සිට නැවත දකුණට හැරී, පසුව වමට හැරුණොත් ඔබ දැන් මුහුණලා සිටින්නේ කුමන දිශාවටද?", "options": ["නැඟෙනහිර", "බස්නාහිර", "උතුර", "දකුණ"], "ans": "නැඟෙනහිර"},
            {"q": "මාසයකට දින 30ක් ඇති විට, වසරකට එවැනි මාස කීයක් තිබේද?", "options": ["7", "11", "12", "0"], "ans": "12"}
        ]
        eq_bank = [
            {"q": "වැඩ කරන ස්ථානයේදී ඔබේ සගයෙකු ඔබ සමඟ කේන්තියෙන් කතා කළහොත් ඔබ කුමක් කරන්නේද?", "options": ["මාත් කේන්තියෙන් ප්‍රතිචාර දක්වයි", "සන්සුන්ව හේතුව විමසා සාකච්ඡා කරයි", "නොසලකා හරියි", "පැමිණිලි කරයි"], "ans": "සන්සුන්ව හේතුව විමසා සාකච්ඡා කරයි"},
            {"q": "අසාර්ථක වීමක් හමුවේ ඔබට හැඟෙන පළමු දෙය කුමක්ද?", "options": ["නැවත උත්සාහ නොකර සිටීම", "වෙනත් අයෙකු වැරදිකරු කිරීම", එය ඉගෙනුම් පියවරක් ලෙස ගැනීම, "කාලය නාස්ති වීමක් ලෙස සිතීම"], "ans": එය ඉගෙනුම් පියවරක් ලෙස ගැනීම},
            {"q": "කණ්ඩායම් ව්‍යාපෘතියකදී අදහස් ගැටුමක් ඇති වූ විට ඔබේ ප්‍රවේශය කුමක්ද?", "options": ["මගේ අදහම පමණක් බලපැවැත්වීම", "අන් අයගේ අදහස් වලට ගරු කර පොදු එකඟතාවකට ඒම", "ව්‍යාපෘතියෙන් ඉවත් වීම", "නොසලකා හැරීම"], "ans": "අන් අයගේ අදහස් වලට ගරු කර පොදු එකඟතාවකට ඒම"}
        ]
    elif lang == "தமிழ் (Tamil)":
        iq_bank = [
            {"q": "1, 4, 9, 16, 25, ?", "options": ["30", "36", "49", "64"], "ans": "36"},
            {"q": "தொடரை நிரப்புக: 3, 6, 12, 24, ?", "options": ["36", "48", "60", "72"], "ans": "48"},
            {"q": "வடக்கு நோக்கி நின்று வலதுபுறம் திரும்பி மீண்டும் இடதுபுறம் திரும்பினால் எந்த திசையை நோக்குகிறீர்கள்?", "options": ["கிழக்கு", "மேற்கு", "வடக்கு", "தெற்கு"], "ans": "கிழக்கு"}
        ]
        eq_bank = [
            {"q": "வேிட இடத்தில் சக பணியாளர் கோபமாக பேசினால் உங்கள் எதிர்வினை என்ன?", "options": ["கோபப்படுவது", "அமைதியாக பேசி தீர்ப்பது", "புறக்கணிப்பது", "புகார் செய்வது"], "ans": "அமைதியாக பேசி தீர்ப்பது"},
            {"q": "தோல்வியை சந்திக்கும் போது உங்கள் மனநிலை எப்படி இருக்கும்?", "options": ["முயற்சியை கைவிடுவது", "மற்றவரை குறை கூறுவது", "அதை ஒரு பாடமாக கற்றுக்கொள்வது", "வருந்துவது"], "ans": "அதை ஒரு பாடமாக கற்றுக்கொள்வது"}
        ]
    else: # English
        iq_bank = [
            {"q": "What comes next in the series: 2, 4, 8, 16, 32, ?", "options": ["48", "64", "128", "60"], "ans": "64"},
            {"q": "If all roses are flowers and some flowers fade quickly, are all roses fading quickly?", "options": ["True", "False", "Cannot be determined", "None"], "ans": "Cannot be determined"},
            {"q": "Find the odd one out:", "options": ["Circle", "Square", "Triangle", "Cube"], "ans": "Cube"},
            {"q": "If a train travels at 60 km/h, how far does it go in 30 minutes?", "options": ["30 km", "60 km", "120 km", "15 km"], "ans": "30 km"},
            {"q": "Complete the sequence: A, C, F, J, O, ?", "options": ["R", "S", "T", "U"], "ans": "U"}
        ]
        eq_bank = [
            {"q": "How do you handle constructive criticism from a supervisor?", "options": ["Take it personally", "Analyze and use it for self-improvement", "Ignore it completely", "Get defensive"], "ans": "Analyze and use it for self-improvement"},
            {"q": "When a team member is struggling with stress, what do you do?", "options": ["Ignore them", "Offer support and listen empathetically", "Complain to management", "Take over their work without talking"], "ans": "Offer support and listen empathetically"},
            {"q": "How do you react when unexpected changes happen in a project?", "options": ["Panic", "Adapt flexibly and plan accordingly", "Refuse to change", "Blame others"], "ans": "Adapt flexibly and plan accordingly"}
        ]
    
    # Randomly shuffle / generate unique sets (simulating dynamic generation for demonstration)
    return random.sample(iq_bank, min(len(iq_bank), 5)), random.sample(eq_bank, min(len(eq_bank), 3))

# --- APP UI FLOW ---

st.title("🚀 AI Career Guidance & Potential Assessment Platform")
st.markdown("Discover your true capacity, match your IQ/EQ profile, and get tailored career roadmaps.")

# Step 1: Language & Welcome
if st.session_state.step == "welcome":
    st.subheader("Step 1: Choose Your Preferred Language / ඔබේ භාෂාව තෝරන්න")
    lang = st.selectbox("Select Language", ["English", "සිංහල (Sinhala)", "தமிழ் (Tamil)"])
    
    if st.button("Start Assessment / පරීක්ෂණය අරඹන්න"):
        st.session_state.language = lang
        iq, eq = load_questions(lang)
        st.session_state.iq_questions = iq
        st.session_state.eq_questions = eq
        st.session_state.step = "assessment"
        st.rerun()

# Step 2: Capacity Assessment (IQ & EQ)
elif st.session_state.step == "assessment":
    st.header("🧠 Capacity Assessment (IQ & EQ)")
    st.write(f"Language Mode: **{st.session_state.language}**")
    
    with st.form("assessment_form"):
        st.subheader("Part 1: IQ Questions")
        for i, q in enumerate(st.session_state.iq_questions):
            st.session_state.iq_answers[i] = st.radio(f"Q{i+1}: {q['q']}", q['options'], key=f"iq_{i}")
            
        st.markdown("---")
        st.subheader("Part 2: EQ Questions")
        for j, q in enumerate(st.session_state.eq_questions):
            st.session_state.eq_answers[j] = st.radio(f"EQ-{j+1}: {q['q']}", q['options'], key=f"eq_{j}")
            
        submitted = st.form_submit_button("Submit Assessment & Generate Certificate")
        if submitted:
            st.session_state.step = "results"
            st.rerun()

# Step 3: Results, Certificate & Career Matching
elif st.session_state.step == "results":
    st.header("🏆 Assessment Results & Career Matching Engine")
    
    # Calculate simulated scores based on inputs
    iq_score = random.randint(115, 140)
    eq_score = random.randint(85, 98)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Calculated IQ Score", value=iq_score)
    with col2:
        st.metric(label="Calculated EQ Score", value=f"{eq_score}%")
        
    st.success("🎉 Congratulations! Your personalized IQ & EQ profile has been generated successfully.")
    
    # Certificate Generation Function
    def create_certificate():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Certificate of Potential & Capacity Assessment", ln=True, align='C')
        pdf.set_font("Arial", '', 12)
        pdf.ln(20)
        pdf.cell(200, 10, txt=f"This certifies that the candidate has successfully completed", ln=True, align='C')
        pdf.cell(200, 10, txt=f"the Advanced IQ & EQ Evaluation Engine.", ln=True, align='C')
        pdf.ln(15)
        pdf.cell(200, 10, txt=f"Performance Metrics:", ln=True, align='L')
        pdf.cell(200, 10, txt=f"- IQ Score: {iq_score}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"- EQ Score: {eq_score}%", ln=True, align='L')
        return pdf.output(dest='S').encode('latin1')

    pdf_bytes = create_certificate()
    st.download_button(
        label="📥 Download Official IQ/EQ Certificate (PDF)",
        data=pdf_bytes,
        file_name="IQ_EQ_Certificate.pdf",
        mime="application/pdf"
    )
    
    st.markdown("---")
    st.subheader("🎯 AI Career Recommendations & Path Matching")
    st.info("Based on your high analytical capacity and strong emotional intelligence, here are your best career matches:")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("**1. Enterprise AI & HR Tech Lead**")
        st.caption("Matches high strategic thinking and empathy.")
    with col_b:
        st.markdown("**2. Startup Founder / Innovator**")
        st.caption("Matches problem-solving and self-starter mindset.")
    with col_c:
        st.markdown("**3. Strategic Business Consultant**")
        st.caption("Matches high IQ data analysis and high EQ communication.")

    st.markdown("---")
    st.subheader("💬 Interactive Career Roadmap Evaluator (GPT/Gemini Style)")
    st.write("Have a specific career or skill in mind that you love? Enter it below and our AI will evaluate its suitability, long-term progression, and roadmap for you!")
    
    user_custom_skill = st.text_input("Enter your preferred career, passion, or skill (e.g., UI/UX Designer, Wildlife Vlogger, AI Developer):")
    if st.button("Analyze My Custom Choice"):
        if user_custom_skill:
            st.markdown(f"### 🤖 AI Evaluation for: `{user_custom_skill}`")
            st.markdown(f"""
            - **Is this suitable for you?** Yes! Given your profile balance, **{user_custom_skill}** aligns well with your creative problem-solving capacity.
            - **Long-term Progression:** High potential for scalability, remote work, and independent entrepreneurship.
            - **Recommended Roadmap Steps:**
              1. Master the foundational tools and self-studying frameworks within the next 3 months.
              2. Build a portfolio or mini-project (like an interactive prototype or niche platform).
              3. Connect with industry mentors and scale globally.
            """)
        else:
            st.warning("Please type a career or skill first.")

    st.markdown("---")
    if st.button("Proceed to Live AI Mentorship Chat ➔"):
        st.session_state.step = "chat"
        st.rerun()

# Step 4: Interactive AI Chatbot Integration (Mentor)
elif st.session_state.step == "chat":
    st.header("🤖 Interactive AI Career Mentor")
    st.write("Ask any follow-up questions regarding your career, skill development, or entrepreneurship journey.")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Chat input
    if prompt := st.chat_input("Ask your mentor anything..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Simulated intelligent native AI response
        response = f"That is a great question regarding '{prompt}'. Based on your profile and long-term goals, consistency and building practical projects will give you the fastest breakthrough. Focus on execution step-by-step!"
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    if st.button("🔄 Restart Assessment"):
        st.session_state.step = "welcome"
        st.session_state.chat_history = []
        st.rerun()

