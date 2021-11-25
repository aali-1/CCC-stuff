import sys
input = sys.stdin.readline
class Section:
    def __init__(self):
        self.L=0
        self.M=0
        self.S=0
    def add(self,novel):
        if novel == 'L':
            self.L+=1
        if novel == 'S':
            self.S+=1
        if novel == 'M':
            self.M+=1
novels = input()
all = Section()

for novel in novels:
    all.add(novel)

L=Section()
M=Section()
S=Section()
u=0

for i in range(all.L):
    L.add(novels[u])
    u+=1
for i in range(all.M):
    M.add(novels[u])
    u+=1
for i in range(all.S):
    S.add(novels[u])
    u+=1

print(L.M + L.S + M.L + M.S - min(M.L, L.M))