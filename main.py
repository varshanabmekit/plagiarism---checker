import hashlib

def get_kgrams(text, k=2):
    words = text.split()
    return [" ".join(words[i:i+k]) for i in range(len(words)-k+1)]

def hash_kgrams(kgrams):
    return [hashlib.sha256(k.encode()).hexdigest() for k in kgrams]

def similarity(text1, text2):
    h1 = set(hash_kgrams(get_kgrams(text1)))
    h2 = set(hash_kgrams(get_kgrams(text2)))
    return len(h1 & h2) / len(h1) * 100 if h1 else 0

text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

print("Similarity:", similarity(text1, text2), "%")
