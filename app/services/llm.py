from app.config import settings

# --- GROQ ---
def _groq_summarize(text):
    from groq import Groq

    client = Groq(api_key=settings.GROQ_API_KEY)

    res = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "system", "content":
                "You are a sharp news analyst. Based on the given text, generate 3 concise, insightful bullet points. Avoid saying you cannot access the article. Infer intelligently."},
            {"role": "user", "content": text}
        ]
    )

    return res.choices[0].message.content


# --- OPENAI ---
def _openai_summarize(text):
    from openai import OpenAI

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    res = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "system", "content": "Summarize in 3 bullet points."},
            {"role": "user", "content": text}
        ]
    )

    return res.choices[0].message.content


# --- OLLAMA ---
def _ollama_summarize(text):
    import requests

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": settings.MODEL_NAME,
            "prompt": f"Summarize in 3 bullet points:\n{text}",
            "stream": False
        }
    )

    return res.json()["response"]


# --- MAIN FUNCTION ---
def summarize(text):
    provider = settings.LLM_PROVIDER.lower()

    if provider == "groq":
        return _groq_summarize(text)

    elif provider == "openai":
        return _openai_summarize(text)

    elif provider == "ollama":
        return _ollama_summarize(text)

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")