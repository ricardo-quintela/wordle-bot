class Letter:
    def __init__(self, char: str, inWord: bool = True) -> None:
        """Constructor of the class Letter

        Args:
            char (str): _description_
            inWord (bool): whether the letter is in the word or not
        """
        self.char = char

        self.inWord = inWord
        
        self.r_pos = []

        self.w_pos = []

    
    def __eq__(self, __o: object) -> bool:
        """To compare with other Letter object

        Args:
            __o (Letter): the letter to caompare

        Returns:
            bool: Whether the letter is the same or not
        """
        return __o.char == self.char

    def __repr__(self) -> str:
        """Returns a string representation of the Letter object

        Returns:
            str: the string representation object
        """
        return self.char

    
    def right_position(self, pos: int):
        """Set the correct position to the letter

        Args:
            pos (int): the position to assign to the letter
        """
        self.r_pos.append(pos)

    def wrong_position(self, pos: int):
        """add a new wrong position to the letter

        Args:
            pos (int): the wrong position to add to the letter
        """
        self.w_pos.append(pos)
