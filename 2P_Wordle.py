#Cows and Bulls
import getpass

import enchant
dict = enchant.Dict("en_IN")

from random_word import RandomWords

r = RandomWords()
print()
print()
l = input("Player 1 , enter ur name")
m = input("Player 2 , enter ur name")


print()
print("Make sure the word u enter is only 4 letters")
print()

w = getpass.getpass("Player 1, enter your word : ")
z = getpass.getpass("Player 2, enter your word : ")

x = w.lower()
y = z.lower()

print("")
print("----------------------------")
print("")

lst1=[]
lst2=[]

if len(x) == 4 and len(y) == 4 and dict.check(x) is True and dict.check(y) is True:

    for i in range(0,4):
    
        a = ord(x[i])
        lst1.append(a)
        
        b = ord(y[i])
        lst2.append(b)
    

    g = input("Player 2 , enter your guess : ")
    h = input("Player 1 , enter your guess : ")
    
    lst3=[]
    lst4=[]

    for i in range(0,4):
        
        d = ord(g[i])
        lst3.append(d)
        
        e = ord(h[i])
        lst4.append(e)
        

    while x!=g and y!=h :  


        print("")
        print("--------")
        print(l)
        print("--------") 
        print("") 

        for i in range(0,4) :
            
            if ord(g[i]) in lst1 :
            
                if lst1[i]==lst3[i]:
                
                    
                    if i == 0 :
                        print(g[i],"- - -")
                    elif i == 1 :
                        print("-",g[i],"- -")
                    elif i == 2 :
                        print("- -",g[i],"-")
                    else :
                        print('- - -',g[i])
                    continue
                
                else :
                
                    print("The letter",g[i],"is in the word but not in the position as in the word u have given")
                    continue
        
        print("")
        print("--------")
        print(m)
        print("--------")
        print("")
        
        for i in range(0,4):
            
            if ord(h[i]) in lst2 :
            
                if lst2[i]==lst4[i]:
                        
                    if i == 0 :
                        print(h[i],"- - -")
                    elif i == 1 :
                        print("-",h[i],"- -")
                    elif i == 2 :
                        print("- -",h[i],"-")
                    else :
                        print('- - -',h[i])
                    continue
                else :
                
                    print("The letter",h[i],"is in the word but not in the position as in the word u have given")
                    continue
        
        if x!=g and y!=h :
            
            lst3.clear()
            lst4.clear()

            print("")
            print("----------------")
            print("")
            
            g = input("Player 2 , enter your guess : ")
            h = input("Player 1 , enter your guess : ")
            
            for i in range(0,4):
            
                d = ord(g[i])
                lst3.append(d)
        
                e = ord(h[i])
                lst4.append(e)
        
    if x==g or y==h :
        
        if x == g and y == h:

                print("")
                print("--------------------------")
                print("Both the players win")
                print("The words are ", g.upper() , "&" , h.upper())
                print("--------------------------")
                print("")
                print("The game has ended. Thank you for playing!!")
                print("")
                print("A project by Abhilash B N V S & Alwin Infanto")
                print("")
                print("")

        elif x == g  :

                print("")
                print("-------------------------")
                print("Player 2 wins!! Congo !!!")
                print("The word is ",g.upper())
                print("-------------------------")
                print("")
                print("The game has ended. Thank you for playing!!")
                print("")
                print("A project by Abhilash B N V S & Alwin Infanto")
                print("")
                print("")

        else :
                
                print("")
                print("-------------------------")
                print("Player 1 wins!! Congo !!!")
                print("The word is ",h.upper())
                print("-------------------------")
                print("")
                print("The game has ended. Thank you for playing!!")
                print("")
                print("A project by Abhilash B N V S & Alwin Infanto")
                print("")
                print("")

    else :
        print("Nothing")

elif len(x) == 4 and len(y) == 4 and dict.check(x) is False or dict.check(y) is False:
    print("It is not a valid word")
    print("The words entered were")
    print(x.upper() ,"and", y.upper())
    print()
    

else :
    
    print("It is not a 4 letter word")
    print("")
