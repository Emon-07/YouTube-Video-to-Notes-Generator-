# 🎓 Academic Scribe  
### AI-Powered YouTube Lecture → High-Yield Study Notes Generator

Academic Scribe transforms YouTube lectures into structured, exam-ready study notes using Google Gemini and an advanced academic prompting framework.

Paste a lecture link.  
Get an executive summary, key terms, Cornell notes, and exam-focused insights — instantly.

---

## 🚀 What It Does

Academic Scribe:

- 📥 Downloads lecture audio from YouTube  
- 🤖 Processes content using Google Gemini  
- 📌 Generates Executive Summary  
- 🔑 Extracts Key Terminology  
- 📝 Creates Cornell Notes structure  
- 🚀 Predicts likely exam questions  
- 📊 Builds conceptual understanding blueprint  
- 📄 Allows Markdown download for revision  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- yt-dlp  
- Google Gemini API  
- python-dotenv  

---

## 📂 Project Structure

```
Academic-Scribe/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Emon-07/YouTube-Video-to-Notes-Generator-.git
cd YouTube-Video-to-Notes-Generator-
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

⚠️ Never commit your `.env` file to GitHub.

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🔐 Environment Variables

| Variable        | Description              |
|----------------|--------------------------|
| GOOGLE_API_KEY | Google Gemini API Key    |

---

## 🧠 How It Works

1. User pastes a YouTube URL  
2. App extracts lecture audio using `yt-dlp`  
3. Audio is uploaded to Google Gemini  
4. Gemini generates structured academic notes  
5. Notes are displayed and can be downloaded  

---

## 🌟 Future Improvements

- PDF export option  
- Multi-language support  
- Transcript fallback mode  
- Model selection toggle  
- User authentication & saved history  

---

## 👨‍💻 Author

Emon Chakraborty

---

## 📜 License

This project is open-source and available under the MIT License.
