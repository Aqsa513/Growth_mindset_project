import streamlit as st
import random
import time

# Growth Mindset Quotes
quotes = [
    "🌟 Failure is an opportunity to grow.",
    "📚 I can learn anything I want to.",
    "🏆 Challenges help me grow.",
    "💡 My effort and attitude determine my abilities.",
    "📝 Feedback is constructive and helps me improve.",
    "🚀 I am inspired by the success of others.",
    "❌ Mistakes help me learn.",
]

st.set_page_config(page_title="Growth Mindset App", page_icon="🌱", layout="centered")

# Enhanced Heading
st.markdown("""
    <h1 style='text-align: center; color: #900C3F;'>🌱⭐   Growth Mindset  AI ⭐ 🌱</h1>
    <h3 style='text-align: center; color: #000000;'>Unlock Your Full Potential Through Learning and Perseverance. ❤️</h3>
""", unsafe_allow_html=True)

st.write("### Get inspired with motivational quotes and track your growth mindset journey! 🌟")

# Sidebar for user input
st.sidebar.header("📝 User Progress Tracker")
name = st.sidebar.text_input("👤 Enter your name:")
progress = st.sidebar.slider("📊 Rate your growth mindset today (1-10):", 1, 10, 5)
submit = st.sidebar.button("💾 Save Progress")

if submit:
    st.sidebar.success(f"✅ Progress saved for {name} with rating {progress}/10!")
    time.sleep(1)

# Main section for quotes
def get_random_quote():
    return random.choice(quotes)

st.write("### 🎯 Click the button below to get a motivational quote!")
if st.button("✨ Get Quote"):
    with st.spinner("🔄 Fetching a powerful quote..."):
        time.sleep(1)
        st.success(get_random_quote())

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: #777;'>🌟 Developed with passion to inspire growth | © 2025 Growth Mindset App 🌟</p>
""", unsafe_allow_html=True)
st.write("** ❤️ created by Aqsa Ahmed **")