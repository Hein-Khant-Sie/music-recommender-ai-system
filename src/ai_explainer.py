import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

_client = None


def _get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return None
        _client = genai.Client(api_key=api_key)
    return _client


def explain_reason(reason_text: str) -> str:
    client = _get_client()
    if client is None:
        return "This song matches your preferences well in mood and style."

    prompt = (
        "Rewrite this explanation into ONE short, natural sentence.\n\n"
        f"{reason_text}\n\n"
        "Rules:\n"
        "- Only output ONE sentence\n"
        "- Do NOT give multiple options\n"
        "- Do NOT include numbers or technical terms\n"
        "- Keep it simple and natural\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        result = response.text.strip()

        # 🔧 Fix messy multi-option responses
        if "option" in result.lower() or "*" in result:
            lines = [line.strip() for line in result.split("\n") if line.strip()]
            result = lines[-1]

        return result

    except Exception:
        return "This song matches your preferences well in mood and style."