#-------------------------------------------------------------------------------
# Name:        enigma_plugboard.py
#
# Notes:       The plugboard (Steckerbrett) added an extra layer of combinations
#              only available to the millitary (not civillian models). Swaps the
#              input letter with another and then sends it through the rotors.
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

# Historically accurate, so it is hard-coded here
MAX_PLUGS = 10

class Plugboard:
    ''' A historic plugboard that swaps two letters up to 10 times '''
    def __init__(self):
        self.plugs = {}
        self.plugs_reversed = {}

    def reset(self):
        ''' Removes all plug connections '''
        self.__init__()

    def add_plug(self, connection_a, connection_b):
        ''' Swaps two letters before or after encryption by the machine '''
        if len(self.plugs) >= MAX_PLUGS:
            return  

        connection_a, connection_b = connection_a.upper(), connection_b.upper()

        # Don't add if either connection is already connected to something else
        if connection_a in self.plugs or connection_a in self.plugs_reversed:
            return
        elif connection_b in self.plugs or connection_b in self.plugs_reversed:
            return
        
        self.plugs[connection_a] = connection_b
        self.plugs_reversed[connection_b] = connection_a

    def remove_plug(self, connection):
        ''' Removes a plug connection and removes it's corresponding link '''
        connection = connection.upper()

        if connection in self.plugs:
            del self.plugs_reversed[self.plugs[connection]]
            del self.plugs[connection]

        if connection in self.plugs_reversed:
            del self.plugs[self.plugs_reversed[connection]]
            del self.plugs_reversed[connection]

    def reroute_letter(self, letter):
        ''' Takes a letter and re-routes or swaps letters bassed on the plugs in the 
            plugboard '''
        letter = letter.upper()

        # Do we send the letter through a connector or just leave it alone?
        if letter in self.plugs:
            return self.plugs[letter]
        elif letter in self.plugs_reversed:
            return self.plugs_reversed[letter]
        else:
            return letter

    def __str__(self):
        ''' Returns a string in the format [(a,b)(c,d)(e,f)...]'''
        # s = ''.join([f'({key},{value})' for key, value in self.plugs.items()])
        # return f'[{s}]'
        s = ' '.join([f'{key}{value}' for key, value in self.plugs.items()])
        return f'[{s}]'




    def __repr__(self):
        ''' Returns a string in the dictionary format
            E.g. {'A': 'B', 'C': 'D', 'E': 'F'} '''
        return f'{self.plugs}'  