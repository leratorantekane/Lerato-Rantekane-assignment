import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
import pdfplumber
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Job Assistant", page_icon="💼")

# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp{ background-color: #C7A07A; }

h1, h2, h3 {
    color: #734128 !important;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #734128;
    font-size: 18px;
    margin-bottom: 20px;
    display: block;
}

/* Buttons */
.stButton>button {
    background-color: #734128;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 20px;
}

/* Inputs */
.stTextArea textarea { border-radius: 20px; }

label {
    color: #734128 !important;
    font-weight: 600;
}

/* Cards */
.card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Chat bubbles */
.user-bubble {
    background-color: #734128;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    text-align: right;
}

.ai-bubble {
    background-color: #fff8f2;
    color: #734128;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    text-align: left;
}

.output-box {
    background-color: #fff8f2;
    color: #734128 !important;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e6c7a8;
}
</style>
""", unsafe_allow_html=True)

# ---------------- ENV + MODE ----------------
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Toggle this:
TEST_MODE = True   # True = mock data, False = real API

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

# ---------------- HEADER ----------------
st.markdown("""
<div class="section">
    <h1>💼 Lerato's AI Job Assistant</h1>
    <p class="subtitle">
        Generate professional cover letters using AI & ask questions regarding your application.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📄 Upload & Job Details")

uploaded_resume = st.file_uploader("Please upload your CV in PDF format.", type="pdf")

# Extract text from PDF
def extract_text_from_pdf(file):
    text = ""

    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        text = ""
        
        # 🔥 Fallback if extraction is poor
    if len(text.strip()) < 100:
         text = """
Candidate with experience in relevant technical and professional fields.
Skilled in problem solving, teamwork, and delivering results.
Has worked on projects and gained practical exposure in their domain.
"""
    return text

job_description = st.text_area("Please paste the applied job description.")
st.markdown('</div>', unsafe_allow_html=True)

def extract_name(resume_text):
    lines = resume_text.split("\n")
    if lines:
        return lines[0].strip()
    return "Candidate"

# Extract resume text
resume = ""
if uploaded_resume:
    resume = extract_text_from_pdf(uploaded_resume)
    candidate_name = extract_name(resume)
    # st.write("DEBUG RESUME:", resume[:1000])

# ---------------- GENERATE BUTTON ----------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("Generate Cover Letter")

# ---------------- COVER LETTER LOGIC ----------------
if generate:
    if resume and job_description:

        # -------- MOCK MODE --------
        if TEST_MODE:
            clean_resume = " ".join(resume.split())

            st.session_state.cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for this role. Based on my background and experience, I believe I am a strong fit.

From my resume, I bring relevant experience such as:
{clean_resume[:1000]}...

This aligns well with your job requirements:
{job_description[:1000]}...

I am confident that my skills and experience will allow me to contribute meaningfully to your team.

Kind regards,  
Candidate
"""

        # -------- REAL API MODE --------
        else:
            try:
                client = OpenAI(api_key=openai_api_key)

                prompt = f"""
Write a professional cover letter.

Resume:
{resume}

Job:
{job_description}
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You help write professional cover letters."},
                        {"role": "user", "content": prompt}
                    ]
                )

                st.session_state.cover_letter = response.choices[0].message.content

            except Exception as e:
                st.error(f"API Error: {str(e)}")

    else:
        st.error("Please upload both your CV and the job description.")

# ---------------- DISPLAY COVER LETTER ----------------
if st.session_state.cover_letter:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### ✨ Cover Letter")
    st.markdown(f"<div class='output-box'>{st.session_state.cover_letter}</div>", unsafe_allow_html=True)

    # Create PDF
    def create_pdf(text):
        file_path = "cover_letter.pdf"
        doc = SimpleDocTemplate(file_path)
        styles = getSampleStyleSheet()
        content = [Paragraph(text, styles["Normal"])]
        doc.build(content)
        return file_path

    pdf_file = create_pdf(st.session_state.cover_letter)

    with open(pdf_file, "rb") as f:
        st.download_button("📄 Download as PDF", f, file_name="cover_letter.pdf")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CHATBOT ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🤖 Ask Your AI Career Assistant")

# ---------------- SESSION STATE FIX ----------------
# Prevent duplicate inputs
if "last_input" not in st.session_state:
    st.session_state.last_input = ""

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.session_state.last_input = ""

# Input box
user_input = st.text_input("Ask a question about your application...")

# ---------------- CHAT LOGIC ----------------
if user_input and user_input != st.session_state.last_input:

    # Save last processed input
    st.session_state.last_input = user_input

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Context for AI
    context = f"""
Resume:
{resume}

Job:
{job_description}
"""

    # ---------------- RESPONSE GENERATION ----------------
    with st.spinner("Thinking..."):

        # -------- MOCK CHAT --------
        if TEST_MODE:
            user_text = user_input.lower()

            if "skills" in user_text:
                reply = f"Based on your CV, your key strengths include Python, SQL, and data visualization. These align well with the job requirements."

            elif "qualify" in user_text:
                reply = f"You appear to meet several important requirements, especially in data analysis and dashboarding. Highlight your projects to strengthen your application."

            elif "experience" in user_text:
                reply = f"Your experience as a Data Intern and your projects demonstrate practical exposure. Focus on measurable results and impact."

            elif "improve" in user_text or "better" in user_text:
                reply = f"You can improve your CV by adding quantified achievements, clearer formatting, and tailoring it more closely to the job description."

            else:
                reply = f"Based on your CV and the job description, you are a strong candidate. Continue refining how you present your experience."

        # -------- REAL API CHAT --------
        else:
            try:
                client = OpenAI(api_key=openai_api_key)

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are a helpful AI career assistant.\n{context}"
                        }
                    ] + st.session_state.messages
                )

                reply = response.choices[0].message.content

            except Exception as e:
                reply = f"API Error: {str(e)}"

    # Store AI response
    st.session_state.messages.append({"role": "assistant", "content": reply})

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-bubble'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)