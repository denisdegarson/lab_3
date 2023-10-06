import json
import os

import mypackage.module1 as md1


# Функція для обрахунку кількості символів у тексті
def count_characters(text):
    return len(text)


# Функція для обрахунку кількості слів у тексті
def count_words(text):
    words = text.split()
    return len(words)


# Функція для обрахунку кількості речень у тексті
def count_sentences(text):
    sentences = text.split('. ')
    return len(sentences)


def trim_text_from_file(input_file, num_sentences, word_count, character_count):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            # Видаляємо зайві речення
            text = file.read()
            sentences = text.split('. ')
            trimmed_text = '. '.join(sentences[:num_sentences])
            # Видаляємо зайві слова
            text = trimmed_text
            words = text.split()
            trimmed_text = ' '.join(words[:word_count])
            # Видаляємо зайві символи
            text = trimmed_text
            trimmed_text = text[:character_count]
            return trimmed_text
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None


def main():
    # Завантаження конфігураційного файлу
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Отримання інформації з конфігураційного файлу
    input_file = config['input_file']
    target_language = config['target_language']
    output_destination = config['output_destination']
    sentence_count = config['sentence_count']
    word_count = config['word_count']
    character_count = config['character_count']

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Отримання інформації про текст
        file_size = os.path.getsize(input_file)
        character_count = count_characters(text)
        word_count = count_words(text)
        sentence_count = count_sentences(text)
        detected_language = md1.LangDetect(text)

        text = trim_text_from_file(input_file, sentence_count, word_count, character_count)

        # Виведення інформації про текст
        print(f"Назва файлу: {input_file}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {character_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
        print(f"Мова тексту: {detected_language}")

        # Переклад тексту
        translation = md1.TransLate(text=text, scr=detected_language, dest=target_language)

        if output_destination == "screen":
            # Виведення перекладу на екран
            print(f"Переклад на мову {target_language}:")
            print(translation)
        elif output_destination == "file":
            # Збереження перекладу в файл
            output_file = f"{input_file.split('.')[0]}_{target_language}.txt"
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(translation)
            print("Ok")

    except Exception as e:
        print(f"Помилка: {str(e)}")

if __name__ == "__main__":
    main()
