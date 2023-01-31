import numpy as np
import random
import string
import sys
import math

target="to be or not to be"
mutation_rate=2
max_population=1000
sexpool=[]
X=[]
Xrate =[]
Min=0
Max=0



def get_random_string(length):
    letters = string.printable
    x=0
    result_str = ''.join(random.choice(letters) for x in range(length))
    X.append(result_str)
    
def word_matching(word="                  ") :
    score=0
    for i in range(len(target)):
        if(target[i]==word[i]):
            score+=1
    rate=((score)/len(target))
    rate=pow(rate,2)
    Xrate.append(rate)

def calcfitness():
    total=0
    Max=max(Xrate)
    Min=min(Xrate) 
    for i in range(len(Xrate)):
        if(Max==Min):
            Xrate[i]=0
        else:
            Xrate[i]=(Xrate[i]-Min)/(Max-Min)
    
    
def natural_Selection():
    besafe=0
    while(True):
        gene =math.floor(random.randint(0,max_population-1))
        gene2 =random.randint(0,100)
        parent=X[gene]
        if(gene2<(Xrate[gene]*100)):
            return parent
        besafe+=1
        if(besafe>1000):
            return parent
      
           
        
def crossover(mom,dad):
    child=""
    for i in range (len(target)):
        gene =random.randint(0,1)
        if(gene==0):
            child+=mom[i]
        elif(gene==1):
            child+=dad[i]
    return child



def mutate(chiled,chance):
    letters = string.printable
    latter=list(chiled)
    for i in range (len(target)):
        mutation =random.randint(chance,100)
        if(mutation==100):
            s=random.choice(letters)
            latter[i]=s
    child=''.join(latter)
    return child
     

   
for i in range (max_population):
     get_random_string(len(target))
for i in range(1000):
    print(i)
    print(X[0]) 
    for i in range (len(X)):
        y=len(target)
        word_matching(X[i])
    calcfitness()
    sexpool.clear()
    for i in range (max_population):
        mom =natural_Selection()
        dad =natural_Selection()
        child=crossover(mom,dad)
        if(child==target):
            print(child)
            sys.exit() 
        child=mutate(child,mutation_rate)
        
        sexpool.append(child)
    Xrate.clear()
    X=sexpool.copy()
    Min=0
    Max=0
    






