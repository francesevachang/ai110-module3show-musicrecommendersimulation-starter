# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

TripleTune 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  

    It generates a ranked top-5 list of songs from a small catalog, matched to a user's stated genre, mood, and target energy, each with a plain-language "Because" explanation.

- What assumptions does it make about the user  

    It assumes the user can name a single favorite genre, a single mood, and one target energy level, and that those three preferences fully capture their taste.

- Is this for real users or classroom exploration  

    This is a classroom exploration project for learning how recommender scoring and bias work, not a production system for real listeners.

---

## 3. How the Model Works  

Explain your scoring approach in simple language. 

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.) 

    The model looks at three things about each song: its genre, its mood, and its energy level.


- What user preferences are considered  

    It considers the user's favorite genre, their preferred mood, and the energy level they're in the mood for.



- How does the model turn those into a score  

   It gives a song 2 points for matching the user's genre, 1 point for matching their mood, and up to 1 more point for how close its energy is to what the user wants, then adds those up and ranks the highest totals first. 

- What changes did you make from the starter logic  

    I added the actual scoring, sorting, and the plain-language "Because" explanations that say why each song was picked.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  

    18.

- What genres or moods are represented  

    Genres span pop, lofi, rock, ambient, jazz, synthwave, indie pop, folk, hip-hop, classical, disco, reggaeton, blues, and funk, with moods ranging from happy and chill to intense, melancholy, and rebellious (and a few others not listed).

- Did you add or remove data  

    I added data to expand the dataset from 10 to 18.

- Are there parts of musical taste missing in the dataset  

    Yes — some genres like country, metal, EDM, R&B, K-pop, etc. are absent, most genres appear only once or twice, and the catalog is too small to represent any listener's taste in real depth.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results

    It works best for users with a coherent, mainstream taste where genre, mood, and energy all point the same direction.

- Any patterns you think your scoring captures correctly  

    When all three signals agree, the scoring correctly floats the "obvious" song to the top and cleanly separates it from weaker matches 

- Cases where the recommendations matched your intuition  

    For Deep Intense Rock, Storm Runner (rock/intense, energy 0.91) landing at #1 with a near-perfect 3.94 matched exactly what I'd expect a rock fan wanting driving music to hear first.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider 

    The scorer only looks at genre, mood, and energy, ignoring the four other columns already in the dataset — tempo, valence, danceability, and acousticness — so the likes_acoustic preference on the user profile has no effect on rankings at all.
- Genres or moods that are underrepresented  

    Due to the scope/instructions of this assignment, most genres appear only once and nearly every mood is unique, so any user whose favorite genre isn't lofi (3 songs) or pop (2 songs) gets at most one genre-matched song, and a mood match beyond the top pick is essentially impossible.

- Cases where the system overfits to one preference  
    Because a genre match is a flat +2.0 while mood and energy each cap at +1.0, the system overfits to genre — as seen in the "Genre Loyalist Trap".

- Ways the scoring might unintentionally favor some users  

    The flat +2.0 genre bonus favors users whose taste sits in a well-stocked genre (a lofi or pop fan gets a coherent, on-genre list), while users who like sparse genres are pushed toward energy-only matches from unrelated styles, giving them noticeably less relevant recommendations.

---

## 6-1. Output for Stress Tests with Diverse Profiles

