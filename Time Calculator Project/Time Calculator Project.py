


def add_time(start, duration,weekday=None):
    parsed=start.split(":")
    duration=duration.split(":")
    raw_hr=int(duration[0])
    duration[0]=hour_12(duration)
    pars2=parsed[1].split(" ")
    mins=int(pars2[0])+int(duration[1])
    hours=int(parsed[0])+int(duration[0])
    total_hr=raw_hr

    if pars2[1] == 'PM' and int(parsed[0]) != 12:
        total_hr=total_hr+12+int(parsed[0])
    else:
        total_hr = total_hr + int(parsed[0])

    days=total_hr*60+mins
    period_cal=(days//60)%24
    days=days//1440

    if mins > 60:
        hours=hours+1
        mins=mins-60


    temp=[hours,mins]
    new_min =str(temp[1])

    if mins<10:
        new_min="0"+str(temp[1])
    if temp[0]>=12:
        temp[0]=hour_12(temp)
    period="AM"
    if period_cal >= 12:
        period="PM"
    new_time=str(temp[0])+":"+ new_min
    new_time = new_time + " "+period

    print(days)
    if weekday:
        day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        idx=day.index(weekday.title())
        new_day=day[(idx+days)%7]
        new_time+=f", {new_day}"





    if days==1:
         new_time = new_time + " (next day)"
    elif days>1 :
        new_time = new_time +f" ({days} days later)"
    return new_time

def hour_12(duration):
    temp = int(duration[0])
    if temp%12==0 :
       return 12
    else:
        return temp % 12


