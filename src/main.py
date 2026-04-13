"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from textwrap import wrap

from src.recommender import load_songs, recommend_songs


def print_recommendations_table(recommendations) -> None:
    title_width = 20
    artist_width = 16
    score_width = 7
    reasons_width = 58

    def row_line() -> str:
        return (
            "+"
            + "-" * (title_width + 2)
            + "+"
            + "-" * (artist_width + 2)
            + "+"
            + "-" * (score_width + 2)
            + "+"
            + "-" * (reasons_width + 2)
            + "+"
        )

    print(row_line())
    print(
        f"| {'Title':<{title_width}} | {'Artist':<{artist_width}} | {'Score':>{score_width}} | {'Reasons':<{reasons_width}} |"
    )
    print(row_line())

    for song, score, explanation in recommendations:
        wrapped_reasons = wrap(explanation, width=reasons_width) or [""]
        print(
            f"| {song['title']:<{title_width}} | {song['artist']:<{artist_width}} | {score:>{score_width}.2f} | {wrapped_reasons[0]:<{reasons_width}} |"
        )
        for extra_line in wrapped_reasons[1:]:
            print(
                f"| {'':<{title_width}} | {'':<{artist_width}} | {'':>{score_width}} | {extra_line:<{reasons_width}} |"
            )
        print(row_line())


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    high_energy_pop_profile = {
        "genre": "pop",
        "mood": "energetic",
        "energy": 0.9,
        "target_popularity": 85,
        "release_decade": "2020s",
        "target_danceability": 0.85,
        "target_acousticness": 0.20,
        "mood_tag": "euphoric",
    }
    chill_lofi_profile = {
        "genre": "lofi",
        "mood": "calm",
        "energy": 0.3,
        "target_popularity": 70,
        "release_decade": "2010s",
        "target_danceability": 0.55,
        "target_acousticness": 0.80,
        "mood_tag": "dreamy",
    }
    deep_intense_rock_profile = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.85,
        "target_popularity": 78,
        "release_decade": "2000s",
        "target_danceability": 0.60,
        "target_acousticness": 0.25,
        "mood_tag": "aggressive",
    }

    user_prefs = deep_intense_rock_profile
    # {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    print_recommendations_table(recommendations)


if __name__ == "__main__":
    main()
