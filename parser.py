#Parse a document of text
from nltk.tag.stanford import StanfordNERTagger
import operator
from pprint import pprint
from nltk.tokenize import word_tokenize
import ner

st = ner.SocketNER(host='localhost', port=8080)

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

#st = StanfordNERTagger('/Users/Owner/stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/Owner/stanford-ner-2014-06-16/stanford-ner.jar')

book_path = 'texts/1984.txt'
text = " ".join( [line.strip() for line in open('texts/1984.txt', 'r')] )
sentence = ""
#splits = word_tokenize(jungle) 
#make new list to keep ngrams generated
#tagged = splits

#tagged.extend([" ".join(ng) for ng in find_ngrams(splits,2)])

#tagged.extend([" ".join(ng) for ng in  find_ngrams(splits,3)])

#tagged.extend([ " ".join(ng) for ng in find_ngrams(splits,4) ])

def combineDicts(d1,d2):
    """
    Combine two dictionaries of LISTS into a single dictionary of SETS
    returns a single new dictionary
    """
    combination = {}
    for k in d1.keys():
        if k in combination:
            entity_list = d1[k]
            for entity in entity_list:
                combination[k].add(entity)
        else:
            combination[k] = set()
            for entity in d1[k]:
                combination[k].add(entity)

    for k in d2.keys():
        if k in combination:
            entity_list = d2[k]
            for entity in entity_list:
                combination[k].add(entity)
        else:
            combination[k] = set()
            for entity in d2[k]:
                combination[k].add(entity)

    return combination

#n is the size of the chunks
n = 2500
l = text
chunks = [l[i:i+n] for i in range(0, len(l), n)]

"""
first = chunks[1]
second = chunks[2]

ta1 = st.get_entities(first)
print (ta1)

ta2 = st.get_entities(second)
print (ta2)
print('---')

print (combineDicts(ta1,ta2))
exit()

"""

all_tags={} 

for chunk in chunks:
    tagged = st.get_entities(chunk)
    all_tags = combineDicts(tagged,all_tags)
    
#pprint(all_tags)



#Now we have all the Entities that occur in the book. 
#Next we will count the frequency of those entities
people = all_tags['PERSON']
"""
entity_count = {}
for entity in people:
    count = text.count(entity)
    entity_count[entity] = count
"""
all_entity_count = {}
for tag in all_tags:
    entity_tag = all_tags[tag]
    entity_count = {}
    for entity in entity_tag:
        count = text.count(entity)
        entity_count[entity] = count
    sorted_entity = [a for a in reversed(sorted(entity_count.items(), key=operator.itemgetter(1)))]
    all_entity_count[tag] = sorted_entity


pprint(all_entity_count)

exit()

#Create a dictionary of tags
tag_dict = {}

for token in all_tags:
    word = token[0]
    tag = token[1]

    if tag in tag_dict:
        if word in tag_dict[tag]:
            tag_dict[tag][word] += 1
        else: 
            tag_dict[tag][word] = 1
    else:
        #1st level was tag category
        #Dictionary of Dictionaries: 2nd level is invididual tag
        #This is so we can count the number of individual tags
        #tag_dict[tag]={token[0]: 1}
        #This is where we initialize a new dictionary
        tag_dict[tag] = {word:1}

#print(tag_dict.keys())
person_dict = tag_dict['R']

sorted_persons = [a for a in reversed(sorted(person_dict.items(), key=operator.itemgetter(1)))]

pprint(sorted_persons)
exit()
#pprint(tag_dict['ORGANIZATION'])

sorted_persons = [a for a in reversed(sorted(person_dict.items(), key=operator.itemgetter(1)))]

pprint(sorted_persons)
##pprint(tag_dict.keys())
