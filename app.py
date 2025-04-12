# app.py
from flask import Flask, request, render_template
from scraper import extract_text_from_url
from gem_api import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        url = request.form['url']
        try:
            page_text = extract_text_from_url(url)
            summary = summarize_text(page_text)
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
