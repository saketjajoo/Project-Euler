f = open("names.txt", "r+")
names = f.read().split(",")
names.sort()
final = 0
for i in range(len(names)):
    x = names[i]
    ans = 0
    for ele in x:
        if ord(ele)>=65 and ord(ele)<=90:
            ans += ord(ele)-64
    final += ans*(i+1)
print(final)
