from flask import Blueprint, render_template, redirect, url_for, session
from flask_dance.contrib.google import google
from .langchain_core import summarize_and_reply

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("login.html")

@bp.route("/home")
def home():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    email = resp.json()["email"]
    session["email"] = email
    return render_template("index.html", user=email)

@bp.route("/generate", methods=["POST"])
def generate():
    from flask import request
    email_text = request.form.get("email_text")
    summary, reply, translated_reply = summarize_and_reply(email_text)
    return render_template("index.html", summary=summary, reply=reply, translated=translated_reply, user=session["email"])
