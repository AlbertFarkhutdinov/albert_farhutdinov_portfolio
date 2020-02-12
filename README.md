# albert_farhutdinov_portfolio

Welcome! My name is Albert Farhutdinov. This is my portfolio. I collect here various small scripts written in Python and JavaScript by me. You can find descriptions for these scripts and requirements for their correct running below.

## Python

### Requirements

1. Before you start, make sure that you have Python 3.7 or later versions. Input this command into terminal:

        python --version
  
2. Install the necessary libraries in your environment for correct running of scripts in folders "kivy_calculator", "yandex_music_chart" and "matplotlib":

		pip install -r kivy_calculator/kivy_requirements.txt
		pip install -r yandex_music_chart/requirements.txt
		pip install -r matplotlib/matplotlib_requirements.txt
    
3. Scripts "integral.py", "equation.py" and "tabulation.py" require the script "input_functions.py" from folder "python" of this portfolio.

### Descriptions

The Python directory contains the following folders and scripts:

#### console_manager

The console manager contains functions for creating, copying and deleting files and folders, obtaining a list of files in the working directory and changing the directory. The script "core.py" contains descriptions of these functions. The script "main.py" contains the work logic of the manager. To run the manager, go to "console_manager" directory:

	cd console_manager
	
Then input:

	python main.py help
	
You will see the list of available commands, which you can input instead of "help". Some of them also require to input name of file or folder to be created, copied or deleted.

#### kivy_calculator

Calculator with basic arithmetic operations, created with Kivy library. Before you run it, read "Requirements".

#### matplotlib

There are 4 small tasks for mathematical statistics. Task conditions described in the scripts comments. Before you run it, read "Requirements".

#### vocabulary

"Vocabulary.py" is the script for training english words. It uses words from vocabulary.txt, where you can write you words in the form "english_word - translation".

#### yandex_music_chart

There is file "songs.xls" with two columns: singers and songs. The script "yandex_music_chart" compars songs from this file with songs in chart on [music.yandex.ru](https://music.yandex.ru/chart). If there are coincidences, the script shows where it is in the chart list.  If song from "songs.xls" is not in chart list, it prints in "Not Found" section. 
Before you run it, read "Requirements".

#### bulls_and_cows.py

This is the game "Bulls and Cows". The computer makes up a 4-digit number. You have to guess this number. The computer gives a clue in the form of bulls and cows after each attempt. This is a bull, if you guessed both a digit and its position in the number. This is a cow, if you guessed a digit of the number, but not its position. Thus, the goal of the game is to get the number of bulls equal to 4.

#### equation.py

This the solution of equation "3 * x - 4 * ln(x) - 5 = 0" by three methods: half division, Newton and iteration methods. The scipt also can work with another equation with one root.

#### gauss.py

This is the solution of systems of linear equations by Gauss method. The scipt works for system with one solution.

#### guess_number_part_1.py

Game "Guess the number". Users guess the number from 1 to 100, that made up by the computer.

#### guess_number_part_2.py

'Game "Guess the number". Computer guesses the number, that made up by the user.'

#### hexadecimal_calculator.py

This is the script, which can sum and multiply two hexadecimal numbers, that user inputs.

#### input_functions.py

There are useful functions, which check numbers inputted by user. If user inputs unacceptable value, a code with one of these functions continues work and gives new attempt for input.

#### integral.py

This is the script to find definite integral of function f(x) = x * ln(1 + x^3) by rectangle (lower and upper sums), trapezium and Simpson's parabolic methods. The scipt also can work with other functions.

#### is_it_prime.py

There is the function, which checks if it's argument is a prime number.

#### russian_roulette.py

The game "Russian roulette".

#### sorters.py

There are functions for sorting and reversing of number arrays, which are not built in Python. The script includes bubble, selection, insertion sorter, Shell sorter, Hoare's quick sorters and array reverser. All functions do not return new array, but change initial one.

#### sorters_creators.py

The same, that in sorters.py, however all functions return new array without changing initial one.

#### tabulation.py

Tabulation of function f(x) = A * x^2 on interval beetween two values inputted by user. Value of parameter A is also inputted by user.  The scipt also can work with other functions.

## JavaScript

### Requirements

JavaScript projects do not have special requirements.

### Descriptions

The JS directory contains the following folders:

#### bullsAndCows

This is the browser game "Bulls and Cows". The computer makes up a 4-digit number. You have to guess this number. The computer gives a clue in the form of bulls and cows after each attempt. This is a bull, if you guessed both a digit and its position in the number. This is a cow, if you guessed a digit of the number, but not its position. Thus, the goal of the game is to get the number of bulls equal to 4.

#### chess

This is the chess board with chess figures.

#### guessNumber

This is the browser game "Guess the number". Users guess the number from 1 to 100, that made up by the computer.

#### millionare

This is the browser game "Who wants to be a millionare".

#### quest

This is demo of the browser quest game.

#### race

This is the browser game "Race".

#### snake

This is the browser game "Snake".

#### ticTacToe

This is the browser game "Tic-Tac-Toe".

