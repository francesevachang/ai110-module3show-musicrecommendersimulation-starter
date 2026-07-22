"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

It defines a set of user preference profiles and runs the recommender
against each one. Alongside three "normal" profiles, it includes three
*adversarial* / *edge-case* profiles designed to probe whether the
scoring logic in recommender.py can be tricked or produces surprising
results.

Scoring recap (see recommender.score_song):
    - genre match .............. +2.0   (dominant weight)
    - mood match ............... +1.0
    - energy similarity ........ +(1 - |song.energy - target|)  in [0.0, 1.0]

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# ---------------------------------------------------------------------------
# "Normal" profiles: coherent, realistic listeners.
# ---------------------------------------------------------------------------
NORMAL_PROFILES = [
    {
        "name": "High-Energy Pop",
        "note": "A coherent pop lover who wants upbeat, high-energy tracks.",
        "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9},
    },
    {
        "name": "Chill Lofi",
        "note": "Low-energy background listener; genre, mood and energy all align.",
        "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.2},
    },
    {
        "name": "Deep Intense Rock",
        "note": "Wants driving, high-energy rock; all three signals reinforce.",
        "prefs": {"genre": "rock", "mood": "intense", "energy": 0.85},
    },
]


# ---------------------------------------------------------------------------
# Adversarial / edge-case profiles: each is built to stress a specific
# weakness in the scoring logic. The `probes` field says what to watch for.
# ---------------------------------------------------------------------------
ADVERSARIAL_PROFILES = [
    {
        "name": "Genre Loyalist Trap (genre outweighs everything)",
        "note": "Loves pop, but asks for near-zero energy and an off mood.",
        "prefs": {"genre": "pop", "mood": "intense", "energy": 0.05},
        "probes": "Genre (+2.0) outweighs energy (max +1.0), so a wrong-energy pop song can still beat a perfect-energy non-pop song.",
    },
    {
        "name": "Sad but Hyped (conflicting mood vs. energy)",
        "note": "A melancholy mood paired with high energy — signals that clash.",
        "prefs": {"genre": "indie pop", "mood": "melancholy", "energy": 0.9},
        "probes": "Mood (+1.0) and energy pull opposite ways since sad songs are low-energy, so results may end up incoherent or ruled by genre.",
    },
]


def print_profile_header(name: str, note: str, prefs: dict) -> None:
    print("=" * 70)
    print(f"PROFILE: {name}")
    print(f"  {note}")
    if prefs:
        pref_bits = []
        for key in ("genre", "mood", "energy"):
            if key in prefs:
                value = prefs[key]
                pref_bits.append(
                    f"{key}={value:.2f}" if isinstance(value, float) else f"{key}={value}"
                )
        print(f"  Preferences: {', '.join(pref_bits) if pref_bits else '(none)'}")
    else:
        print("  Preferences: (empty)")
    print("=" * 70)


def run_profile(profile: dict, songs: list, top_k: int = 5) -> None:
    print_profile_header(profile["name"], profile["note"], profile["prefs"])

    if "probes" in profile:
        print(f"  Watching for: {profile['probes']}")

    print(f"\n  Top {top_k} recommendations:\n")

    recommendations = recommend_songs(profile["prefs"], songs, k=top_k)

    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"  {index}. {song['title']} ({song['genre']}/{song['mood']}, "
              f"energy={song['energy']:.2f}) - Score: {score:.2f}")
        print(f"     Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    print("\n\n########## NORMAL PROFILES ##########\n")
    for profile in NORMAL_PROFILES:
        run_profile(profile, songs)

    print("\n\n########## ADVERSARIAL / EDGE-CASE PROFILES ##########\n")
    for profile in ADVERSARIAL_PROFILES:
        run_profile(profile, songs)


if __name__ == "__main__":
    main()
