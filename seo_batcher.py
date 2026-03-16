import os
import csv
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Используем твой рабочий ключ из .env
client = Groq(api_key=os.getenv("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"))

def generate_seo_tags(topic):
    prompt = f"Ты SEO-специалист. Для темы '{topic}' напиши привлекательный Title (до 60 симв.) и Description (до 160 симв.) на русском языке. Ответ дай в формате: Title | Description"
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content

def main():
    # Читаем темы из файла keywords.txt
    if not os.path.exists('keywords.txt'):
        print("Ошибка: Создай файл keywords.txt и напиши там темы!")
        return

    with open('keywords.txt', 'r', encoding='utf-8') as f:
        topics = [line.strip() for line in f if line.strip()]
    
    print(f"Начинаю массовую обработку {len(topics)} тем...")
    
    with open('seo_results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Topic", "SEO Title | Description"])
        
        for topic in topics:
            print(f"Генерирую для: {topic}")
            try:
                result = generate_seo_tags(topic)
                writer.writerow([topic, result])
            except Exception as e:
                print(f"Ошибка на теме {topic}: {e}")
            
    print("\n✅ ГОТОВО! Проверь файл seo_results.csv в папке.")
    
if __name__ == "__main__":
    main()