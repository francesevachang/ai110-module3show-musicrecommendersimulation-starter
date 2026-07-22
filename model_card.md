# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

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
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
