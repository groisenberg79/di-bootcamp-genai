# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.

# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists

# Instructions:
# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    """
    A class used to represent song lyrics

    Attributes
    ----------
    lyrics: list
    - a list whose items are the verses of a song (strings)

    Methods
    -------
    sing_me_a_song()
        Prints the verses of the song


    """
    def __init__(self, lyrics):
        """
        :param lyrics: a list whose elements are the verses (strings) of the song
        :type lyrics: list
        """
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        """
        Prints the verses of the song
        """
        for verse in self.lyrics:
            print(verse)

def main():
    stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
    stairway.sing_me_a_song()

main()