with open("Madlibs.txt", "r") as f:
    story = f.read()

words = set()
start_of_words = -1

check_start = "<"
check_end = ">"
for idx, chr in enumerate(story):
    if chr == check_start:
        start_of_words = idx

    if chr == check_end and start_of_words != -1:
        word = story[start_of_words: idx + 1]
        words.add(word)
        start_of_words = -1

ans = {}

for word in words:
    type = input("enter a word" + word + ": ")
    ans[word] = type

for word in words:
   story = story.replace(word, ans[word])

print(story)
