import sys

sys.stdin = open("_신용카드만들기1.txt")
T = int(input()) #테스트케이스 수
t = 15
sum_ = 0

for i in range(1,T+1):
    list_ = [0 for i in range(t)]
    list_ = list(map(int, input().split()))
    for j in range(t):#0,1,2,3...,13,14
        if j % 2 == 0:
            sum_ += list_[j]*2 #list_[]
        else :
            sum_ += list_[j]
    #print(sum_)
    N = 10 - int(str(sum_)[-1])
    if N != 10:
        print(f'#{i} {N}')
    elif N == 10:
        print(f'#{i} 0')
    sum_ = 0