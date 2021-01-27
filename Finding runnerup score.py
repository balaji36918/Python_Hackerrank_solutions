valuesno = int(input())
scores = map(int,input().split())
scorelist = list(scores)

print(max([x for x in scorelist if x!= max(scorelist)]))
