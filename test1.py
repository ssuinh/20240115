#마주보는 숫자의 곱의 합의 최대값 구하기
#n=ai의 요소 개수 m=bj의 요소 개수
s=0
r=0
k=0
v=0
T=int(input())
for test in range(T):
    N, M = map(int, input().split())
    a = map(int, input().split())
    li_a = list(a)
    b=map(int, input().split())
    li_b = list(b)

    if N<M:
        loop=N
    else:
        loop=M
    for p in range(abs(N-M)+1):
        k=0
        for i in range(loop):
            if N<M:
                s=int(li_a[i])*int(li_b[(i+p)])
                k+=s
            else:
                s=int(li_a[(i+p)])*int(li_b[i])
                k+=s
        if k>v:
            v=k
    print(f"#{test+1} {v}")