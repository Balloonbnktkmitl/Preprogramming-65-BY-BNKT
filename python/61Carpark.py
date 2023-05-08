"""Prepro"""
def cald1(din, dout, tin, tout):
    "cal"
    day = dout-din
    hour = tout-tin
    if hour < 0:
        hour = hour + 24
        day = day-1
    if  hour <= 2:
        money = 0
    elif hour <= 12:
        money = 15*((hour))
    elif  hour < 24:
        money = 200
    if day == 0:
        print("%d day %d hour\n%d baht" %(day, hour, money))
    elif 1 <= day <= 6:
        print("%d day %d hour\n%d baht" %(day, hour, (money+(200*day))))
    elif day >= 7  and day <= 365:
        if day // 7 > 0:
            money = money+((200*day)-(300*(day//7)))
            if day >= 28:
                money = money-500
            print("%d day %d hour\n%d baht" %(day, hour, money))
def main():
    """61Carpark"""
    daycome = int(input())
    timecome = int(input())
    dayout = int(input())
    timeout = int(input())
    if1 = daycome <= 0 or dayout <= 0
    if2 = daycome > 365 or dayout > 365
    if3 = timecome >= 24 or timeout >= 24
    if4 = timecome < 0 or timeout < 0
    if5 = (daycome == dayout) and (timecome > timeout)
    if6 = (dayout - daycome < 0)
    if if1 or if2 or if3 or if4 or if5 or if6:
        print("error")
    else:
        cald1(daycome, dayout, timecome, timeout)
main()
