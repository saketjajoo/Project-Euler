ans = 0

for i in range(1406357289,9999999999):
    if "".join(sorted(str(i))) == "0123456789":
        no = []
        for j in range(1, 8):
            temp = ""
            temp += str(i)[j] + str(i)[j+1] + str(i)[j+2]
            no.append(int(temp))
        if no[0]%2 == 0 and no[1]%3 == 0 and no[2]%5 == 0 and no[3]%7 == 0 and no[4]%11 == 0 and no[5]%13 == 0 and no[6]%17 == 0:
            ans += i

print(ans)