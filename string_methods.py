text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier())
print("1234".isidentifier())
print("ananananananananananan".count("ana"))
print("ananananananananananan".replace("ana","banana"))
print("ananananananananananan".find("ana",1))
print("bbbbbbbabbbbbabbbbabbbb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind-sir, how may! I be of your service today?"
punctuation = ".,;!?-"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p," ") #replace punctuation with nothing
print(sentence)
sentence = sentence.replace(" ","")
#split the sentence into words
words = sentence.split(" ")
print(words)