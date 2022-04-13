def is_included(word, sentence):
    if word in sentence:
        return "yes"
    else:
        return "no"

print(is_included("love", "I love you"))
print(is_included("me", "I love you"))
print(is_included("you", "I love you"))