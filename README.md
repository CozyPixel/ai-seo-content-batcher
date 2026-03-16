# AI SEO Content Batcher 🚀

An automated tool designed to generate high-quality SEO metadata (Titles and Descriptions) in bulk using the **Llama 3.1** model via **Groq API**.

## 🌟 Key Features
- **Bulk Processing:** Handles multiple keywords/topics at once from a text file.
- **AI-Powered:** Uses Llama 3.1 for human-like, SEO-optimized content generation.
- **Fast Execution:** Leverages Groq's high-speed inference engine.
- **CSV Export:** Automatically saves results into a structured format ready for Google Sheets or Excel.

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Llama-3.1-8b-instant (via Groq SDK)
- **Environment:** Dotenv for secure API key management

## 🚀 How to Use
1. Clone the repository.
2. Install dependencies: `pip install groq python-dotenv`.
3. Add your `GROQ_API_KEY` to the `.env` file.
4. Place your topics in `keywords.txt`.
5. Run the script: `python seo_batcher.py`.
