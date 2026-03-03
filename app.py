import streamlit as st
import os
import yt_dlp
from dotenv import load_dotenv
from google import genai

# --- 1. SETUP ---
load_dotenv()
st.set_page_config(page_title="Academic Scribe", page_icon="🎓", layout="wide")
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

STUDY_PROMPT = """
You are an Elite Academic Tutor. Transform this lecture into high-yield study notes.
Structure:
1. 📌 **Executive Summary**: A high-level overview.
2. 🔑 **Key Terminology**: Bold terms with concise definitions.
3. 📝 **Cornell Notes**: Detailed hierarchy with bullet points.
4. 🚀 **Exam-Day Essentials**: 3 likely exam questions and answers.
5. 📊 **Conceptual Blueprint**: A structured explanation of how the main ideas connect.
"""

def download_lecture(url):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': 'lecture_temp.m4a',
        'overwrites': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "lecture_temp.m4a"

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

# --- 2. UI STYLING ---
st.markdown("""
    <style>
    .stApp { background: #0b0e14; color: #eef2f6; }
    .header-text {
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 3.5rem; font-weight: 800; text-align: center;
    }
    .notes-card {
        background: #161b22; border: 1px solid #30363d;
        border-radius: 12px; padding: 2.5rem; line-height: 1.6;
    }
    .video-preview {
        border-radius: 15px; border: 2px solid #38BDF8;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="header-text">Academic Scribe 🎓</h1>', unsafe_allow_html=True)

# --- 3. INPUT SECTION ---
col_in, col_pre = st.columns([2, 1])

with col_in:
    url = st.text_input("Lecture URL", placeholder="Paste YouTube link here...")
    process_button = st.button("✨ Make Notes ")

with col_pre:
    if url:
        v_id = get_video_id(url)
        if v_id:
            # Displaying the Video Thumbnail
            st.image(f"https://img.youtube.com/vi/{v_id}/maxresdefault.jpg", 
                     caption="Video Preview", use_container_width=True)

# --- 4. GENERATION LOGIC ---
if process_button:
    if url:
        file_path = None
        with st.spinner("Analyzing lecture material and drafting notes..."):
            try:
                file_path = download_lecture(url)
                
                with open(file_path, "rb") as f:
                    file_upload = client.files.upload(file=f, config={'mime_type': 'audio/mp4'})
                
                # Hidden model priority list
                for model_name in ["gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.0-flash"]:
                    try:
                        response = client.models.generate_content(
                            model=model_name, 
                            contents=[file_upload, STUDY_PROMPT]
                        )
                        st.session_state.notes = response.text
                        break 
                    except:
                        continue 

            except Exception:
                st.error("Processing failed. Please try again in a moment.")
            
            finally:
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)
    else:
        st.warning("Please provide a lecture link.")

st.divider()

# --- 5. DISPLAY ---
if "notes" in st.session_state:
    st.markdown("###  Your Study Guide")
    
    # Quick reminder of the Cornell System for active recall
    
    
    st.markdown(f'<div class="notes-card">{st.session_state.notes}</div>', unsafe_allow_html=True)
    st.write("")
    st.download_button("📥 Save Notes as Markdown", st.session_state.notes, file_name="Study_Notes.md")