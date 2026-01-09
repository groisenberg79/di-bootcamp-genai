class AnagramChecker:
    with open("Week4/Day1/AnagramChecker/sowpods.txt", "r") as f:
        word_list = f.read().split()

    def __init__(self):
        self.word_list = AnagramChecker.word_list
    
    def is_valid_word(self, word: str) -> bool:
        """
        checks if the given word (ie. the word of the user) is a valid word.
        
        :param word: a word
        :type word: str
        :return: True if word is valid, False otherwise
        :rtype: bool
        """
        if word.upper() in self.word_list:
            return True
        else:
            return False
    
    @classmethod
    def is_anagram(cls, word1:str, word2:str) -> bool:
        """
        checks if two words are anagrams of each other
        
        :param word1: a word
        :type word1: str
        :param word2: a word
        :type word2: str
        :return: True if they are anagrams, False otherwise
        :rtype: bool
        """
        # make a sorted list of the letters of word1 
        word1_sorted = sorted(word1)
        # make a sorted list of the letters of word2
        word2_sorted = sorted(word2)
        return word1_sorted == word2_sorted
    
    def get_anagrams(self, word: str) -> list[str]:
        """
        finds all anagrams for the given word
        
        :param word: a word
        :type word: str
        :return: a list of all anagrams of the given word
        :rtype: list[str]
        """
        return [anagram for anagram in self.word_list if anagram != word and AnagramChecker.is_anagram(word, anagram)]