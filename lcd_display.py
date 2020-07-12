#-----------------------------------------------------
#with this loop the string that is displayed on the top, will start at the beginning and when
#it comes to the end, it will wait 1.5 sec and will reset, wait 1.5sec and scroll again to the end

import lcddriver
import time

display = lcddriver.lcd()
#string1 will be displayed at the top of the display. CAN BE MORE THAN 16 CHAR LONG!
string1 = "Please insert the coins into the coin slot!"
#string2 will be displayed at the bottom of the dispaly. WILL DISPLAY ONLY UP TO 16 CHAR
string2 = "Value: 0.00$"
#create two variables, which will be used for slicing the string
x1=0
y1=16



try:
    #create while True: loop, inside of a try:
    while True:
        if x1 == 0: #create if statement if x1 is 0, so if the beginning of string slice is 0
            print("Writing to display - beginning")
            display.lcd_display_string(string1[x1:y1], 1)   #display string1 at the top (1 is for top)
            display.lcd_display_string(string2, 2) #display string2 at the bottom (2 is for bottom)
            x1 += 1 #add 1 to x1 variable
            y1 += 1 #add 1 to y1 variable
            time.sleep(1.5) #wait for 1.5sec

        elif y1 < len(string1): #if y1 (end of string slice) is lower than whole length of string1
            print("Writing to display")
            display.lcd_display_string(string1[x1:y1], 1)   #display string1 at the top with current x1 and y1 value for string slice
            x1 += 1 #and again add 1 to x1
            y1 += 1 #and 1 to y1
            time.sleep(0.3) #wait for 0.3sec, so technically, scrolling will have 0.3sec delay
            #if you want display, to be more slower, lower the value in time.sleep from 0.3 to 0.5 or higher,
            #or if you want it to be faster, lower from 0.3 to 0.15 for example

        elif y1 == len(string1):    #when y1 (end of string slice) is same as length of string1 (so when it reaches the end)
            print("Writing to display - end")
            display.lcd_display_string(string1[x1:y1], 1) # display string1
            x1 = 0  #reset the value of x1 variable to 0
            y1 = 16 #reset the value of y1 variable to 16
            time.sleep(1.5) #wait for 1.5sec and reset the string1 to the beginning


except KeyboardInterrupt: # If there is a KeyboardInterrupt clear the display
    print("Cleaning up!")
    display.lcd_clear()



##--------------------------------------------------------------------



# #IF YOU WANT TO INFINITE SCROLL THE TOP SIDE OF SCREEN
# import lcddriver   
# import time


# display = lcddriver.lcd()

# #string variable is what top part of the lcd screen will display
# #it can contain MORE THAN 16 characters
# string = "Please insert the coins into the coin slot!"
# #string2 variable is what bottom part of the lcd screen will display
# #it will show ONLY UP TO 16 characters
# string2 = "Value: 0.00$"

# #to add 16 characters (white spaces) at the beginning and 16 at the end of the string, use this code:
# string_length=len(string)+32    #we make new variable string_length, which has the length of variable string + 32 
# string1=string.center(string_length)    #we center variable string, into variable string_length,
# #which means we added 16 spaces at the beginning and 16 white spaces at the end of string

# #we create 2 variables, which we will use for slicing string
# x1=0
# y1=16




# try:
#     #we create while True: loop inside of a try:
#     while True:
#         if x1 == 0:    #if statement, if x1(beginning of string slice) is equal to 16, which is
#             print("Writing to display - beginning")
#             display.lcd_display_string(string1[x1:y1], 1)   #display string1 to the code... 1 means on the top side, 2 on the bottom
#             display.lcd_display_string(string2, 2)  #display string2 on the bottom (2)
#             x1 += 1 #than add 1 to variable x1
#             y1 += 1 #same, add 1 to variable y1


#         elif y1 < len(string1): #if y1 (end of string slice) is lower than length of string1 
#             print("Writing to display")
#             display.lcd_display_string(string1[x1:y1], 1) # display string1 on top line
#             x1 += 1 #add 1 to x1
#             y1 += 1 #add 1 to y1
#             time.sleep(0.15)    #wait for 0.15 second

#         elif y1 == len(string1):    #if y1 is equal to whole length of string1
#             print("Writing to display - end")
#             display.lcd_display_string(string1[x1:y1], 1) # same as allways, display string1 on top
#             x1 = 0  #reset x1 to 0 (technically first of the 16 white spaces)
#             y1 = 16 #reset y1 to 16 (technically 16th or last white space before the string starts)
               


# except KeyboardInterrupt: # If there is a KeyboardInterrupt, clear lcd display
#     print("Cleaning up!")
#     display.lcd_clear()
