# http://www.npr.org/templates/transcript/transcript.php?storyId=472825113

# And here's the puzzle - can you think of a common five-letter word
# that works in the opposite way, in which the value of the
# alphabetical positions of its last four letters add up to the value
# of the alphabetical positions of its first letter. So again, a common
# five-letter word in which the value of the alphabetical positions of
# its last four letters add up to the value of the alphabetical
# position of its first letter. What word is it?


def letter_value(letter):
    return ord(letter.lower()) - ord('a') + 1


with open('/etc/dictionaries-common/words') as f:
    for word in f:
        # skip possessives
        if "'" in word:
            continue
        # skip capitalized words names
        if word[0].upper() == word[0]:
            continue
        word = word.strip()
        if len(word) != 5:
            continue
        last4 = sum([letter_value(letter) for letter in word[1:]])
        if last4 == letter_value(word[0]):
            print word
