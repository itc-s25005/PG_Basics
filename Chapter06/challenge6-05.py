words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words[:-2] + [words[-2] + words[-1]])
print(one)
