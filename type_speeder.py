# Useing Time modules

from time import *
import random as rd

def mistake(paratest, usertest):
   error = 0
   for i in range(len(paratest)):
       try:
           if paratest[i] != usertest[i]:
               error = error + 1
       except:
           error = error + 1
   return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':
   while True:
        ck = input("Ready to Test : yes/no = ")
        if ck == 'yes':

            test =[ "This is right plateform on the practice will continue for the will present on time",
                "there for consider for the rules will conduct in college",
                    "This is right for the all common are will cover for the danger will opportunity"]
            test1 =rd.choice(test)
            print(" ***** Typing Speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Write Here :")
            time_2 = time()

            print("Speed : ", speed_time(time_1, time_2, testinput), "W/sec")
            print("Error : ", mistake(test1, testinput))


        elif ck == 'no':
            print("Thank You")
            break

        else:
            print("Wrong Input")