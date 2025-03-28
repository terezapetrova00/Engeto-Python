"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Petrova
email: tereza.petrova00@gmail.com
"""
approved_users = {    
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

text_1 = ('''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''')
text_2 = ('''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''')
text_3 = ('''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''')

texts = [text_1, text_2, text_3]

username = input("Zadejte prihlasovaci jmeno: ")
password = input("Zadejte heslo: ")

if username in approved_users and approved_users[username] == password:
    print("username:",username)
    print("password:",password)
    print("----------------------------------------")
    print("Welcome to the app, ", username)
    print("We have 3 texts to be analyzed.")
    print("----------------------------------------")

    try:

        choice = int(input("Enter a number btw. 1 and 3 to select: ")) 
        print("----------------------------------------") 
        if 1 <= choice <= 3:
            selected_text = texts[choice - 1]            
        else:
            print ("Invalid selection. Please enter a number between 1 and 3.") 
            exit() 
    except ValueError:
        print("Invalid input. Please enter a numeric value.") 
        exit()  

    
    words = selected_text.split()
    word_count = len(words) 
    title_case_count = sum(1 for word in words if word.istitle())  
    uppercase_count = sum(1 for word in words if word.isupper())  
    lowercase_count = sum(1 for word in words if word.islower())  
    number_list = [int(word) for word in words if word.isdigit()]  
    number_count = len(number_list)  
    number_sum = sum(number_list)  

    print("There are ", word_count, "words in the selected text.")
    print("There are ", title_case_count, "titlecase words.")
    print("There are ", uppercase_count, "uppercase words.")
    print("There are ", lowercase_count,"lowercase words.")
    print("There are ", number_count, "numeric strings.")
    print("The sum of all the numbers ", number_sum)   
    print("----------------------------------------")
    print ("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")

    word_lengths = {}
    for word in words:
        length = len(word.strip(".,!?"))
        word_lengths[length] = word_lengths.get(length, 0) + 1

    for length, count in sorted(word_lengths.items()):
        print("{:2} | {} | {}".format(length, '*' * count, count))

else:
    print("username:",username) 
    print("password:",password)
    print("unregistered user, terminating the program..")
    
