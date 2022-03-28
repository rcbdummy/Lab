#4) id3 Program:
import pandas as pd
from collections import Counter
import math
tennis = pd.read_csv ('4.csv')
print ("|n given play tennis dataset:|n|n",tennis)
def entropy (alist):
    c=Counter(x for x in alist)
    instances=len(alist)
    prob= [x/instances for x in c.values()]
    return sum([-p*math.log(p,2)for p in prob])
def information_gain(d,split,target):
    splitting=d.groupby(split)
    n=len(d.index)
    agent=splitting.agg({target:[entropy,lambda x:len (x)/n]})[target]
    agent.columns=['Entropy','observations']
    newentropy = sum (agent ['Entropy']*agent['observations'])
    oldentropy=entropy(d[target])
    return oldentropy-newentropy
def id3 (sub,target,a):
    count=Counter(x for x in sub[target])
    if len(count)==1:
        return next(iter(count))
    else:
        gain = [information_gain(sub,attr,target)for attr in a]
        print ("Gain=",gain)                        
        maximum =gain.index(max(gain))
        best= a[maximum]
        print("Best attribute:",best)
        tree ={best:{}}
        remaining = [i for i in a if i!=best]
        
        for val,subset in sub.groupby(best):
            subtree=id3(subset,target,remaining)
            tree[best][val]=subtree
        return tree
names=list(tennis.columns)
print("List of Attributes:",names)
names.remove('PlayTennis')
print("predicting attributes :",names)

tree=id3(tennis,'PlayTennis',names)
print("\n\nThe resultent decision tree is \n")
print(tree)

'''output:

|n given play tennis dataset:|n|n      Outlook Temperature Humidity  Windy PlayTennis
0      Sunny         Hot     High  False         No
1      Sunny         Hot     High   True         No
2   Overcast         Hot     High  False        Yes
3      Rainy        Mild     High  False        Yes
4      Rainy        Cool   Normal  False        Yes
5      Rainy        Cool   Normal   True         No
6   Overcast        Cool   Normal   True        Yes
7      Sunny        Mild     High  False         No
8      Sunny        Cool   Normal  False        Yes
9      Rainy        Mild   Normal  False        Yes
10     Sunny        Mild   Normal   True        Yes
11  Overcast        Mild     High   True        Yes
12  Overcast         Hot   Normal  False        Yes
13     Rainy        Mild     High   True         No
List of Attributes: ['Outlook', 'Temperature', 'Humidity', 'Windy', 'PlayTennis']
predicting attributes : ['Outlook', 'Temperature', 'Humidity', 'Windy']
Gain= [0.2467498197744391, 0.029222565658954647, 0.15183550136234136, 0.04812703040826927]
Best attribute: Outlook
Gain= [0.01997309402197489, 0.01997309402197489, 0.9709505944546686]
Best attribute: Windy
Gain= [0.5709505944546686, 0.9709505944546686, 0.01997309402197489]
Best attribute: Humidity


 the resultent decision tree is 

{'Outlook': {'Overcast': 'Yes', 'Rainy': {'Windy': {False: 'Yes', True: 'No'}}, 'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}}}}
'''