#WAP to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Function to calculate word frequency
def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
        #'get' method of a dictionary is used to retrieve the value associated with the specified key. If the key (word in this case) is not present in the dictionary, it returns the default value (which is 0 in this case).
    return frequency

input_text = input("Enter a sentence: ")

# Calculate word frequency
frequency_dict = word_frequency(input_text)

# Sort the keys alphanumerically
sorted_keys = sorted(frequency_dict.keys())

print("Word Frequency:")
for key in sorted_keys:
    print(f"{key}: {frequency_dict[key]}")
