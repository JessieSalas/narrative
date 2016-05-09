import nltk
import string
import re
import time

exampleArray = ['The incredibly intimidating NLP scares people away who are sissies.']


orwell = " ".join( [line.strip() for line in open('1984.txt', 'r')] )
for c in string.punctuation:
    orwell=orwell.replace(c,'')

print(orwell)

contentArray =["The room they were standing in was long-shaped and softly lit. The telescreen was dimmed to a low murmur; the richness of the dark-blue carpet gave one the impression of treading on velvet. At the far end of the room O'Brien was sitting at a table under a green-shaded lamp, with a mass of papers on either side of him. He had not bothered to look up when the servant showed Julia and Winston in. ",
               'Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.',
               'They just began expansion into food products, which has been going quite well so far for them.',
               'I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.',
               'Starbucks is also indeed expanding their number of stores as well.',
               'Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.',
               'Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.',
               'As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.',
               'Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!',
               'Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.',
               'Increase in supply... well you know the rules...',]
contentArray=[orwell]

t_d = {}

##let the fun begin!##
def processLanguage():
        for item in contentArray:
            try:

                tokenized = nltk.word_tokenize(item)
                tagged = nltk.pos_tag(tokenized)
                #print(tagged)
                for t in tagged:
                    tag = t[1]
                    if tag in t_d:
                        t_d[tag].add(t[0])
                    else:
                        t_d[tag]=set([t[0]])



                #namedEnt = nltk.ne_chunk(tagged)
                #print(namedEnt)
                #namedEnt.draw()

                #time.sleep(1)
                print(t_d['NNP'])
            
            except:
                pass

processLanguage()
