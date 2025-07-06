# 🤖 Build an AI Agent with Gemini

This is part of the Boot.dev backend development track. The goal is to build a toy version of *Claude Code* using Google's free **Gemini API**.

---

## 🚀 Features

This is a command-line interface (CLI) tool that:

- Accepts a coding-related task (e.g., *"My dictionary isn't returning the keys; help me trace the code"*).
- Sends your prompt to the Gemini API for code-related responses.
- (In future versions) selects from predefined helper functions such as:
  - Scanning files in a directory
  - Reading file contents
  - Overwriting file contents
  - Executing Python files
- Repeats tasks until the job is complete (or fails—yes, that's still possible 😅)

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/tawficFatah/ai-gemini-agent.git

# Navigate into the project directory
cd ai-gemini-agent

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
---


## 🧪 Usage
```bash
python src/main.py "your prompt"
```

To get verbose output (token usage stats):

```bash
python main.py "What are Python's list comprehensions?" --verbose
```
---

## 🔐 Environment Variables
Create a .env file in the project root with the following content:

GEMINI_API_KEY=your_api_key_here

You can get a free Gemini API key from: https://makersuite.google.com/app/apikey

---

## 📂 File Structure
```bash
ai-gemini-agent/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── tests.py                 # For unit tests
```

## ✍️ Author
Tawfic Abdul-Fatah – [GitHub](https://github.com/tawficFatah)

