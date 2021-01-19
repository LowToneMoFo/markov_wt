import random, time

class MarkovWt(object):
    """
    Class for generating a Markov model using a (large) input text and
    generating new text based on the analysed input

    """

    database = {} # dictionary for holding the markov model. i.e. list of indexes with possible following words

    def __init__(self):
        pass


    def create_markov_from_text(self, textfile):
        """
        Takes a plain text file to iterate and generate the markov chain dictionary.
        """

        #open textfile and read all contents into variable
        with open(textfile, encoding="mbcs") as f:
        #with open(textfile) as f:
            text = f.read()

            #strip unwanted characters from input
            text = text.replace("\n", " ")
            text = text.translate(["", '",.!@#$_-'])

        wordlist = text.split(' ')

        #traverse wordlist, checking out all 3 consecutive ones
        for i in range(0, len(wordlist)-2):
            key = (wordlist[i], wordlist[i+1])
            word = wordlist[i+2]

            #if key exists, append word. Else add key and word
            if key in self.database:
                self.database[key].append(word)
            else:
                self.database[key] = [word]



    def generate_sentence(self, wordlength):
        """
        Generates a sentence of <wordlength> words using the Markov database
        """
        if wordlength > 1:

            output = []
            #choose starting word pair
            key = random.choice(list(self.database.keys()))

            #add wordpair to output list
            output.append(key[0])
            output.append(key[1])
            length = 2


            # keep adding words from database until desired length is reached
            while length < wordlength:
                key = (output[length-2],output[length-1]) #new key is last 2 words of current chain

                # if current key doesn't exist, terminate output early.
                # (this happens when there is no recorded follow up for some word combinations)
                if not key in self.database:
                    break

                # if current key exists and has multiple options, choose one at random:
                #elif len(self.database[key]) > 1:
                else:
                    options = self.database[key]
                    output.append(options[random.randint(0, len(options)-1)])
                    #output.append(self.database[key][random.randint(len(self.database[key]))])

                # otherwise, choose only option:
                #else:
                #    output.append(self.database[key][0])

                length += 1
                
            #parse output for some corrections:
                
            #capitalize letters of word following a colon
            for i in range(len(output)-1):
                #print(output[i])
                if len(output) > 0:
                    if output[i][-1] in [".", "!", "?"]:
                        #print("ja!")
                        output[i+1] = output[i+1].capitalize()
                        #FIXME!
                

            #return wordlist as single sentence (with capital and colon):
            output =  " ".join(output) + "."
            return output.capitalize()

        else:
            return False

my_markov = MarkovWt()

my_markov.create_markov_from_text("TrumpTweets2.txt")

#generate new sentences to console with short delays:
while True:
    print(my_markov.generate_sentence(random.randint(10,30)))
    print("---")
    time.sleep(5)










