#6. Reverse Words in a Sentence (String + List + Loop)
#Write a function that takes a sentence and returns it with words reversed, not characters.
#Example: "I love Python" → "Python love I"

def reversed_string(sentence):
    words = sentence.split()
    reversed_sentence = words[::-1]
    result =  "".join(reversed_sentence)
    return result

print(reversed_string("I Love Python"))