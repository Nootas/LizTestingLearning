import time

def Fahrenheit2Degree(fahrenheit):
    '''
    temperature transfer
    '''
    degree = round(5/9*(fahrenheit-32),2) #keep 2 decimal behand the point
    return degree


def GenerateWeaterTime(currenttime):
    '''
    form UNIX time to YYYY-MM-DD HH:MM:SS
    '''
    time_local = time.localtime(currenttime)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S',time_local)
    return timestamp
