from dotenv import load_dotenv
import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------- LOAD ENV ---------------- #
import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="MoneyMate AI",
    page_icon="💰",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* App Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
    color: white;
}

/* Main Container */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d1d5db;
    margin-bottom: 30px;
}

/* Text */
html, body, p, li, span, label, div {
    color: white !important;
}

/* Input Box */
.stTextInput input {
    background-color: #f8fafc !important;
    color: black !important;
    border-radius: 12px !important;
    padding: 14px !important;
    font-size: 17px !important;
    border: none !important;
}

/* Button */
.stButton button {
    background: linear-gradient(
        90deg,
        #38bdf8,
        #0ea5e9
    ) !important;

    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 10px 24px !important;
}

.stButton button:hover {
    opacity: 0.9;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 15px;
    margin-top: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Expander */
.streamlit-expanderHeader {
    color: white !important;
    font-weight: bold !important;
    font-size: 18px !important;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 30px;
    color: #cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown(
    "<div class='main-title'>💰 MoneyMate AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Smart Personal Finance Assistant</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:

    st.title("💰 MoneyMate AI")

    st.markdown("---")

    st.subheader("📌 What It Helps With")

    st.write("""
    • Budget planning  
    • Saving money  
    • Investment basics  
    • Emergency funds  
    • Debt management  
    • Expense tracking  
    • Financial habits  
    """)

    st.markdown("---")


# ---------------- EXAMPLE QUESTIONS ---------------- #
with st.expander("💡 Example Questions"):

    st.write("""
    • How should I divide my monthly salary?  
    • Explain SIP investment in simple words  
    • How much emergency fund should I keep?  
    • Tips to save money faster  
    """)

# ---------------- PROMPT ---------------- #
template = """
You are MoneyMate AI,
an expert Personal Finance Advisor with deep knowledge of:

- Budget planning
- Savings
- Investments
- Mutual funds
- SIPs
- Debt management
- Financial discipline
- Emergency funds
- Personal wealth growth

Your job is to explain finance concepts
in very simple beginner-friendly language.

Instructions:

- Give practical financial advice.
- Explain concepts clearly and simply.
- Use examples whenever possible.
- Suggest budgeting and saving strategies.
- Encourage responsible financial habits.
- Use headings and bullet points.
- Keep responses motivating and easy to understand.
- Avoid overly technical financial jargon.
- If investment risk exists, mention it clearly.
- Never guarantee profits or unrealistic returns.

Question:
{query}
"""

prompt = ChatPromptTemplate.from_template(template)

# ---------------- MODEL ---------------- #
llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.6
    )


# ---------------- CHAIN ---------------- #
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt | llm | parser

# ---------------- USER INPUT ---------------- #
user_input = st.text_input(
    "Ask anything about money, savings, investments, or budgeting:",
    placeholder="Example: How can I save money every month?"
)

# ---------------- RESPONSE ---------------- #
if st.button("Get Advice"):

    if user_input.strip() == "":
        st.warning("Please enter a finance-related question.")

    else:

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Analyzing your finance query..."):

            response = chain.invoke({
                "query": user_input
            })

        with st.chat_message("assistant"):
            st.markdown(response)

# ---------------- FOOTER ---------------- #
st.markdown(
    """
    <div class='footer'>
        💰 MoneyMate AI • Your Personal Finance Guide
    </div>
    """,
    unsafe_allow_html=True
)
