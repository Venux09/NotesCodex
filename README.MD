# NoteCodex 📚

AI-powered study tool that reads PDFs and generates smart summaries or bullet point notes.

## Features
- 📄 Extract text from any PDF file
- 🤖 AI-generated summaries or bullet point notes
- 📝 Export output as a clean PDF
- 🗄️ Save history to local database
- ⚠️ Error handling for invalid file paths

## Tech Stack
- Python
- Groq API (LLaMA 3.3 70B)
- pdfplumber
- fpdf2
- SQLite

## Project Structure
```
notecodex/
├── main.py            # entry point
├── reader.py          # PDF text extraction
├── ai_engine.py       # Groq API integration
├── pdf_generator.py   # PDF generation
├── storage.py         # SQLite database
├── requirements.txt
└── README.md
```

## Setup & Usage

1. Clone the repo
```bash
git clone https://github.com/venux09/notecodex
cd notecodex
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create `.env` file
```
API=your_groq_api_key_here
```

4. Run
```bash
python main.py
```

5. Enter your PDF path when prompted and choose output type

## Output
- Generated PDF saved as `notes.pdf` in project folder
- Session saved to `notecodex.db` database

## Author
Made by Monu (venux09) — self-taught developer, Age 17
