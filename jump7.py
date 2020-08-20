a = 0
while a < 100:
    a += 1
    if a % 7 == 0:
        continue
    elif ( a + 3 ) % 10 == 0:
        continue
    elif a < 80 and a >=70:
        continue
    else:
        print (a)

