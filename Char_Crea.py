def insert_dat(legal,index,message):
    """This function recieves a list of legal inputs,
     ,the index in character in which to input the data
     and the message to give the user as long as he/she is not finished.
     The function prompts the user for input and will continue so
     if the input is not in legal. If it is, the function will still
     give the user the oppurtunity to change the input"""

    flag = '0';  # A flag for the while loop
    while (flag == '0'):
        print(message);  # Prompting the user to choose a race using the letters in brackets
        character[index] = input();  # Getting input
        # Using the "not in" operation and the pre-prepared list to check whether the input is legal.
        if (character[index] not in legal):
            flag = '0';  # If the input is illegal continue in the loop (This line is a precaution)
            print("Illegal input. Try again")
        else:
            print("Do you want to change your mind? If so, enter (Y)");
            flagi = input();  # A flag to check if the user changed his/her mind
            if (flagi == 'y' or flagi == 'Y'):
                flag = '0';  # Again, Just in case
            else:
                flag = '1';


#The character contains a name[0], race[1],
#The "social" general status of the character[2]
#and The economical if the character is urban or rural
# (Noble and Tribal are assigned automatically)[3]
character=[0,'0','0','0'];

print("Choose Your name (maximum 24 characters)");
character[0]=input(); #Getting the name from the user
print(character[0]); #TEST printing the name
print("Hello {name}. How are you".format(name=character[0])); #TEST printing the name

#Prompting the user to choos his race
print("Choose Your race amongst the following:");
legal=['H','h','E','e','D','d','G','g','B','b','C']; #Creating a list of legal input for the races so that it can easily be checked whether the input is legal
#Will keep asking the user for a race as long as he didn't put a legal input. Using the insert_dat function
insert_dat(legal,1,"(H)uman, (E)lf, (D)warf, (G)nome, (B)asil, (C)P");
print(character[1]); #TEST printing the characer's race
legal=['N','n','U','u','R','r','T','t']; #Creating a list of legal input for soc so that it can easily be checked whether the input is legal
print("Choose Your background amongst the following:");
#Prompting the user to choose a soc using the letters in brackets.
#The list of legal inputs has changed
insert_dat(legal,2,"(N)oble, (U)rban, (R)ural, (T)ribal (or from a small community)");
print(character[2]); #TEST printing the characer's soc
if (character[2]=='N' or character[2]=='n'):
    character[3]='h'; #Giving Noble characters the "higher class" economical status
    print("Nobles are automatically rich (at least for now)");
elif (character[2]=='T' or character[2]=='t'):
    character[3] = 'l'; #Giving Tribal characters the "lower class" economical status
    print("Tribals are automatically from the lower economical class");
else:
    legal = ['H', 'h', 'M', 'm', 'L', 'l', 'S','s'];  # Creating a list of legal input for eco so that it can easily be checked whether the input is legal
    print("Choose Your background amongst the following:");
    # Prompting the user to choose a eco IF he chose urban or rural using the letters in brackets.
    # The list of legal inputs has changed
    insert_dat(legal, 3, "(H)igher class, (M)iddle class, (L)ower class, (S)treet urchin");
print(character[3]);  # TEST printing the characer's soc



