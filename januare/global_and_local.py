def becon():
    spam = 99 #создает локальную переменную
    print(spam) #99
    
spam = 43 #global
print(spam)#43

becon() #99
print(spam) #43