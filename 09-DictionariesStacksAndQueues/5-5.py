paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into individual words
words = paragraph.split()

# Create an empty dictionary to store counts
word_count = {}

# Loop through each word
for word in words:
    if word in word_count:
        word_count[word] += 1   # Increase count if word already exists
    else:
        word_count[word] = 1    # Add word to dictionary with count 1

print(word_count)