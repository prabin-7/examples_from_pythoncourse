def freq(text):
    word_count = {}
    words = []
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Define a function to strip punctuation from each word
    def strip_punctuation(word):
        return word.strip('.,?!')
    
    # Create a new list with stripped words (removing punctuation)
    stripped_words = [strip_punctuation(word) for word in words]
    
    key = 'little'
    word_count[key] = stripped_words.count(key)
    
    return word_count

# Sample string
string = ("Mary had a little lamb Little lamb little, \
          litle. little lamb Mary had a little lamb.Its fleece was\
           white as snow And everywhere that Mary went Mary went little little little, Mary went Everywhere that Mary went The lamb was sure to go")

# Call the function with the sample string
result = freq(string)
print("The frequency of the word 'little' is:", result['little'])
