# 🎬 Script AI — Video Script Writing Assistant using DeepSeek

Script AI is an AI-powered video script generation tool built with the DeepSeek model via OpenRouter API. Designed for content creators, marketers, and social media influencers, it helps generate high-quality, engaging scripts tailored for platforms like YouTube, Instagram, TikTok, and more.

✨ Whether you need a compelling intro, a well-structured body, or a catchy CTA — Script AI crafts your script with the power of modern AI.

---

## 🚀 Features

- 🎯 Generate detailed video scripts using custom prompts
- 🧠 AI writing tailored to your chosen **niche/topic**
- 📚 Access and manage your **previous scripts** in one place (MongoDB-based history)
- 🔐 Secure API handling using environment variables
- 🧩 Modular Django backend with clean UI for script creation

---

## 🛠️ Tech Stack

| Layer      | Tech         |
|------------|--------------|
| Backend    | Python, Django |
| AI Model   | DeepSeek via OpenRouter API |
| Database   | MongoDB (via PyMongo) |
| Env Mgmt   | python-dotenv |
| Frontend   | Django Templating (HTML/CSS/JS) |

---

## 🧰 Installation

> ⚠️ Python and MongoDB must be pre-installed on your system.

```bash
# 1. Clone the repository
git clone https://github.com/your-username/script-ai.git
cd script-ai

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create a .env file in the root directory with the following:
OPENROUTER_API_KEY=your_api_key_here
MONGODB_URI=your_mongodb_uri_here

# 5. Run the Django server
python manage.py runserver
