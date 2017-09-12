#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdafx.h>

#define skip printf("\n");

struct character {
	char race; //The character's name
	int soc; //The "social" general status of the character
	int eco; //The economical if the character is urban or rural (Noble and Tribal are assigned automatically)
};

//Get the character's race from the user.
char get_race(char race);

//Get the character's "social" from the user.
char get_soc(char soc);

//Get the character's "eco" from the user. This time taking a previous input (soc) into account
char get_eco(char eco, char soc);

//In case the user changed his mind about something, this function will tell the calling function that
char changeofheart();

/*
The option to change your mind now works as it should.



*/
//IMPORTANT: Remember when getting a character to use a dummy char variable to "absorb" the \n characater, to prevent "pollution" of the input stream
//NEED TO ADD NAME OPTION NEXT. And afterwards we'll see
/*NEED TO ADD LATER: 
Writing a character struct to a file,
Adding another Program which can read a character struct from a file
Addin a program which the other program can use, containing all sort of functions, like getting a character's stats, changing them etc.

*/
int main(int argc, char* argv[])
{
	char soc, eco; //The "social" general status of the character, and the economical if the character is urban or rural (Noble and Tribal are assigned automatically)
	char race; //A race for the character.
	char name[25]; //The character's name.
	printf("Choose Your race amongst the following:");
	skip;
	race = get_race('0'); //Getting the character's race using the get_race function
	printf("Choose Your background amongst the following:");
	skip;
	soc = get_soc('0'); //Getting the character's soc using the get_soc function
	eco = get_eco('0', soc); //Getting the character's eco using the get_eco function which also takes the character's soc into account
	skip;

    

	//system("pause");
}


//Get the character's race from the user.
char get_race(char race)
{
	char blank; //blank is an improvised way of dealing with the \n problem.
	//A do while loop to make sure we end up with a legal input. For the race input.
	do
	{
		printf("(H)uman, (E)lf, (D)warf, (G)nome, (B)asil, (C)P"); //Prompting the user to choose a race using the letters in brackets
		skip;

		race = getc(stdin); //Getting an input for he character's race
		blank = getc(stdin); //"Absorbing" the \n character so that if the user failed he won't get bla illegal bla and the prompt twice.
		
		//A switch-case check to see whether the user put in legal input. If he did, he gets a message about it and the option to change his choice
		//Otherwise he is told the imput was illegal and get sent back to provide input
		switch (race)
		{

		case 'b':
		case 'B':
			printf("You have chosen the Basil race.");
			skip;
			break;

		case 'h':
		case 'H':
			printf("You have chosen the Human race.");
			skip;
			break;

		case 'e':
		case 'E':
			printf("You have chosen the Elven race.");
			skip;
			break;

		case 'd':
		case 'D':
			printf("You have chosen the Dwarven race.");
			skip;
			break;

		case 'g':
		case 'G':
			printf("You have chosen the Gnome race.");
			skip;
			break;

		case 'c':
		case 'C':
			printf("You have chosen the CP race.");
			skip;
			break;

		default:
			race = '0';
			printf("Illegal input. Try again.");
			skip;
		}
		//If the user put a legal input (meaning race is not '0') will send him to the changeofheart function. Reusing blank for saving memory
		if (race != '0')
			blank = changeofheart();
		//If he changed his mind, will set race to 0 so that the do while will continue
		if (blank == '0')
			race = '0';
	} while (race == '0');
	return race;
}

