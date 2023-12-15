def replace_words(file_path, word1, word2):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            replaced_content = content.replace(word1, word2)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(replaced_content)

        print(f'Заміна слова "{word1}" на "{word2}" виконана успішно.')

    except FileNotFoundError:
        print(f'Файл {file_path} не знайдено.')
if __name__ == "__main__":
    file_path = 'text.txt'
    word1 = input('Введіть перше слово: ')
    word2 = input('Введіть друге слово: ')
replace_words(file_path, word1, word2)

