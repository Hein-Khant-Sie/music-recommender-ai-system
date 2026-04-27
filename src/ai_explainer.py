import os
import re
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


def _dynamic_fallback(reason_text: str) -> str:
    text = reason_text.lower()
    parts = []

    if "mood" in text:
        parts.append("the right mood")
    if "energy" in text:
        parts.append("a matching energy")
    if "danceab" in text:
        parts.append("a rhythm made for moving")
    if "acoustic" in text:
        parts.append("a natural, softer sound")
    if "genre" in text:
        parts.append("a style that suits your taste")

    if not parts:
        parts = ["a feel that lines up with what you enjoy"]

    if len(parts) == 1:
        return f"This track brings {parts[0]} that we think you'll love."
    elif len(parts) == 2:
        return f"This track brings {parts[0]} and {parts[1]} that we think you'll love."
    else:
        joined = ", ".join(parts[:-1]) + f", and {parts[-1]}"
        return f"This track brings {joined} that we think you'll love."


def explain_reason(reason_text: str) -> str:
    client = _get_client()
    if client is None:
        return _dynamic_fallback(reason_text)

    prompt = (
        "You are writing a short music recommendation blurb for a listener.\n"
        "Convert the technical reason below into exactly ONE warm, natural sentence.\n\n"
        f"Reason: {reason_text}\n\n"
        "Rules:\n"
        "- Output ONE sentence only — no options, no alternatives, no bullet points\n"
        "- No numbers, scores, percentages, or technical terms\n"
        "- Sound like a knowledgeable friend casually recommending a song\n"
        "- Reference what makes it a good fit: mood, energy, rhythm, sound texture, or style\n"
        "- Good example: \"This song should hit the right mood and energy, with a familiar rhythm and natural sound that we think you'll love.\"\n"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        result = response.text.strip()

        # Strip markdown bold/italic markers
        result = re.sub(r"[*_]{1,2}", "", result)

        # If multiple lines sneak through, take the first non-empty sentence
        lines = [line.strip() for line in result.splitlines() if line.strip()]
        if lines:
            result = lines[0]

        # If still multiple sentences, keep only the first
        sentences = re.split(r"(?<=[.!?])\s+", result)
        result = sentences[0].strip()

        return result if result else _dynamic_fallback(reason_text)

    except Exception:
        return _dynamic_fallback(reason_text)
