from math import *

def julian_day(year, month, day, hour=0, minutes=0, seconds=0, accuracy=3,type_of_calender='gregorian', method='default'):
    if method=='default':
        if type_of_calender.lower() == "gregorian":
            #julian day number from Gregorian calender date
            JDN = int((1461 * (year + 4800 + (month - 14)/12))/4) + int((367 * month - 2 - 12 * ((month - 14)/12))/12) - int((3 * ((year + 4900 + (month - 14)/12)/100))/4) + day - 32075
        elif type_of_calender.lower() == "julian":
            #julian day number from julian calender date
            JDN = 367 * year - int((7 * (year + 5001 + (month - 9)/7))/4) + int((275 * month)/9) + day + 1729777
        #JDN to JD
        JD = JDN + round(((hour - 12)/24),accuracy) + round((minutes/1440), accuracy) + round((seconds/86400), accuracy)
        return [JDN, round(JD, accuracy)]
    elif method == 'textbook_method':
        if 1901 <= year <= 2099:
            JDN = 367 * year + int((7 * (year + int((month + 9)/12)))/4) + int(275 * month/9) + day + 1721013.5
            UT = hour + round((minutes/60), accuracy) + round((seconds/3600), accuracy)
            JD = JDN + UT/24
            return [JDN, JD]
        else:
            return "Not Possible from this method"


if __name__ == '__main__':        
    a = julian_day(2004,5,12,14,45,30,3)
    print(a)
    


