import os
from typing import List, Tuple, Dict

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def explain_recommendations(
    recommendations: List[Tuple[Dict, float, str]]
) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY not set. Skipping AI explanation."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    song_lines = []
    for song, score, explanation in recommendations:
        song_lines.append(
            f"- \"{song['title']}\" by {song['artist']} "
            f"(score: {score:.2f}) — {explanation}"
        )
    songs_text = "\n".join(song_lines)

    prompt = (
        "A music recommender system selected these songs for a user:\n\n"
        f"{songs_text}\n\n"
        "In 2-3 sentences, explain simply why these songs were recommended. "
        "Focus on what they have in common and why they suit the user's taste. "
        "Avoid technical jargon."
    )

    response = model.generate_content(prompt)
    return response.text.strip()
