#마주보는 숫자의 곱의 합의 최대값 구하기
#n=ai의 요소 개수 m=bj의 요소 개수
s=0
r=0
T=int(input())
for test in range(T):
    M, N = map(int, input().split())
    a = map(int, input().split())
    li_a = list(a)
    b=map(int, input().split())
    li_b = list(b)

    for i in range(abs(M-N)+1):
        if N<M:
            k=s+int(li_a[i])*int(li_b[(i+i)//2])
            print(li_b[(i+i)//2])
            if k>r:
                r=k
        else:
            k=s+int(li_a[(i+i)//2])*int(li_b[i])
            print(li_b[(i+i)//2])
            if k>r:
                r=k
    print(f"#{test+1} {r}")

                