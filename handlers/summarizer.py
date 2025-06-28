from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import OPENAI_API_KEY

def summarize_email(email_text, language="en"):
    prompt_text = (
        "لخص هذا البريد الإلكتروني:\n\n{email}"
        if language == "ar" else
        "Summarize this email:\n\n{email}"
    )
    prompt = ChatPromptTemplate.from_template(prompt_text)
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
    chain = prompt | llm
    response = chain.invoke({"email": email_text})
    return response.content.strip()


