import random
import datetime


def randomizer(s):
    f = open("Rasgele.txt", "w")
    print("Zaman                       Olay Sırası                           Rasgele Sayı", file=f)
    a = 0
    while a < s:
        a = a + 1
        zaman = datetime.datetime.now()
        bugun = zaman.strftime("%Y.%M.%d %H:%M:%S")
        if a == 10:
            print(bugun, "                 ", a, "                                  ", random.randint(1, 100), file=f)
        else:
            print(bugun, "                 ", a, "                                   ", random.randint(1, 100), file=f)


randomizer(10)
