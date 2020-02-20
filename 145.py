def containsoddnos(n):
    n = str(n)
    for i in range(len(n)):
        if int(n[i])%2 == 0:
            return False
    return True

end = 10**9
count = 0
for i in range(1, end):
    if (str(i)[0] == "0") or (str(i)[-1] == "0"):
        continue
    if containsoddnos(i + int(str(i)[::-1])):
        #print(i)
        count += 1
#print("------------")
print(count)