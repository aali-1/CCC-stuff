import sys
input = sys.stdin.readline
distance = int(input())
n = int(input())
clubs = [int(input()) for x in range(n)]
positions = [5281 for x in range(distance+1)]
positions[0] = 0
for k in range(distance+1):
  for j in range(len(clubs)):
    if k + clubs[j] <= distance: 
      if positions[k] + 1 <positions[k+clubs[j]]:
        positions[k+clubs[j]] =positions[k]+1
if positions[distance] < 5281:
    print(f"Roberta wins in {str(positions[distance])} strokes.")
else:
    print("Roberta acknowledges defeat.")