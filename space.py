import spacy
from pprint import pprint
nlp = spacy.load('en',)

NOUN = "NOUN"
ATTRIBUTE = "attr"
ADJ = "ADJ"

def print_fine_pos(token):
    return (token.tag_)

def isDescribed(pos, dep):
    return pos == NOUN and dep == ATTRIBUTE

def allAdj(toks):
    dic = {}
    for tok in toks:
        #prup = "{0} {1} {2} {3} {4} ".format(tok.orth_, tok.dep_, tok.pos_, [t.orth_ for t in tok.lefts], [t.orth_ for t in tok.rights])
        item = tok.orth_
        dependency = tok.dep_
        print(item)
        print(tok.pos_)
        pos = tok.pos_
        if isDescribed(pos,dependency):
            properties = [t.orth_ for t in tok.lefts if t.dep_ == "amod"]
            if len(properties) != 0:
                if item in dic:
                    for p in properties:
                        dic[item].add(p)
                else:
                    dic[item] = set([p for p in properties])
    pprint(dic)

#ext = " ".join( [line.strip() for line in open('texts/1984.txt', 'r')] )
#text = text[:20000]

text = "Kenny Smith was a short man. He is a bad person honestly. Kenny cannot die if he is young. Larry is big. Larry is a mess. Kenny is honest."
toks = nlp(text)
allAdj(toks)

exit()

def pos_tags(sentence):
    #sentence = unicode(sentence, "utf-8")
    tokens = nlp(sentence)
    tags = []
    for tok in tokens:
        tags.append((tok,print_fine_pos(tok)))
    return tags

b = nlp('My happy dog is good.')
print(pos_tags("I love a man who is tall and delightful."))

for token in b:
    print(token.dep_)

print(nlp.parser(  b  ))
print(dir(nlp))
