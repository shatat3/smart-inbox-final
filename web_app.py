from flask import Flask, render_template, request
from handlers.summarizer import summarize_email
from handlers.reply_generator import generate_reply
from utils.email_drafter import save_draft

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    reply = ""
    translated_reply = ""

    if request.method == "POST":
        email = request.form["email"]
        recipient = request.form["recipient"]
        subject = request.form["subject"]

        summary = summarize_email(email)
        reply = generate_reply(email)

        # Optional: translate reply to Arabic if needed
        # from handlers.translator import translate_to_arabic
        # translated_reply = translate_to_arabic(reply)

        # Save as draft
        save_draft(to_email=recipient, subject=subject, body=reply)

    return render_template("index.html", summary=summary, reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
