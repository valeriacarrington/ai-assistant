import openai

# Ваш ключ API OpenAI
openai.api_key = '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'

# Функция для запроса к OpenAI API
def ai_assistant():
    try:
        question = input("\nЗадайте питання AI асистенту: ").strip()
        if not question:
            print("Питання не може бути порожнім.")
            return
        
        # Запрос к OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Используйте соответствующую модель
            prompt=question,
            max_tokens=150
        )

        # Вывод ответа
        print("\nAI Асистент відповідає:", response.choices[0].text.strip())

    except Exception as e:
        print(f"Сталася помилка: {e}")

