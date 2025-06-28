from handlers.summarizer import summarize_email
from handlers.reply_generator import generate_reply
from handlers.translator import translate_to_arabic
import langdetect

# Helper to check if the email is Arabic
def is_arabic(text):
    try:
        return langdetect.detect(text) == 'ar'
    except:
        return False

# Load email from file
with open("data/sample_emails.txt", "r", encoding="utf-8") as f:
    email_text = f.read().strip()

print("\n📩 Original Email:\n", email_text)

if is_arabic(email_text):
    print("\n🌐 Detected Language: Arabic")
    summary = summarize_email(email_text, language="ar")
    reply = generate_reply(email_text, language="ar")
    print("\n🧠 Summary (Arabic):\n", summary)
    print("\n✉️ Suggested Reply (Arabic):\n", reply)
else:
    print("\n🌐 Detected Language: Non-Arabic")
    summary = summarize_email(email_text, language="en")
    reply = generate_reply(email_text, language="en")
    translated_reply = translate_to_arabic(reply)
    print("\n🧠 Summary (English):\n", summary)
    print("\n✉️ Suggested Reply (English):\n", reply)
    print("\n✉️ Suggested Reply (Arabic Translation):\n", translated_reply)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))