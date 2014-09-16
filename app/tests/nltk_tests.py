from nltk import *

def first():
    text = word_tokenize("And now for something completely different")
    print pos_tag(text)
    
def show_tags(t):
    text = word_tokenize(t)
    return pos_tag(text)

def list_all():
    print help.upenn_tagset()

