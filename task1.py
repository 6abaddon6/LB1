import re

def analyze_text(text):
    # Видаляємо розділові знаки та приводимо до нижнього регістру для ігнорування регістру
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    frequent_words = [word for word, count in word_counts.items() if count > 3]

    return word_counts, frequent_words

# Приклад використання:
text_example = "Це приклад тексту, в якому слово приклад зустрічається декілька разів. " \
               "Слово текст також зустрічається тут. І ще раз слово приклад."

word_frequency, frequent_word_list = analyze_text(text_example)

print("Частота зустрічання слів:")
for word, count in word_frequency.items():
    print(f"'{word}': {count}")

print("\nСлова, що зустрічаються більше 3 разів:")
if frequent_word_list:
    print(frequent_word_list)
else:
    print("Такі слова відсутні.")
    
