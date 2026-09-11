records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Ravi",   "Science", 65),
    ("Priya",  "Math",    55),
    ("Anjali", "Science", 88),
    ("Priya",  "Science", 40),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Priya",  "English", 33),
]
keys=("name","subject","marks")
relist=[]
for rec in records:
  values=rec
  redict=dict(zip(keys,values))
  relist.append(redict)

names=[]
subjects=[]
for re in relist:
    s=re['subject']
    n=re["name"]
    if n not in names:
        names.append(n)
    if s not in subjects:
        subjects.append(s)
print("---Student Averages---")
x=[]
for na in names:
    n=0
    t=0
    for re in relist:
        if na == re["name"]:
            t+=re["marks"]
            n+=1
            
    avg= lambda x,y: x/y
    average=round(avg(t,n),2)
    
    x.append((na,average))
x=sorted(x,key=lambda item:item[1],reverse=True)
for xx in x:
    print(f"{xx[0]:<8}:{xx[1]}")
print(f"\nTop Scorer:{x[0][0]}\n")
