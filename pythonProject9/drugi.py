sec = input("seconds: ")
sec = int(sec)
if sec < 0 or sec > 86400:
    print("wrong")
else:
    hh = sec // 3600
    sec = sec - (hh * 3600)
    mm = sec // 60
    sec = sec - (mm * 60)
    ss = sec
    print(str(hh) + " hours: " + str(mm) + " minutes: " + "and seconds: " + str(ss))
