import re
from collections import Counter
import matplotlib.pyplot as plt

with open("book.txt", encoding="utf-8") as f:
    text = f.read()

# Fix curly apostrophes so "don’t" stays one word
text = text.replace("’", "'")
words = re.findall(r"[a-z']+", text.lower())

stop_words = {
    "the", "and", "of", "to", "a", "in", "i", "he", "was", "that",
    "it", "his", "you", "with", "as", "had", "is", "at", "for", "her",
    "she", "but", "not", "my", "me", "him", "be", "on", "have", "by",
    "so", "which", "this", "are", "from", "they", "were", "there",
    "what", "all", "one", "said", "an", "would", "if", "do", "no",
    "been", "am", "some", "about", "who", "when", "or", "your", "them",
    "will", "we", "over", "like", "don't", "it's", "i'm", "i've",
    "i'll", "can't", "didn't", "you're", "that's",
}

meaningful = [w for w in words if w not in stop_words]
counts = Counter(meaningful)

print("Total words:", len(words))
print("Unique words:", len(set(words)))
for word, n in counts.most_common(25):
    print(word, n)

# Make the chart
top = counts.most_common(15)
labels = [w for w, n in top][::-1]
values = [n for w, n in top][::-1]

plt.figure(figsize=(10, 6))
plt.barh(labels, values, color="#6b3fa0")
plt.title("Most frequent words in The Picture of Dorian Gray")
plt.xlabel("Times used")
plt.tight_layout()
plt.savefig("dorian_gray_top_words.png", dpi=150)
plt.show()