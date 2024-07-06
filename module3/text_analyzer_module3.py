


class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        fText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        self.text = fText.lower()
   
    def freqAll(self):        
        # split text into words
        self.words = []
        self.words = self.text.split()              #the list 'words' in this method is not imported to next method unless self.
        
        # Create dictionary
        dict = {}
        for key in set(self.words):                #this only removes the duplicate for the loop used for counting so that the loop does not run many times for the same word...
            dict[key]= self.words.count(key)
        return dict    
    def freqOf(self,word):
        # get frequency map
        freq = self.freqAll()
        # key = word
        # for items in set(self.words):          # item was used for loop as using key overwrites the value of input word    
        #     freq[key]= self.words.count(key)
        # return freq[key]
        if word in freq:
            return freq[word]
        else: 
            return 0


givenstring="Lorem ipsum dolor! diam amet,\
    consetetur Lorem magna. sed diam nonumy eirmod tempor.\
          diam et labore? et diam magna. et diam amet."

analyze = TextAnalzer(givenstring)

print(analyze.freqAll())
input_word = "hello"                    #take input from user in next version
print(f'The count of {input_word} is ',analyze.freqOf(input_word))