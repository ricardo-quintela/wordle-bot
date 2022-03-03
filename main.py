from letter import Letter
from math import log2

def read_list() -> list:
    """Reads the list of words from the file

    Returns:
        list: the list of words available in wordle
    """
    with open("words.txt", "r") as f:
        return f.read().split("\n")


def write_list(words: list):
    """writes the list of words to a file

    Args:
        words (list): the list of words available
    """
    with open("wlist.txt", "w") as f:
        for word in words:
            f.write(word + "\n")


def start_word(words: list) -> str:
    """Asks the user to input a word

    Args:
        words (list): the list of words available in wordle

    Returns:
        str: the word guess
    """

    word = input("Please input the attempt in wordle> ")

    # protect against guesses that contain more or less than 5 letters
    while len(word) != 5:
        print("Input is not a 5 letter word!")
        word = input("Please input the attempt in wordle> ")

    # protect against guesses that are not in the word list
    while word not in words:
        print("Not in the word list!")
        word = input("Please input the attempt in wordle> ")

    return word



def validation_string() -> str:
    """Asks the user to input a validation string

    Returns:
        str: the validation string
    """

    output = input("Please input the wordle hints> ")

    # protect against inputs that contain more or less than 5 characters
    while len(output) != 5:
        print("Input is not a 5 character string!")
        output = input("Please input the wordle hints> ")

    # protect against invalid validation symbols
    while False in [char in "xyg" for char in output]:
        print("Error! Unknown symbol.")
        output = input("Please input the wordle hints> ")

    return output


def count_letters(words: list) -> dict:
    """Counts the letters in a word list

    Args:
        words (list): the list of words

    Returns:
        dict: the letter count
    """
    letters = {}

    # iterate through all words
    for word in words:

        # iterate through all letters of the word
        for letter in word:

            # add the letter to the dictionary
            if letter not in letters:
                letters[letter] = 1
                continue

            letters[letter] += 1

    return letters


def total_letters(words: list) -> int:
    """Counts the total number of letters in all words available

    Args:
        words (list): the words list

    Returns:
        int: the total number of letters in all words
    """
    total = 0

    # iterates through all words and counts all the letters
    for word in words:
        total += len(word)

    return total


def best_word(words: list, letter_count: dict, tot_letters: int) -> str:
    """Calculates the entropy of each word available to get the best guess

    Args:
        words (list): the list of words available
        letter_count (dict): the letter count of all words
        tot_letters (int): the total letters in all words

    Returns:
        str: the best next guess
    """
    
    # list containing all the entropies of all words available in the words list
    entropies = []

    # iterate through all words and calculate the entropy
    for word in words:
        
        entropy = 0
        
        # iterate through all letters to calculate the probability of each character to use in the entropy formula calculation
        for char in word:

            entropy += (letter_count[char] / tot_letters) * log2(letter_count[char] / tot_letters)

        entropies.append(-entropy)

    # return the word that gives the most entropy
    return words[entropies.index(max(entropies))]



def main():
    """Main function where all the others are going to be called
    """

    # list of words available in wordle
    words = read_list()

    # letters that have been tried
    letters = []

    # do an attept
    attempt = start_word(words)
    wordle_output = ""

    while wordle_output != "ggggg":

        # wrong letters
        w_letters = []

        # wordle hints
        wordle_output = validation_string()

        # add the letters to the data structures
        for i in range(5):

            letter = Letter(attempt[i], False if wordle_output[i] == "x" else True)
            
            # letter is not in the word
            if not letter.inWord:
                
                # letter isn't in letters list yet
                if letter not in w_letters:
                    w_letters.append(letter)
                
                continue

            # letter is in the word
            elif letter not in letters:
                letters.append(letter)
            
            # get the index of the letter in the letters list
            index = letters.index(letter)


            # letter is in the correct position
            if wordle_output[i] == "g":
                if i not in letters[index].r_pos:
                    letters[index].right_position(i)

            # letter is not in the correct position
            else:
                letters[index].wrong_position(i)


        # remove the words in the list with the letters in a wrong position
        i = 0
        while i < len(words):

            # wrong letter in word
            for letter in w_letters:

                if letter.char in words[i] and letter not in letters:
                    words.pop(i)
                    i -= 1 if i > 0 else 0
                    break
            
            # correct letter in a wrong spot
            for letter in letters:

                if letter.char not in words[i] or False in [letter.char == words[i][j] for j in letter.r_pos] or True in [letter.char == words[i][j] for j in letter.w_pos]:
                    words.pop(i)
                    i -= 1 if i > 0 else 0
                    break

            i += 1
        
        # !bug in the first word
        if words[0][0] != attempt[0] and wordle_output[0] == "g":
            words.pop(0)

        # Next attempt
        attempt = best_word(words, count_letters(words), total_letters(words))

        print("Try the word " + attempt)


if __name__ == "__main__":
    main()