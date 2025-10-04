from random import *

user_pass = input("enter ur password: ")
crack = ""

password = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B' , 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0','!',
             '@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',':',';','"',
             "'",'<','>',',','.','?','/','1','2','3','4','5','6','7','8','9','0']
while (crack != user_pass):
    crack = ""
    for i in range(len(user_pass)):
        crack_letter = password[randint(0,61)]
        crack += crack_letter
    print(crack)

print("your password is: " + crack)