import json
import openai
from ai_assistant import ai_assistant

# Функція для завантаження проєктів з файлу
def load_projects():
    try:
        with open('projects.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл з проєктами не знайдений!")
        return []

# Функція для відображення списку проєктів
def show_projects(projects):
    print("\nСписок доступних проєктів:")
    for idx, project in enumerate(projects, 1):
        print(f"{idx}. {project['project_name']}")

# Функція для отримання інформації про проєкт
def get_project_info(projects, project_idx):
    if project_idx < 1 or project_idx > len(projects):
        print("Невірний індекс проєкту.")
        return
    project = projects[project_idx - 1]
    print(f"\nПроєкт: {project['project_name']}")
    print(f"Короткий опис: {project['description']['short']}")
    print(f"Повний опис: {project['description']['full']}")
    print(f"Нагороди: {project['rewards']['amount']}")
    print(f"Посилання: {project['links']['website']}")

# Основна функція для роботи з меню
def main():
    projects = load_projects()
    if not projects:
        print("Немає даних про проєкти. Завершення програми.")
        return

    while True:
        print("\nОберіть дію:")
        print("1. Переглянути криптопроєкти")
        print("2. Отримати інформацію про проєкт")
        print("3. Задати питання AI асистенту")
        print("4. Вийти")

        choice = input("Ваш вибір: ").strip()

        if choice == '1':
            show_projects(projects)
        elif choice == '2':
            try:
                project_idx = int(input("Оберіть номер проєкту для перегляду: ").strip())
                get_project_info(projects, project_idx)
            except ValueError:
                print("Будь ласка, введіть правильний номер.")
        elif choice == '3':
            ai_assistant()
        elif choice == '4':
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == '__main__':
    main()
