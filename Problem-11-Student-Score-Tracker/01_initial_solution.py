records = [
    ("Ravi",  "Math",    80),
    ("Ravi",  "Science", 85),
    ("Ravi",  "English", 90),
    ("Priya", "Math",    25),
    ("Priya", "Science", 30),
    ("Priya", "English", 20),
    ("Kumar", "Math",    10),
    ("Kumar", "Science", 15),
    ("Kumar", "English", 12),
]
reclist=[]
keys=('name','subject','marks')
for rec in records:
    values=rec
    recdict=dict(zip(keys,values))
    reclist.append(recdict)
    
SUB=[]
NAM=[]
for rec in reclist:
    na=rec['name']
    su=rec['subject']
    if su not in SUB:
        SUB.append(su)
    if na not in NAM:
        NAM.append(na)
def ca(t,n):
    return t/n
print("--- Student Averages ---")
X=[]
TM=0
TP=''
for NA in NAM:
    t=0
    n=0
    for rec in reclist:
        if NA == rec['name']:
            t+=rec['marks']
            n+=1
    avg=ca(t,n)
    average=round(avg,2)
    if TM < average:
        TM=average
        TP=NA
    X.append([NA,average])
    X=sorted(X,key= lambda X:X[1],reverse='True')
for x in X:
    print(f"{x[0]:<8}:{x[1]}")
print(f"\nTop Scorer:{TP}({TM})\n")
 
print("--- Subject Averages ---")
Y=[]
LM=None
LP=''
for SU in SUB:
    t=0
    n=0
    for rec in reclist:
        if SU == rec['subject']:
            t+=rec['marks']
            n+=1
    avg=ca(t,n)
    average=round(avg,2)
    if LM is None or LM > average:
        LM=average
        LP=SU
    Y.append([SU,average])
    Y=sorted(Y,key= lambda Y:Y[1],reverse='True')
for y in Y:
    print(f"{y[0]:<8}:{y[1]}")
print(f"\nHardest Subject:{LP}({LM})\n")
Z=[] 
for x in X:
    if x[1] < 40:
        Z.append(x)
U=[]
for x in X:
    if x[1] >= 40: 
        U.append(x)
print("\n--- Passed Students (Average >= 40) ---")
if not U:
    print("None")
else:
    for u in U:
        print(f"{u[0]:<8}:{u[1]}")
print("\n--- Failed Students (Average < 40) ---")
if not Z:
    print("None")
else:
    for z in Z:
        print(f"{z[0]:<8}:{z[1]}")
    
