import sys
moves = []
while(True):
    move = sys.stdin.readline()[:-1]
    if move == "SCHOOL":
        break
    moves.append(move)
for x in range(len(moves)-1,-1,-1):
    if moves[x] in ['L','R']:
        direction = 'LEFT' if moves[x]=='R' else 'RIGHT'
    else:
        print(f"Turn {direction} onto {moves[x]} street.")
print(f"Turn {direction} into your HOME.")