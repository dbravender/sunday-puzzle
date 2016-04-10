# http://www.npr.org/2016/04/10/473649171/rearrange-the-letters-in-these-names-to-solve-this-puzzle

# Name something in eight letters that's usually bought in pairs. Change
# the second letter to the letter two spaces later in the alphabet, and
# you'll get a new word that names something else that's usually bought
# in pairs. Both words are plurals. What are they?


def letter_value(letter):
    return ord(letter.lower()) - ord('a') + 1


words = set()

with open('/etc/dictionaries-common/words') as f:
    for word in f:
        words.add(word)

for word in words:
    new_word = list(word)
    new_word[1] = chr(ord(new_word[1]) + 2)
    new_word = ''.join(new_word)
    if new_word in words:
        print word, new_word

# sneakers
# speakers
