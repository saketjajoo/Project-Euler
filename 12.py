def noofdiv(n):
    ans = 0
    for i in range(1,int(n//2)):
        if n%i == 0:
            ans+=1
    return ans

trianglenos = []
for i in range(1, 1000000):
    trianglenos.append(int(i * (i + 1) / 2))

for ele in trianglenos:
    if noofdiv(ele)>=500:
        print(ele)
        break
