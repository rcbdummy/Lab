#3) Candidate elimination 

import csv
a=[]
csvfile=open('3.csv','r')
reader=csv.reader(csvfile)
for row in reader:
    a.append(row)
    print(row)
num_attributes=len(a[0])-1
print("Initial hypothesis is: ")
s=['0']*num_attributes
g=['?']*num_attributes
print("the most specific: ",s)
print("the most general: ",g)
for j in range(0,num_attributes):
    s[j]=a[0][j]
print("the candidate algorithm\n")
temp=[]
for i in range (0,len(a)):
    if(a[i][num_attributes]=='Yes'):
      for j in range(0,num_attributes):
          if(a[i][j]!=s[j]):
              s[j]='?'
      for j in range(0,num_attributes):
          for k in range(1,len(temp)):
              if temp[k][j]!='?' and temp[k][j]!=s[j]:
                  del temp[k]
      print("for instance{0} the hypothesis is s{0}",format(i+1),s)
      if(len(temp)==0):
          print("for instance{0} the hypothesis is g{0}",format(i+1),g)
      else:
          print("for instance{0} the hypothesis is s{0}",format(i+1),temp)
    if(a[i][num_attributes]=='No'):
        for j in range(0,num_attributes):
            if(s[j]!=a[i][j] and s[j]!='?'):
                g[j]=s[j]
                temp.append(g)
                g=['?']*num_attributes
        print("for instance {0} the hypothesis is s{0}",format(i+1),s)
        print("for instance {0} the hypothesis is s{0}",format(i+1),temp)

'''output:

['sunny ', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
['sunny ', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Same', 'No']
['sunny ', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
Initial hypothesis is: 
the most specific:  ['0', '0', '0', '0', '0', '0']
the most general:  ['?', '?', '?', '?', '?', '?']
the candidate algorithm

for instance{0} the hypothesis is s{0} 1 ['sunny ', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
for instance{0} the hypothesis is g{0} 1 ['?', '?', '?', '?', '?', '?']
for instance{0} the hypothesis is s{0} 2 ['sunny ', 'Warm', '?', 'Strong', 'Warm', 'Same']
for instance{0} the hypothesis is g{0} 2 ['?', '?', '?', '?', '?', '?']
for instance {0} the hypothesis is s{0} 3 ['sunny ', 'Warm', '?', 'Strong', 'Warm', 'Same']
for instance {0} the hypothesis is s{0} 3 [['sunny ', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]
for instance{0} the hypothesis is s{0} 4 ['sunny ', 'Warm', '?', 'Strong', '?', '?']
for instance{0} the hypothesis is s{0} 4 [['sunny ', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]
            '''
    
          