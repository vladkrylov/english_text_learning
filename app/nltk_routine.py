from nltk import *

def recognize(t):
    text = word_tokenize(t)
    return pos_tag(text)

def construct_verbs_dict(tagged_list=[]):
    return {tagged_list.index(w): w[0] for w in tagged_list if w[1][0] is "V"}

def construct_verbs_list(tagged_list=[]):
    return [w[0] for w in tagged_list if w[1][0] is "V"]

def construct_verbs_set(tagged_list=[]):
    return {w[0] for w in tagged_list if w[1][0] is "V"}
