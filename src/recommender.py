from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


ARTIST_DIVERSITY_PENALTY = 0.35


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                    "popularity": int(row["popularity"]),
                    "release_decade": row["release_decade"],
                    "mood_tag": row["mood_tag"],
                }
            )

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a song's recommendation score and explanation reasons from user preferences."""
    score = 0.0
    explanation_parts: List[str] = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 1.0
        explanation_parts.append("genre match (+1.0)")

    if song.get("mood") == user_prefs.get("mood"):
        score += 2.0
        explanation_parts.append("mood match (+2.0)")

    energy_similarity = 1 - \
        abs(song.get("energy", 0.0) - user_prefs.get("energy", 0.0))
    weighted_energy = 1.0 * energy_similarity
    score += weighted_energy
    explanation_parts.append(f"energy similarity (+{weighted_energy:.2f})")

    popularity_similarity = 1 - abs(
        song.get("popularity", 0) - user_prefs.get("target_popularity", 50)
    ) / 100
    weighted_popularity = max(0.0, popularity_similarity)
    score += weighted_popularity
    explanation_parts.append(
        f"popularity similarity (+{weighted_popularity:.2f})")

    if song.get("release_decade") == user_prefs.get("release_decade"):
        score += 0.8
        explanation_parts.append("release decade match (+0.8)")

    danceability_similarity = 1 - abs(
        song.get("danceability", 0.0) -
        user_prefs.get("target_danceability", 0.5)
    )
    weighted_danceability = max(0.0, danceability_similarity)
    score += weighted_danceability
    explanation_parts.append(
        f"danceability similarity (+{weighted_danceability:.2f})")

    acousticness_similarity = 1 - abs(
        song.get("acousticness", 0.0) -
        user_prefs.get("target_acousticness", 0.5)
    )
    weighted_acousticness = max(0.0, acousticness_similarity)
    score += weighted_acousticness
    explanation_parts.append(
        f"acousticness similarity (+{weighted_acousticness:.2f})")

    if song.get("mood_tag") == user_prefs.get("mood_tag"):
        score += 1.2
        explanation_parts.append("mood tag match (+1.2)")

    return score, explanation_parts


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k with score explanations."""
    results: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, explanation_parts = score_song(user_prefs, song)
        explanation = ", ".join(explanation_parts)
        results.append((song, score, explanation))

    selected_results: List[Tuple[Dict, float, str]] = []
    artist_counts: Dict[str, int] = {}
    remaining = results.copy()

    while remaining and len(selected_results) < k:
        best_index = 0
        best_adjusted_score = None

        for index, (song, base_score, _) in enumerate(remaining):
            artist = song.get("artist", "")
            repeats = artist_counts.get(artist, 0)
            adjusted_score = base_score - (ARTIST_DIVERSITY_PENALTY * repeats)

            if best_adjusted_score is None or adjusted_score > best_adjusted_score:
                best_adjusted_score = adjusted_score
                best_index = index

        song, base_score, explanation = remaining.pop(best_index)
        artist = song.get("artist", "")
        repeats = artist_counts.get(artist, 0)
        penalty_value = ARTIST_DIVERSITY_PENALTY * repeats
        final_score = base_score - penalty_value

        if penalty_value > 0:
            explanation = f"{explanation}, artist diversity penalty (-{penalty_value:.2f})"

        selected_results.append((song, final_score, explanation))
        artist_counts[artist] = repeats + 1

    return selected_results
