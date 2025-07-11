# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string

def randomchar():
    ranl=""
    for i in range(0,3):
        ranl+=random.choice(string.ascii_letters)
    return ranl
c=int(input("want to code(0) or decode(1)?"))
if(c==0):
    str=input("enter string: ")
    print(str)
    coding=True
else:
    dec=input("enter string: ")
    coding=False
strr=""
if(coding):
    if(len(str)<=3):
        dec=str[::-1]
        # print("h")
    else:
        dec=randomchar()+str[1:len(str)]+str[0]+randomchar()
        # print("hgf")
    print(dec)

if(not coding):
    if(len(dec)<=3):
        strr=dec[::-1]
        # print("h")
    else:
        strr=dec[3:len(dec)-3]
        # print(strr[len(str)-1])
        # print(strr[0:len(str)-1])
        strr=strr[len(strr)-1]+strr[0:len(strr)-1]
        # print("hgf")
    print(strr)