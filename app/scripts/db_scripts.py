import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parentdir1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.sys.path.insert(0,parentdir)
os.sys.path.insert(0,parentdir1)

from models import db, Tense, Text

def GetShortName(tense=None):
    if tense:
        err = "Wrong tense passed to GetShortName function"
        words = tense.split()
        l = len(words)
        
        for w in words:
            if len(w) < 4:
                raise Exception(err)
            
        if l == 1:
            return words[0][:4]
        elif l == 2:
            return words[0][:2] + words[1][:2]
        elif l == 3:
            return words[0][:2] + words[1][:1] + words[2][:1]
        elif l == 4:
            return words[0][:1] + words[1][:1] + words[2][:1] + words[3][:1]
        else:
            raise Exception(err)
    else:
        raise Exception(err)
    
def AddAllExistingTenses():
    l1 = ['Present', 'Past', 'Future']
    l2 = ['Simple', 'Continuous', 'Perfect', 'Perfect Continuous']
    all_exesting_tenses_list = [w1 + ' ' + w2 for w1 in l1 for w2 in l2]
    
    for tense_name in all_exesting_tenses_list:
        tense = Tense(name=tense_name)
        tense.short_name = GetShortName(tense_name)
        
        db.session.add(tense)
        db.session.commit()
        
def AddTestTexts():
    files_list = ['text_1.txt', 'text_2.txt', 'text_3.txt']
    for filename in files_list:
        f = open(filename, 'r')
        title = f.readline()
        content = f.read()
        
        t = Text(title=title, body=content)
        
        db.session.add(t)
        db.session.commit()

def init_db():
    db.drop_all()
    db.create_all()
    
    AddAllExistingTenses()
    AddTestTexts()
    