//Get the character's soc from the user.
char get_soc(char soc)
{
	char blank; //blank is an improvised way of dealing with the \n problem.

	//A do while loop to make sure we end up with a legal input. For the soc input.
	do
	{
		printf("(N)oble, (U)rban, (R)ural, (T)ribal (or from a small community)"); //Prompting the user to choose a soc using the letters in brackets
		skip;

		soc = getc(stdin); //Getting an input for he character's race
		blank = getc(stdin); //"Absorbing" the \n character so that if the user failed he won't get bla illegal bla and the prompt twice.
		
		//A switch-case check to see whether the user put in legal input. If he did, he gets a message about it and the option to change his choice
		//Otherwise he is told the imput was illegal and get sent back to provide input
		switch (soc)
		{

		case 'n':
		case 'N':
			printf("You have chosen the Noble background. Nobles are automatically rich (at least for now)");
			skip;
			break;

		case 'u':
		case 'U':
			printf("You have chosen the Urban background.");
			skip;
			break;

		case 'r':
		case 'R':
			printf("You have chosen the Rural background.");
			skip;
			break;

		case 't':
		case 'T':
			printf("You have chosen the Tribal (or small community) background. They are automatically from the lower economical class");
			skip;
			break;

		default:
			soc = '0';
			printf("Illegal input. Try again.");
			skip;
		}
		//If the user put a legal input (meaning race is not '0') will send him to the changeofheart function. Reusing blank for saving memory
		if (soc != '0')
			blank = changeofheart();
		//If he changed his mind, will set race to 0 so that the do while will continue
		if (blank == '0')
			soc = '0';
	} while (soc == '0');
	return soc;
}

//Get the character's "eco" from the user. This time taking a previous input (soc) into account
char get_eco(char eco, char soc)
{
	//A switch case to check whether the character is noble or tribal and then assigning the appropriate values.
	//Otherwise it goes on.
	switch (soc)
	{

	case 'n':
	case 'N':
		printf("Nobles are automatically rich (at least for now)");
		skip;
		return 'h';

	case 't':
	case 'T':
		printf("Tribals are automatically from the lower economical class");
		skip;
		return 'l';

	default:
		break;

	}


	char blank; //blank is an improvised way of dealing with the \n problem.
	printf("Choose Your economical background amongst the following:");
	skip;

	//A do while loop to make sure we end up with a legal input. For the eco input.
	do
	{
		printf("(H)igher class, (M)iddle class, (L)ower class, (S)treet urchin"); //Prompting the user to choose an economical level using the letters in brackets
		skip;

		eco = getc(stdin); //Getting an input for he character's race
		blank = getc(stdin); //"Absorbing" the \n character so that if the user failed he won't get bla illegal bla and the prompt twice.

		//A switch-case check to see whether the user put in legal input. If he did, he gets a message about it and the option to change his choice
		//Otherwise he is told the imput was illegal and get sent back to provide input
		switch (eco)
		{

		case 'h':
		case 'H':
			printf("You have chosen the higher class");
			skip;
			break;

		case 'm':
		case 'M':
			printf("You have chosen the middle class.");
			skip;
			break;

		case 'l':
		case 'L':
			printf("You have chosen the lower class");
			skip;
			break;		

		case 's':
		case 'S':
			printf("You have chosen thes street urchin");
			skip;
			break;

		default:
			eco = '0';
			printf("Illegal input. Try again.");
			skip;
		}
		//If the user put a legal input (meaning race is not '0') will send him to the changeofheart function. Reusing blank for saving memory
		if (eco != '0')
			blank = changeofheart();
		//If he changed his mind, will set race to 0 so that the do while will continue
		if (blank == '0')
			eco = '0';
	} while (eco == '0');
	return eco;
}

//In case the user changed his mind about something, this function will tell the calling function that.
//If the user changed his mind, the function will return '0'. otherwise, it will return '1'
char changeofheart()
{
	printf("Are you sure of your choice? If you'll want to change it, type in Y. Otherwise type something else");
	skip;
	char flag = getc(stdin);
	if ((flag == 'y') || (flag == 'Y'))
	{
		flag = getc(stdin); //"Absorbing" the \n character so that it won't "pollute" the input stream.
		return '0';
	}
	else
	{
		flag = getc(stdin); //"Absorbing" the \n character so that it won't "pollute" the input stream.
		return '1';
	}
}