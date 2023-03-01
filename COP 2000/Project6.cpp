//William Knapp
//COP2000.0M1
//Program is a game that allows user to roll a simulated die that either adds or subracts from their balance,
//depending on what they roll.
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;


//Class declarations
class Game
{
private:
	int balance;
	int rolled;
	char choice;
	void validateBalance(float &);
	void validateAgain(char &);

public:
	Game()
	{
		balance = 0;
		rolled = 0;
		choice = 'y';
		srand(time(NULL));
	}

	void setBalance();
	void roll();
	void display();
	void again();
};


//Function prototypes



//Function definitions
void Game::validateBalance(float &b)
{
	
	while ((!cin) || (b < 1))	//tests if the cin fails or if input is less than 1
	{
		//clears input buffer, asks for input again
		cin.sync();
		cin.clear();
		cin.ignore(10000000, '\n');
		cout << endl << "Invalid amount entered. Try again: $ ";
		cin >> b;
	}
}

void Game::validateAgain(char &c)
{
	while ((!cin) || (c != ('y' || 'n' || 'Y' || 'N')))	//tests if the cin fails or if input something other than 'y/Y' or 'n/N'
	{
		//clears input buffer, asks for input again
		cin.sync();
		cin.clear();
		cin.ignore(10000000, '\n');
		cout << endl << "Invalid option selected. Try again. (y=yes, n=no): ";
		cin.get() >> c;
	}
}

void Game::setBalance()
{
	float input;
	cout << "Enter your starting balance (minimum of $1): $";
	cin >> input;
	validateBalance(input);
}




int main()
{
	//program code goes here

	system("pause");
	return 0;
}
