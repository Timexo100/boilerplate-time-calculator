def parse_time(time):
    #todo with regexp
    h, m  = time.split(":")

    try:
        m, ampm = m.split(" ")
        if ampm == 'PM':
            h = str(int(h) + 12)
        if h == '24':
            h = '00'
        t = h, m
    except:
        t = h, m
    return t

def to_minutes(time_tuple):
    result = int(time_tuple[0]) * 60 + int(time_tuple[1])
    return result

def hm_fmt(hm):
    if hm < 10:
        hm = "0{}".format(hm)
    return hm

def days_after(hours):
    dl = hours//24
    if dl == 1:
        return  " (next day)"
    if dl > 1:
        return " ({} days later)".format(dl)
    return ''

def add_time(start, duration, day=''):
    days = ['', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    arvo = 'AM'
    s = parse_time(start)
    d = parse_time(duration)

    sm = to_minutes(s)
    dm = to_minutes(d)
    iday = 0
    dl = 0

    rtime = sm + dm
    hafter = rtime//60
    mafter = rtime%60

    dafter = days_after(hafter)

    if day != '':
        iday = days.index(day.lower())
        df = hafter//24
        iday = iday + df
        if iday > 7:
            iday = iday%7
        dafter = ", {}{}".format(days[iday].capitalize(), dafter)
    if hafter > 24:
        hafter = hafter%24
    if hafter > 12:
        hafter = hafter - 12
        arvo = 'PM'
    if hafter == 12:
        arvo = 'PM'
    if hafter == 0:
        hafter = 12
        arvo = 'AM'

    mafter = hm_fmt(mafter)
    result = "{}:{} {}{}".format(hafter, mafter, arvo, dafter)
    return result