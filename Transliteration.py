import gspread
import ast

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("Lyrics")

wks = sh.worksheet("Sheet1")

currdict=wks.cell(1, 1).value
rowno=int(currdict[1:])+1
di=wks.acell(currdict).value
c=ast.literal_eval(di)

l=[]
l1=[]
a=''
print("Enter the Tamil Text")
while a!="@@":
    a=input()
    l.extend(a.split())
    l1.append(a)

l.pop()
l1.pop()
b=list(set(l))
print("Enter the Tanglish Text for")
for i in b:
  if i not in c.keys():
    print(i,end=": ")
    d=input()
    c[i]=d

print("-----------------\n COPY THE LYRICS \n-----------------")
e=0
for i in l1:
    print("\n",l1[e],sep="")
    for j in i.split():
        print(c[j].capitalize(), end=" ")
    e+=1


print("\n\n-----------------\n ")
wks.update('A1','A'+str(rowno))
wks.update('A'+str(rowno),str(c))
print("\n DICTIONARY: ",c)
print("Updated Dictionary")
