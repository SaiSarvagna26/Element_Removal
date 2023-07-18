A=list(map(int,input().split()))
sort_rev=sorted(A,reverse=True)
cost=0
for i in range(len(A)):
    cost+=A[i]*(i+1)
print(cost)