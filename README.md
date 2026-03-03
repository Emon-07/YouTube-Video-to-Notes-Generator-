# Academic Scribe  
### AI-Powered YouTube Lecture to High-Yield Study Notes Generator

Academic Scribe transforms YouTube lectures into structured, exam-ready study notes using advanced AI and an optimized academic prompting framework.

Paste a lecture link.  
Get an executive summary, key terms, Cornell notes, and exam-focused insights instantly.

---

## What It Does

Academic Scribe:

- Downloads lecture audio from YouTube  
- Processes content using advanced AI models  
- Generates an Executive Summary  
- Extracts Key Terminology  
- Creates Cornell Notes structure  
- Predicts likely exam questions  
- Builds a conceptual understanding blueprint  
- Allows Markdown download for revision  

---

## Tech Stack

- Python  
- Streamlit  
- yt-dlp  
- Generative AI  
- python-dotenv  

---

## Project Structure

```
Academic-Scribe/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/Emon-07/YouTube-Video-to-Notes-Generator-.git
cd YouTube-Video-to-Notes-Generator-
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## How It Works

1. User pastes a YouTube URL  
2. App extracts lecture audio using `yt-dlp`  
3. Audio is processed by an AI model  
4. Structured academic notes are generated  
5. Notes are displayed and can be downloaded  

---

## Future Improvements

- PDF export option  
- Multi-language support  
- Transcript fallback mode  
- Model selection toggle  
- User authentication and saved history  

---

## Author

Eman Chakraborty

---

## License

This project is open-source and available under the MIT License.
