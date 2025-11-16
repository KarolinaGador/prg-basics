###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
count = 0

# Count vowels in the text

i = 0
while i < len(text):
    if text[i] in vowels:
        count += 1
    i += 1

    
    

print(f"The number of vowels in the text is: {count}")
