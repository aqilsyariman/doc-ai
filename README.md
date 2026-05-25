# PDF Question Answering Chatbot

A RAG (Retrieval-Augmented Generation) system that allows you to ask questions about any PDF document and get accurate AI-powered answers.

## What It Does

Upload any PDF file and ask questions about its content. The system reads the document, understands the meaning of each section, and returns precise answers based only on the information inside the PDF.

**Example:**
```
Question: "What is ICMP?"
Answer: "ICMP stands for Internet Control Message Protocol. It handles error and control messages in IP networks..."
```

## How It Works

```
PDF → Validate → Read → Split into chunks → Convert to vectors → Store in ChromaDB → Search by question → AI answers
```

1. Validates the file is a PDF
2. Extracts all text from every page
3. Splits text into 500-character chunks
4. Converts chunks into vectors using Sentence Transformers
5. Stores vectors in ChromaDB
6. Converts user question into a vector
7. Finds the most relevant chunks
8. Sends relevant chunks to AI to generate a clear answer

## Tech Stack

- **Python** - Core language
- **PyPDF2** - PDF text extraction
- **Sentence Transformers** - Text to vector conversion
- **ChromaDB** - Vector database storage and search
- **LangChain** - AI model integration
- **Groq API** - Free AI inference (LLaMA 3.1)

## Installation

### Prerequisites
- Python 3.10+
- VSCode
- Mac or Windows

### Step 1 — Clone the repository
```bash
git clone https://github.com/aqilsyariman/pdf-chatbot.git
cd pdf-chatbot
```

### Step 2 — Install dependencies
```bash
pip3 install PyPDF2 sentence-transformers chromadb langchain langchain-groq
```

### Step 3 — Get a free Groq API key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Create an API key

### Step 4 — Set your API key
```bash
export GROQ_API_KEY="your-api-key-here"
```

### Step 5 — Add your PDF
Place your PDF file in the project folder and update this line in `chatbot.py`:
```python
result = validate_files(["your-file.pdf"])
```

### Step 6 — Ask your question
Update this line with your question:
```python
results = search("Your question here?", collection)
final_answer = get_answer("Your question here?", results)
```

### Step 7 — Run
```bash
python3 chatbot.py
```

## Project Structure

```
pdf-chatbot/
│
├── chatbot.py          # Main application
└── README.md           # Documentation
```

## Built By

Aqil Syariman — AI Engineer in progress 🔥
