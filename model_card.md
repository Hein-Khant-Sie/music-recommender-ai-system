# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
Moodfinder 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  
Moodfinder 1.0 is designed to recommend songs based on a user’s preferences for genre, energy, and mood. It assumes that users can describe their taste using these three features and that similar values will lead to better matches. The system generates a ranked list of songs that best fit the user’s preferences. This model is mainly built for classroom exploration rather than real-world users, so it focuses on demonstrating how recommendation logic works rather than handling complex or large-scale music data.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  
The model looks at three main features of each song: genre, energy level, and mood. It compares these features to the user’s preferences and assigns a score based on how closely they match. Genre and mood are treated as exact matches, while energy is compared numerically to measure how close it is to the user’s desired level. These values are combined into a final score, and songs are ranked from highest to lowest. I adjusted the weights from the starter logic so that energy has a stronger influence on the final ranking.
Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  
The model uses a dataset of 18 songs stored in a CSV file. The songs include a mix of genres such as pop, rock, lofi, classical, and EDM, along with moods like happy, chill, intense, and tranquil. However, the dataset is small and unevenly distributed, with some genres and moods appearing only once. I did not make major changes to the dataset, so it still lacks diversity and does not fully represent different types of musical taste.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users with clear and simple preferences. For example, a chill lofi listener receives calm, low-energy songs, while a high-energy rock listener gets more intense tracks. The model captures basic patterns correctly, especially when energy levels play an important role in the listening experience. In many cases, the recommendations matched what I would expect based on the user’s preferences.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
The system struggles because it relies on a limited set of features—mainly genre, energy, and mood—while ignoring other important attributes like tempo, valence, or danceability. This makes the recommendations less nuanced and can miss songs that feel similar in other ways. Some genres and moods are also underrepresented in the dataset, which means users with those preferences receive fewer or repetitive recommendations. The scoring system can overfit to one preference, especially genre, since it uses an exact-match bonus that narrows the results. As a result, users with specific or extreme preferences may be favored or disadvantaged depending on how well their profile aligns with the limited dataset.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.
To evaluate the recommender, I tested several distinct user profiles such as a high-energy pop listener, a calm lofi listener, and an intense rock listener. I looked at whether the top recommendations matched the user’s preferences in terms of genre, energy level, and mood. I also checked if the results changed meaningfully when I adjusted weights or removed certain features, such as reducing genre importance or disabling mood. One surprising result was that the same song often appeared at the top for certain profiles, showing that the system can be repetitive. I also compared outputs before and after weight changes to see how sensitive the system was to different factors, which helped reveal biases in the scoring logic.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would improve the model by adding more features such as tempo, valence, and danceability to better capture how songs feel. I would also expand the dataset to include more songs and a wider range of genres and moods. Another improvement would be adding a diversity mechanism so the top results are not always from the same genre. Additionally, I would explore ways to explain recommendations more clearly to users.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
Through this project, I learned that recommender systems depend heavily on both the scoring logic and the dataset. One interesting discovery was how changing weights can significantly affect the results. I also realized that a small dataset can limit the system’s ability to provide diverse recommendations. This project changed how I think about music recommendation apps, showing me that even simple systems require careful design to balance accuracy and variety.


## Relectition on the process of building and testing the recommender system.
My biggest learning moment during this project was realizing how much small changes in the scoring system can affect the final recommendations. At first, I thought the algorithm would just work as long as the logic made sense, but I learned that even adjusting one weight can completely change which songs rank at the top. Using AI tools like Copilot helped me move faster when writing and modifying code, especially for testing different ideas, but I still had to double-check the logic to make sure the changes actually matched what I intended. Sometimes the AI would suggest something that worked technically but didn’t make sense for my goal.

What surprised me the most was how a simple algorithm could still feel like a real recommendation system. Even with just a few features like genre, energy, and mood, the results often felt logical and matched what I expected. At the same time, I noticed how easily the system could become repetitive or biased, which showed me how important data and balance are. If I continued this project, I would try adding more features and improving diversity so the recommendations feel less repetitive and more realistic.