from array import *


isnum = 0
x = input("Enter your message: ")[ :8]
if len(x) <= 8:
    x = x.upper()
    for letter in x:
         if letter.isalpha() or letter.isspace() != False:
            isnum = isnum+0
         else:
             isnum = isnum+1
else:
     print("Message too long keep it shorter!")
    
        

T = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
if isnum <1:
    z=0
    for letter in x:
        y=((ord(letter)))
        number = y
        string = f'{number:08b}'
        newString =(repr(string))[1:9]
        print(newString)
        y = 0
        for letter in newString:
            T[z][y] = letter
            print("y: " , y)    
            y = y+1
            
        print("z: " ,z)
        z=z+1

elif (isnum>0):
    print("Please do not include numbers!")

print(T)

label.configure(text=res)