from random import *
import os,sys,string,time,pyautogui

class Nouns:
    NounList = []
    nList = open(r'Lists\NounList.txt')
    for line in nList:
        if (len(line)>3):
            NounList.append(line.replace('\n',''))
    nList.close()
            
    ListLen = len(NounList)
    def rNoun():
        rng = randint(0,Nouns.ListLen - 1)
        return str(Nouns.NounList[rng])

    
class Adj:
    AdjList = []
    nList = open(r'Lists\AdjectiveList.txt')
    for line in nList:
        if (len(line)>3):
            AdjList.append(line.replace('\n',''))
    nList.close()
    
    ListLen = len(AdjList)
    def rAdj():
        rng = randint(0,Adj.ListLen - 1)
        return str(Adj.AdjList[rng])

    
class Verbs:
    VerbList = []
    nList = open(r'Lists\VerbList.txt')
    for line in nList:
        if (len(line)>3):
            VerbList.append(line.replace('\n',''))
    nList.close()
    
    ListLen = len(VerbList)
    def rVerb():
        rng = randint(0,Verbs.ListLen - 1)
        return str(Verbs.VerbList[rng])

class BingURL:
    URL = r'https://www.bing.com/search?q='

class BingSearchWL:
    def BingAutoSearch(bLoops = 50):
        for i in range(0,bLoops):
            
            pyautogui.hotkey(r'ctrl','l')
            time.sleep(1)
            pyautogui.hotkey(r'ctrl','a')
            time.sleep(1)
            pyautogui.write(BingURL.URL  + BingSearch.BingStringConcat() , interval=0.075)
            pyautogui.press(r'enter')
            time.sleep(7)

        print(r'AutoSearch Complete')
        

    def BingStringConcat():
        OutString = Adj.rAdj()
        OutString += ' ' + Nouns.rNoun()
        OutString += ' ' + Verbs.rVerb()
        OutString += ' ' + Adj.rAdj()
        OutString += ' ' + Nouns.rNoun()
        OutString = OutString.replace(r'  ',r' ').replace(r'  ',r' ')
        print(str(OutString))        
        return OutString

print('\n-------------------------------------\n_BingSearchWordlist Loaded\n-------------------------------------\n')
