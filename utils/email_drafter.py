import yagmail
import os

def save_draft(to_email, subject, body):
    sender_email = os.getenv("GMAIL_SENDER")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    try:
        yag = yagmail.SMTP(user=sender_email, password=app_password)
        yag.send(to=to_email, subject=subject, contents=body)
        print("✅ Reply saved as a draft.")
    except Exception as e:
        print("❌ Failed to save draft:", e)
