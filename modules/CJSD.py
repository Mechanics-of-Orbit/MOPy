from math import *
class JulianDay():

    @classmethod
    def tb_method(cls,year, month, day, hour, minutes, seconds, accuracy):
        if 1901 <= year <= 2099:
            JDN = 367 * year + int((7 * (year + int((month + 9)/12)))/4) + int(275 * month/9) + day + 1721013.5
            UT = hour + round((minutes/60), accuracy) + round((seconds/3600), accuracy)
            JD = JDN + UT/24
            return [JDN, JD]
        else:
            #manju you can set limits when this option is selected between 1901 and 2099
            print("Not Possible from this method")

    @classmethod
    def julian_day(cls,year, month, day, hour, minutes, seconds, accuracy,type_of_calender):
        if type_of_calender == "Gregorian":
            #julian day number from Gregorian calender date
            JDN = int((1461 * (year + 4800 + (month - 14)/12))/4) + int((367 * month - 2 - 12 * ((month - 14)/12))/12) - int((3 * ((year + 4900 + (month - 14)/12)/100))/4) + day - 32075
        elif type_of_calender == "Julian":
            #julian day number from julian calender date
            JDN = 367 * year - int((7 * (year + 5001 + (month - 9)/7))/4) + int((275 * month)/9) + day + 1729777
        #JDN to JD
        JD = JDN + round(((hour - 12)/24),accuracy) + round((minutes/1440), accuracy) + round((seconds/86400), accuracy)
        return [JDN, round(JD, accuracy)]


if __name__ == '__main__':        
    a = JulianDay.tb_method(2004,5,12,14,45,30,3)
    print(a)
    


