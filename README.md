# AI Web Scraping & Copy Analyzer Tool

## 🧠 What It Does
- Scrapes visible text from any webpage.
- Sends it to Gemini AI to get a 3-point summary.
- Displays results in a clean web UI.

## 🔧 How to Run

1. Clone the repo.
2. Create `.env` with your `GEMINI_API_KEY`.
3. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Run the app:
    ```
    python app.py
    ```

## 🔐 API Used
- Google Gemini Pro via `google-generativeai` SDK.