```
Loading songs from data/songs.csv...
Loaded 18 songs.


########## NORMAL PROFILES ##########

======================================================================
PROFILE: High-Energy Pop
  A coherent pop lover who wants upbeat, high-energy tracks.
  Preferences: genre=pop, mood=happy, energy=0.90
======================================================================

  Top 5 recommendations:

  1. Sunrise City (pop/happy, energy=0.82) - Score: 3.92
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.92)
  2. Gym Hero (pop/intense, energy=0.93) - Score: 2.97
     Because: genre match (+2.0), energy similarity (+0.97)
  3. Rooftop Lights (indie pop/happy, energy=0.76) - Score: 1.86
     Because: mood match (+1.0), energy similarity (+0.86)
  4. Storm Runner (rock/intense, energy=0.91) - Score: 0.99
     Because: energy similarity (+0.99)
  5. Backstreet Sparks (hip-hop/confident, energy=0.87) - Score: 0.97
     Because: energy similarity (+0.97)

======================================================================
PROFILE: Chill Lofi
  Low-energy background listener; genre, mood and energy all align.
  Preferences: genre=lofi, mood=chill, energy=0.20
======================================================================

  Top 5 recommendations:

  1. Library Rain (lofi/chill, energy=0.35) - Score: 3.85
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.85)
  2. Midnight Coding (lofi/chill, energy=0.42) - Score: 3.78
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.78)
  3. Focus Flow (lofi/focused, energy=0.40) - Score: 2.80
     Because: genre match (+2.0), energy similarity (+0.80)
  4. Spacewalk Thoughts (ambient/chill, energy=0.28) - Score: 1.92
     Because: mood match (+1.0), energy similarity (+0.92)
  5. Velvet Skyline (classical/dreamy, energy=0.29) - Score: 0.91
     Because: energy similarity (+0.91)

======================================================================
PROFILE: Deep Intense Rock
  Wants driving, high-energy rock; all three signals reinforce.
  Preferences: genre=rock, mood=intense, energy=0.85
======================================================================

  Top 5 recommendations:

  1. Storm Runner (rock/intense, energy=0.91) - Score: 3.94
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.94)
  2. Gym Hero (pop/intense, energy=0.93) - Score: 1.92
     Because: mood match (+1.0), energy similarity (+0.92)
  3. Neon Boulevard (disco/energetic, energy=0.84) - Score: 0.99
     Because: energy similarity (+0.99)
  4. Backstreet Sparks (hip-hop/confident, energy=0.87) - Score: 0.98
     Because: energy similarity (+0.98)
  5. Sunrise City (pop/happy, energy=0.82) - Score: 0.97
     Because: energy similarity (+0.97)



########## ADVERSARIAL / EDGE-CASE PROFILES ##########

======================================================================
PROFILE: Genre Loyalist Trap (genre outweighs everything)
  Loves pop, but asks for near-zero energy and an off mood.
  Preferences: genre=pop, mood=intense, energy=0.05
======================================================================
  Watching for: Genre (+2.0) outweighs energy (max +1.0), so a wrong-energy pop song can still beat a perfect-energy non-pop song.

  Top 5 recommendations:

  1. Gym Hero (pop/intense, energy=0.93) - Score: 3.12
     Because: genre match (+2.0), mood match (+1.0), energy similarity (+0.12)
  2. Sunrise City (pop/happy, energy=0.82) - Score: 2.23
     Because: genre match (+2.0), energy similarity (+0.23)
  3. Storm Runner (rock/intense, energy=0.91) - Score: 1.14
     Because: mood match (+1.0), energy similarity (+0.14)
  4. Spacewalk Thoughts (ambient/chill, energy=0.28) - Score: 0.77
     Because: energy similarity (+0.77)
  5. Velvet Skyline (classical/dreamy, energy=0.29) - Score: 0.76
     Because: energy similarity (+0.76)

======================================================================
PROFILE: Sad but Hyped (conflicting mood vs. energy)
  A melancholy mood paired with high energy — signals that clash.
  Preferences: genre=indie pop, mood=melancholy, energy=0.90
======================================================================
  Watching for: Mood (+1.0) and energy pull opposite ways since sad songs are low-energy, so results may end up incoherent or ruled by genre.

  Top 5 recommendations:

  1. Rooftop Lights (indie pop/happy, energy=0.76) - Score: 2.86
     Because: genre match (+2.0), energy similarity (+0.86)
  2. Cedar Moonlight (folk/melancholy, energy=0.44) - Score: 1.54
     Because: mood match (+1.0), energy similarity (+0.54)
  3. Storm Runner (rock/intense, energy=0.91) - Score: 0.99
     Because: energy similarity (+0.99)
  4. Gym Hero (pop/intense, energy=0.93) - Score: 0.97
     Because: energy similarity (+0.97)
  5. Backstreet Sparks (hip-hop/confident, energy=0.87) - Score: 0.97
     Because: energy similarity (+0.97)
```
--- 

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested 

    Three coherent "normal" profiles — High-Energy Pop, Chill Lofi, and Deep Intense Rock — where genre, mood, and energy all reinforce each other. Plus two adversarial edge cases: Genre Loyalist Trap (loves pop but asks for near-zero energy and an off mood) and Sad but Hyped (melancholy mood paired with high energy, so the signals clash).

- What you looked for in the recommendations  

    Whether the top picks matched the profile's stated taste, whether each "Because" explanation lined up with the score, and how the three signals traded off — especially whether the dominant genre weight (+2.0) was doing too much of the work relative to mood (+1.0) and energy (max +1.0).

- What surprised you 

    How much genre overpowers everything else. In the Genre Loyalist Trap, Gym Hero (energy 0.93) still ranked #1 for a listener asking for energy 0.05, because the +2.0 genre match swamped the near-zero energy similarity. A perfectly-energy-matched song from another genre couldn't compete.

- Any simple tests or comparisons you ran? No need for numeric metrics unless you created some.

    The unit tests in tests/test_recommender.py. The profile runner in src/main.py prints ranked results so normal vs. adversarial behavior can be compared side by side. I mainly checked each adversarial profile's output against the "Watching for" hypothesis written into it, to confirm the predicted failure modes appeared.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences

    Bring the unused columns into scoring, such as tempo, valence, danceability, and acousticness.

- Better ways to explain recommendations

    Improve the "Because" text to name what's missing too (e.g., "great genre match, but energy is way off"), so users understand weak picks, not just strong ones.

- Improving diversity among the top results  

    Add a diversity penalty so the top 5 don't cluster in one genre, giving users a broader mix instead of five near-identical songs.

- Handling more complex user tastes  

    Let users express multiple genres or moods with weights, instead of forcing a single favorite of each to represent mixed tastes.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  

    Weighting is a crucial factor deciding whether the system suggests reasonable recommendation to the users.

- Something unexpected or interesting you discovered  

    A recommendation system can serve well to certain group of users and extremely poorly to others.

- How this changed the way you think about music recommendation apps  

    When I got recommendations from my Spotify account, I might start thinking from another perspective: Is the recommendation system overweighing or underweighing certain aspects?
