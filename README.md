# 🎵 Music Recommender AI System

## Original Project (Modules 1–3)

This project is based on the Module 3: Music Recommender Simulation from CodePath’s AI coursework. The original goal was to build a rule-based system that recommends songs by scoring how well each song matches a user’s preferences (genre, mood, energy, etc.). It demonstrated how simple data and weighted features can produce meaningful recommendations.

---

## Title & Summary

The Music Recommender AI System suggests songs based on a user’s taste profile and enhances the results with AI-generated explanations. It combines a deterministic scoring algorithm with a Gemini-powered explanation layer to make recommendations both accurate and easy to understand.

This matters because modern AI systems are not just about making decisions—they must also explain those decisions clearly to users.

---

## Architecture Overview

The system consists of three main components:

- Recommender (recommender.py)  
  Scores and ranks songs using weighted features such as genre, mood, energy, and similarity metrics.

- AI Explainer (ai_explainer.py)  
  Uses the Gemini API to rewrite technical scoring explanations into human-friendly language.

- Runner (main.py)  
  Orchestrates the workflow and prints results in a structured table.

### Data Flow

User Preferences → Scoring → Ranking → AI Explanation → Final Output

The AI layer does not replace the logic but improves interpretability.

---

## Setup Instructions

1. Clone the repository:
bash git clone <your-repo-url> cd music-recommender-ai-system 

2. (Optional) Create a virtual environment:
bash python3 -m venv .venv source .venv/bin/activate 

3. Install dependencies:
bash pip install -r requirements.txt 

4. Create a .env file in the root directory:
bash GEMINI_API_KEY=your_api_key_here 

5. Run the program:
bash python3 -m src.main 

---

## Sample Interactions

### Example 1 – Deep Intense Rock Profile

Input:
- Genre: rock  
- Mood: intense  
- Energy: 0.85  

Output:
- Storm Runner  
- Gym Hero  

AI Explanation:
> These songs were selected because they match your intense mood and have energy levels very close to what you prefer, creating a powerful and engaging listening experience.

---

### Example 2 – Chill Lofi Profile

Input:
- Genre: lofi  
- Mood: calm  
- Energy: 0.3  

Output:
- Calm, low-energy tracks  

AI Explanation:
> These songs fit your calm mood and have softer energy levels, making them ideal for a relaxed and peaceful listening session.

---

### Example 3 – High Energy Pop Profile

Input:
- Genre: pop  
- Mood: energetic  
- Energy: 0.9  

Output:
- Upbeat and danceable songs  

AI Explanation:
> These songs were chosen because they are energetic, upbeat, and closely match the lively style you prefer.

---

## Design Decisions

- Separation of logic and AI  
  The recommender uses deterministic scoring, while AI is only used for explanation. This keeps the system transparent and reliable.

- Feature-based scoring  
  Multiple features (mood, genre, energy, etc.) are combined instead of relying on a single factor.

- AI for interpretability  
  Instead of replacing logic, Gemini improves user understanding by translating technical reasoning into natural language.

### Trade-offs
- API calls introduce slight latency  
- Small dataset limits recommendation diversity  
- Rule-based scoring lacks adaptability compared to ML models  

---

## Testing Summary

I tested the system using multiple user profiles:
- High-Energy Pop  
- Chill Lofi  
- Deep Intense Rock  

### What worked:
- Recommendations aligned well with user preferences  
- AI explanations improved clarity and usability  

### What didn’t:
- Some results were repetitive due to strong feature weighting  
- Limited dataset reduced variety  

### Key takeaway:
Small changes in feature weights significantly affect recommendation outcomes.

All tests passed successfully using pytest, confirming that both the recommendation logic and AI explanation function execute correctly.

---

## Reliability and Evaluation

The system was evaluated through repeated manual testing using different user profiles. It consistently returned 5 relevant recommendations per run, showing stable behavior across inputs.

The AI explanation layer was also tested to ensure it converts technical scoring details into clear, human-friendly sentences. Error handling ensures that if the API fails or the key is missing, the system falls back to the original explanation instead of crashing.

Overall, the system is reliable for structured inputs but limited by dataset size and feature weighting.

---

## Reflection and Ethics

This system has several limitations and potential biases. Because it uses a small dataset, some genres and moods are underrepresented, which can lead to repetitive recommendations. The scoring system also gives more weight to certain features like mood and genre, which may reduce diversity and ignore songs that could still be a good match in different ways.

While this recommender is designed for learning purposes, a similar system in the real world could be misused by over-personalizing content and limiting exposure to new or diverse options. To reduce this risk, future improvements could include adding diversity constraints and giving users more control over recommendation settings.

One thing that surprised me during testing was how often the same songs appeared at the top for different but similar user profiles. This showed me how sensitive the system is to feature weighting and how easily it can become repetitive.

During this project, AI tools were helpful for improving explanations and refining parts of the code. For example, AI helped generate clearer, more user-friendly explanations from technical scoring logic. However, there were also times when AI suggestions were not fully aligned with my implementation, which required me to carefully review and adjust them. This reinforced the importance of understanding the system rather than relying entirely on AI-generated output.

---

## Running Tests

Run all tests with:

bash python -m pytest 

---

## System Diagram

System Diagram

---