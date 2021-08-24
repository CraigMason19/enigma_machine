#-------------------------------------------------------------------------------
# Name:        enigma_plugboard.py
#
# Notes:       The plugboard (Steckerbrett) added an extra layer of combinations
#              only available to the millitary (not civillian models). 
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

# Historically accurate, so it is a hard-coded global here
MAX_PLUGS = 10

class Plugboard:
    """A historic M3 plugboard that creates a link between two letters. This 
       swaps the letters before and after going through the rotor translation.
       Up to 10 connections can be made.
    
    Attributes:
        plugs:
            A dictionary containing a link between two letters. 
            E.G. A-C
        plugs_reversed:
            A dictionay containing the reversed link between two letters. 
            E.G. C-A

    Methods:
        __init__():
            Creates two dictionaries that represent the dual relationship of a 
            pair of connected letters
        reset():
            Calls the __init__ method and recreates both lists as empty 
            dictionaries.
        add_plug(connection_a, connection_b):
            Creates a link and reversed link between two letters.
        remove_plug(connection):
            Removes a connection from both connection dictionaries.
        reroute_letter(letter):
            Returns the coresponding linked letter of a plug connection, or
            if no connection exists returns the original letter.
    """
    def __init__(self):
        """Creates two dictionaries that represent the dual relationship of a 
           pair of connected letters.

        Args:
            None.

        Returns:
            None.
        """  
        self.plugs, self.plugs_reversed = {}, {}

    def reset(self):
        """Removes all plug connections.

        Args:
            None.

        Returns:
            None.
        """  
        self.__init__()

    def add_plug(self, connection_a, connection_b):
        """Adds a connection between two letters in the plugboard.

        Args:
            connection_a:
                The first letter in the connection pair.
            connection_b:
                The second letter in the connection pair.

        Returns:
            None.
        """  
        if len(self.plugs) >= MAX_PLUGS:
            return  

        connection_a, connection_b = connection_a.upper(), connection_b.upper()

        # Don't add if either connection is already connected to something else
        if connection_a in self.plugs or connection_a in self.plugs_reversed:
            return
        elif connection_b in self.plugs or connection_b in self.plugs_reversed:
            return
        
        # Otherwise, put a link to each other in the two dictionaries
        self.plugs[connection_a] = connection_b
        self.plugs_reversed[connection_b] = connection_a

    def remove_plug(self, connection):
        """Removes a plug connection and also it's corresponding link.

        Args:
            connection:
                One letter of the connection pair we want to remove.

        Returns:
            A single uppercase letter.
        """  
        connection = connection.upper()

        if connection in self.plugs:
            del self.plugs_reversed[self.plugs[connection]]
            del self.plugs[connection]

        if connection in self.plugs_reversed:
            del self.plugs[self.plugs_reversed[connection]]
            del self.plugs_reversed[connection]

    def reroute_letter(self, letter):
        """Takes a letter and re-routes it through the plugs that have been set
           in the plugboard. If the letter is not effected by the plugboard it 
           is simply returned.

        Args:
            letter:
                The letter we wish to translate through the plugboard.

        Returns:
            A single uppercase letter.
        """  
        letter = letter.upper()

        # Do we send the letter through a connector or just leave it alone?
        if letter in self.plugs:
            return self.plugs[letter]
        elif letter in self.plugs_reversed:
            return self.plugs_reversed[letter]
        else:
            return letter

    def __str__(self):
        """Returns a string in the format [ab cd ef...].

        Args:
            None.

        Returns:
            A string.
        """  
        s = ' '.join([f'{key}{value}' for key, value in self.plugs.items()])
        return f'[{s}]'

    def __repr__(self):
        """Returns a string in the dictionary format.
           E.g. {'A': 'B', 'C': 'D', 'E': 'F'} 

        Args:
            None.

        Returns:
            A string.
        """   
        return f'{self.plugs}'  