path = 'stopwords_chinese.txt'

with open(path, 'r', encoding='utf-8') as f:
    words = f.readlines()

# Remove trailing newline characters
words = [word.strip() for word in words]

# Remove duplicates and sort
unique_sorted_words = sorted(set(words))



with open('stopwords_chinese.txt', 'w', encoding='utf-8') as f:
    for word in unique_sorted_words:
        f.write(f'{word}\n')
