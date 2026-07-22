# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

  Each Song uses features such as genre, mood, energy, tempo, valence, danceability, and acousticness to compare songs by their musical characteristics. 

- What information does your `UserProfile` store

  The UserProfile stores the user’s preferred genre, preferred mood, target energy level, and whether they tend to like acoustic songs.

- How does your `Recommender` compute a score for each song

  The Recommender computes a score for each song by giving points for matching these preferences, with closer matches in numerical features like energy receiving higher scores.

- How do you choose which songs to recommend

   Songs with the highest overall scores get recommended, ranking them from best match to weakest match.

- Finalized "Algorithm Recipe" and a brief note on any potential biases you expect.

  My finalized Algorithm Recipe is a simple content-based scoring system. For each song, I give +2.0 points if the genre matches the user’s favorite genre, +1.0 points if the mood matches the user’s favorite mood, and then add similarity points based on how close the song’s energy is to the user’s target energy. I can calculate the energy similarity with a distance-based rule such as 1 - |SongEnergy - TargetEnergy|, so songs with energy values near the user’s preferred level receive higher scores. After scoring all songs, I rank them from highest to lowest and recommend the top results. I expect this recommender to have a few biases. It may over-prioritize genre, since a genre match gives the largest score, and that could cause it to miss songs that are a great mood match but belong to a different genre. It may also favor songs with energy values close to the user’s target, which could make it seem too narrow if the user actually likes a wider range of moods or styles. In a real system, this kind of bias could make recommendations feel repetitive or overly predictable.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loading songs from data/songs.csv...
Loaded 18 songs.

User preferences:
Genre: pop
Mood: happy
Energy target: 0.80

Top 5 recommendations:

1. Sunrise City - Score: 3.98
   Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)

2. Gym Hero - Score: 2.87
   Because: genre match (+2.0), energy similarity (+0.87)

3. Rooftop Lights - Score: 1.96
   Because: mood match (+1.0), energy similarity (+0.96)

4. Midnight Parade - Score: 0.99
   Because: energy similarity (+0.99)

5. Neon Boulevard - Score: 0.96
   Because: energy similarity (+0.96)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

This section is covered in model_card.md.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This section is covered in model_card.md.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This section is covered in model_card.md.

