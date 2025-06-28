from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from config import OPENAI_API_KEY
import re

def is_arabic(text):
    return re.search(r'[\u0600-\u06FF]', text) is not None

def translate_to_arabic(text):
    # Dummy fallback (replace with DeepL or Google Translate API if needed)
    return f"[ARABIC TRANSLATION]: {text}"

def summarize_and_reply(email_text):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
    
    summary_prompt = ChatPromptTemplate.from_template("Summarize this email:\n\n{email}")
    reply_prompt = ChatPromptTemplate.from_template("Write a polite reply to this email:\n\n{email}")

    summary_chain: Runnable = summary_prompt | llm
    reply_chain: Runnable = reply_prompt | llm

    summary = summary_chain.invoke({"email": email_text}).content.strip()
    reply = reply_chain.invoke({"email": email_text}).content.strip()

    if is_arabic(email_text):
        return summary, reply, translate_to_arabic(reply)
    else:
        translated_reply = translate_to_arabic(reply)
        return summary, reply, translated_reply
