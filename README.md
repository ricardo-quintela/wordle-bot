# Wordle bot

This sheet provides the documentation for the wordle bot.  

## Adding a hint:

The program will ask the user for an input.  
After the user inputs a valid word (that belongs to the list) another input is goign to be asked to the user, this time regarding the letters that have been found.
There are some combinations of characters to indicate the bot which letters have been found to belong or not to the word. These are called **validation strings**.  

## Next hints:
The program will automaticly give the user a word to guess.


## Validation Strings

Combinations of characters to tell the bot which letters were hit right.  

Symbol | Meaning
-------|----------------------------------------------------------------
x      | The letter doesnt belong to the word
y      | The leter belongs to the word, however it's on a wrong position
g      | The letter is in a correct position

The user can use this characters to indicate the program the letters that have been found.  

Example:  
>```Please input the attempt in wordle> apple```  
>```Please input the wordle hints> yxxyg```  

This example indicate the program that the letters ***a*** and ***l*** belong to the word but are in the wrong position and that the letter ***e*** is in a correct position.
