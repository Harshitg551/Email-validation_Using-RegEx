import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"                                   # in regex ^ it is used for the first character and the condition 1 is to pass alphabets because number cannot be there
user_email=input('Enter your email id:  ')                                                   #[] is is use to pass a condition in regex
if re.search(email_condition,user_email):                                                    #if we created any string under regex we use \. to search it
    print("The Email you have entered is seems to be correct Awesome")                       # ? is is used to pass the condition one time only 
else:                                                                                        # If we want to search a special character into a string we use \w
    print("Wrong email")                                                                     #if we have to specify any condition over a certain location we use {cond)
                                                                                             # If we have to search for anything from behind we use $
#condition we need to satisfy that are:
#1. It should start with alphabets a-z
# 0-9 num
# . _ can be used 1 time
# @ also can be used 1 time 
# We have to check from backwords that "." will come at the position 2,3

#Finished
