#!/usr/bin/env python

from word_splitter import analyze_word

slot_dicts = {}

def init():
    for i in list(range(1,15)) + ['stress']:
        slot_dicts[i] = {}
        try:
            with open('data/slot%s.dat' % i, 'r') as f:
                for line in f:
                    line = line.replace('\n','')
                    pts = line.split(': ')
                    slot_dicts[i][pts[1]] = pts[0]
            if i == 11:
                with open('data/slot11deg.dat', 'r') as f:
                    for line in f:
                        line = line.replace('\n','')
                        pts = line.split(': ')
                        slot_dicts[i][pts[1]] = pts[0]
        except:
            pass

def describe_formative(slots):
    desc = []
    for i in list(range(1,15)) + ['stress']:
        if i in slots:
            try:
                if i not in (5, 6, 7, 11):
                    desc.append(slot_dicts[i][slots[i]])
                elif i == 5:
                    if slots['type5'] == 'Cx':
                        desc.append(str(slots[i]))
                    else:
                        desc.append(slot_dicts[1][slots[i]])
                elif i == 6:
                    if slots['type5'] == 'Cx':
                        desc.append(slot_dicts[i][slots[i]])
                    else:
                        desc.append(slot_dicts[2][slots[i]])
                elif i == 7:
                    desc.append(str(slots[i]))
                else:
                    for suf in slots[11]:
                        desc.append('%s_%s' % (slot_dicts[i][suf[1]], slot_dicts[i][suf[0]]))
            except:
                print('No entry found for slot %s: %s' % (i, slots[i]))
    return '-'.join(desc)

def describe(word):
    slots = analyze_word(word)
    
    if slots['type'] == 'formative':
        return describe_formative(slots)
    
    else:
        return 'TODO'
    
if __name__ == '__main__':
    init()
    print('Type \'quit\' to quit.')
    while True:
        text = input('Type a sentence: ')
        if text == 'quit':
            break
        words = text.split()
        for word in words:
            if not word: continue
            print('%s: %s' % (word, describe(word)))
