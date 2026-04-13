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
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
In real-world recommender systems, recommendations are usually created by combining multiple features instead of relying on just one. Systems often use a weighted scoring method that considers factors like mood, genre, energy, tempo, and user preferences to rank songs. Mood helps capture the overall vibe a user wants, but it is often combined with numeric features like energy and tempo to make the recommendations more precise. In my version, I prioritize mood as the main factor by giving higher scores to songs that match the user’s desired feeling, while also using other features to refine the final results.

## Song features used:
	•	Mood
	•	Genre
	•	Energy
	•	Tempo (BPM)
## UserProfile stores:
	•	Preferred mood
	•	Favorite genres
	•	Preferred energy level
	•	Preferred tempo range

My recommender system works by comparing each song in the dataset to a user’s taste profile and assigning a score based on how well it matches. In real-world systems, recommendations usually combine multiple features, but in my version I prioritize simplicity while still capturing key preferences like mood, genre, and energy. Each song includes features such as genre, mood, energy, tempo, valence, danceability, and acousticness, while the user profile stores preferred values for these attributes. The system reads one song at a time from the dataset, evaluates how closely it matches the user’s preferences, and then ranks all songs based on their scores.

## Algorithm Recipe
Each song is scored using a simple point-based system. If the song’s genre matches the user’s favorite genre, it receives +2.0 points. If the song’s mood matches the user’s preferred mood, it receives +1.0 point. The system then calculates an energy similarity score based on how close the song’s energy is to the user’s target energy, using a formula like (1 − |song_energy − target_energy|). The total score is the sum of these values. After scoring all songs, the system sorts them in descending order and recommends the top-ranked songs.

## Potential Biases
This system may over-prioritize genre since it has the highest point value, which could cause it to ignore songs from different genres that still match the user’s mood or energy well. It may also be somewhat narrow because it only uses exact matches for mood and genre, limiting diversity in recommendations. Additionally, relying heavily on energy similarity might favor songs within a small range and overlook slightly different but still enjoyable options.

## Sample output 
![Recommendations Screenshot](images/recommendations.png)

## High Energy Pop
![High Energy Pop](images/high_energy_pop_profile.png)

## Chill Lofi
![Chill Lofi](images/chill_lofi_profile.png)

## Deep Intense Rock
![Deep Intense Rock](images/deep_intense_rock_profile.png)

## test
I tested several user profiles, including a “High-Energy Pop” listener, a “Chill Lofi” listener, and a “Deep Intense Rock” listener. One thing that surprised me was how often the same song showed up at the top for certain profiles, especially when their preferences were very specific. For example, the “High-Energy Pop” profile and a general “Happy Pop” profile both kept getting the same top song. This happens because the system heavily rewards matching energy and genre, so a song like “Gym Hero” keeps winning since it is both high-energy and pop.  

When comparing profiles, the differences usually made sense. The “Chill Lofi” profile produced slower, calmer songs, while the “Deep Intense Rock” profile shifted toward louder and more energetic tracks. However, the system sometimes felt repetitive because it focuses on exact matches instead of offering similar alternatives. Overall, the results show that the recommender understands basic preferences, but it still struggles to provide variety.
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

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users
I tested several user profiles, including a “High-Energy Pop” listener, a “Chill Lofi” listener, and a “Deep Intense Rock” listener. One thing that surprised me was how often the same song showed up at the top for certain profiles, especially when their preferences were very specific. For example, the “High-Energy Pop” profile and a general “Happy Pop” profile both kept getting the same top song. This happens because the system heavily rewards matching energy and genre, so a song like “Gym Hero” keeps winning since it is both high-energy and pop.  

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This recommender has several limitations due to its small dataset and simple scoring method. It only works with a limited number of songs, which makes the recommendations repetitive and less diverse. 
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Through this project, I learned how recommender systems turn simple data into predictions by assigning scores based on how well items match a user’s preferences. Even with just a few features like genre, mood, and energy, the system was able to produce recommendations that often felt reasonable. I realized that the way features are weighted plays a big role in what gets recommended, and small changes in the scoring logic can lead to very different results.

I also learned how bias and unfairness can easily appear in these systems. For example, if certain genres or moods are overrepresented in the dataset, the recommender will favor them more often. The system can also become repetitive by over-relying on exact matches, which limits diversity and ignores other good options. This showed me that both the data and the design of the algorithm are important for making recommendations feel fair and balanced.
---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:


> Moodfinder 1.0
---

## 2. Intended Use

- What is this system trying to do
- Who is it for
This system is designed to recommend a small set of songs based on a user’s preferences for genre, mood, and energy level. It aims to suggest songs that best match what the user is looking for at a given moment. The recommender is built for classroom exploration and learning purposes, so it is meant to demonstrate how recommendation systems work rather than serve real users.

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

The recommender system looks at each song’s genre, mood, and energy level and compares them to the user’s preferences. The user profile includes a preferred genre, mood, and a target energy level. For each song, the system gives points if the genre and mood match the user’s preferences, and it also calculates how close the song’s energy level is to what the user wants. These values are combined into a total score for each song. Finally, the songs are ranked based on their scores, and the top results are recommended to the user.
---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect
The dataset contains 18 songs stored in the data/songs.csv file. The original dataset started with 10 songs, but I added more to increase variety and improve the recommendations. It includes a mix of genres such as pop, rock, lofi, classical, and EDM, along with moods like happy, chill, intense, and tranquil. However, the distribution is still uneven, with some genres and moods appearing only once. Overall, the dataset reflects a simplified version of general music taste rather than representing a specific group of users.
---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits
The recommender works well for users with clear and specific preferences, especially when their desired genre, mood, and energy level are well represented in the dataset. For example, a chill lofi listener receives calm, low-energy songs, while a high-energy rock listener gets more intense tracks, which matches expectations. The system also performs well when the user’s preferences align closely with the available songs, producing results that feel accurate. Another strength is its simplicity and transparency, since it is easy to understand how each feature contributes to the final score. This makes it easier to explain why certain songs are recommended.
---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product
This system may over-prioritize genre since it has the highest point value, which could cause it to ignore songs from different genres that still match the user’s mood or energy well. It may also be somewhat narrow because it only uses exact matches for mood and genre, limiting diversity in recommendations. Additionally, relying heavily on energy similarity might favor songs within a small range and overlook slightly different but still enjoyable options.
---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.
To evaluate the system, I tested multiple user profiles such as High-Energy Pop, Chill Lofi, and Deep Intense Rock. I checked whether the recommended songs matched the user’s preferences in terms of genre, mood, and energy level. I also compared how the results changed when I adjusted feature weights, which helped me understand how sensitive the system is to different factors. In addition, I compared the behavior of my recommender to how real apps like Spotify recommend music, noticing that my system is more repetitive due to the small dataset. These tests showed that the system can capture basic preferences but still lacks variety and flexibility.
---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes
If I had more time, I would improve this recommender by expanding the dataset to include more songs and a wider range of genres and moods. I would also add more features such as tempo, valence, and danceability to better capture how songs feel. Another improvement would be adding a diversity mechanism so the top recommendations are not too similar and can introduce new options to the user. Finally, I would improve how the system explains its recommendations so users understand why certain songs are suggested.
---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

One thing that surprised me during this project was how often the same song appeared at the top for certain user profiles. I did not expect such a simple scoring system to feel both accurate and repetitive at the same time. Building this project changed how I think about real music recommenders, because I realized that even simple algorithms can produce results that seem meaningful, but they depend heavily on data and design choices. It also showed me that human judgment still matters, especially when deciding what makes recommendations feel fair, diverse, and useful.