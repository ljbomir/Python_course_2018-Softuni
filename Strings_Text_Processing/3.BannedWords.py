banned_words = input().split()
text = input()


for word in text:
    for bw in banned_words:
        text = text.replace(bw, '*' * len(bw))
print(text)
