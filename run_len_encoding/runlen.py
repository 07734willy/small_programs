text="aaabbbcc"

def encode(text):
    if not text:
        return ""
    prev = text[0]
    lentext = len(text)
    i = 1
    while i < lentext and prev == text[i]:
        i += 1
    return prev + str(i) + encode(text[i:])

print(encode(text))
