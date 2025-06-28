from flask import Flask, render_template, request
from handlers.summarizer import summarize_email
from handlers.translator import translate_to_arabic
from langdetect import detect
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def suggest_reply(summary, language="en"):
    return f"Thank you for your message. Here's a quick summary of your concern: \"{summary}\". We are reviewing your request and will respond shortly."

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    reply = ""
    original_email = ""

    if request.method == "POST":
        original_email = request.form.get("email", "").strip()
        action = request.form.get("action")

        if original_email:
            try:
                lang = detect(original_email)
                summary = summarize_email(original_email, language=lang)

                if lang != "ar":
                    summary_translated = translate_to_arabic(summary)
                else:
                    summary_translated = summary

                if action == "reply":
                    reply = suggest_reply(summary_translated, language=lang)

                summary = summary_translated

            except Exception as e:
                summary = f"❌ Error: {str(e)}"

    return render_template("index.html", summary=summary, original_email=original_email, reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
