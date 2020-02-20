for i in range(100000, 999999):
    x = i
    x2 = i*2
    x3 = i*3
    x4 = i*4
    x5 = i*5
    x6 = i*6

    if "".join(sorted(str(x))) == "".join(sorted(str(x2))) == "".join(sorted(str(x3))) == "".join(sorted(str(x4))) == "".join(sorted(str(x5))) == "".join(sorted(str(x6))):
        print(x)
        break