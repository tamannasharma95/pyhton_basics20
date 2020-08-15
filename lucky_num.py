#Initiate a dictionary
numbers={ 
    0:'Your daya will be awesome',
    1:'You will get an opprtunity today,dont miss it',
    2:'Day is full of perils',
    3:'You will get a lottery today',
    4:'Dont go out today,its risky for you',
    5:'This day will bring something best for you',
    6:'You will meet your bf today',
    7:'You will have a horrible fight today',
    8:'You will get married soon',
    9:'You are about to become Data Scientist',
    10:'You are born to rule the world'
}

GREETINGS='Please enter a number: '
Lucky_Prid= int(input(GREETINGS))
print(Lucky_Prid)
print(type(Lucky_Prid))
print('Your lucky prediction for today is: ' + numbers.get(Lucky_Prid,'Sorry wrong option selected'))
print('Thank you for visiting us')