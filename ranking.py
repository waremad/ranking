import random
import math

def two_ch(num,n):#二進数リストを十進数に
    n = n-1
    out = 0
    for i in num:
        out += i*(2**n)
        n = n - 1
    return out

def max_two(ls):#2のn乗の最大を返す
    n = 0
    while not(len(ls) <= 2**n-1):
        n += 1
    return n

log = {}
times = 0
task = 0.0
howlen = 0

def up_task():
    global task
    global howlen
    task += 1/(math.log2(howlen) * howlen)
    

def quest(A,B):#AとBの大きいほうを入力
    global log
    global times
    global task
    global howlen
    if (A,B) in list(log.keys()):
        up_task()
        return not(log[(A,B)])
    elif (B,A) in list(log.keys()):
        up_task()
        return not(log[(B,A)])
    IN = ""
    while not(IN in ["a","b","A","B"]):
        par = str((task*1000//1)/10)
        while len(par) < 4:
            par = "0" + par
        memo =par + "% " + "A:" + str(A) + ",B:" + str(B)
        IN = input(memo)
    times += 1
    if IN in ["a","A"]:
        out = False
    else:
        out = True
    log[(A,B)] = out
    up_task()
    return out

def add_ls(self,ls):#リストに要素を昇順になるように挿入
    global task
    global howlen
#    print("ls",self,ls)
    if ls == []:
#        print("[self]")
        return [self]
    n = max_two(ls)
    num = []
#    print("n,num",n,num)
    while not(len(num) >= n):
        p = two_ch(num+[1],n)
#        print("ls,p,slef",ls,p,self)
#        print("n,num",n,num)
        if len(ls) <= p:
            num.append(0)
        else:
            if quest(self,ls[p]):
                num.append(0)
            else:
                num.append(1)
#    print("insert",num,two_ch(num+[1],n),self)
    if quest(ls[two_ch(num,n)],self):
        ls.insert(two_ch(num,n)+1,self)
    else:
        ls.insert(two_ch(num,n),self)
    return ls

def txt2ls(path):#txtファイルからリストを返す
    out = []
    with open(path) as f:
        for now_line in f:
            out.append(now_line[:-1])
        out[-1] = now_line
    return out 

def randomls(ls):#リストをシャッフル
    out = []
    for i in ls:
        out.insert(random.randint(0,len(ls)),i)
    return out

theme = input("テーマ(theme)")
obje = txt2ls("in.txt")
obje = randomls(obje)
howlen = len(obje)
rank = []

print("より「" + str(theme) + "」である方を選べ")

for i in obje:
    task = len(rank) / howlen
    rank = add_ls(i,rank)

n = 1
rank = rank[::-1]
print("Ranking")
for i in rank:
    print(str(n)+". "+str(i))
    n += 1
print("times",times)