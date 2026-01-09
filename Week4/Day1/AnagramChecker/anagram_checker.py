class AnagramChecker:
    def __init__(self):
        with open("Week4/Day1/AnagramChecker/sowpods.txt", "r") as f:
            self.word_list = f.read().split()
    
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
        # a dict that records each letter frequency in word1
        word1_count = {letter: word1.count(letter) for letter in word1}
        # a dict that records each letter frequency in word2
        word2_count = {letter: word2.count(letter) for letter in word2}
        # check if they are anagrams
        return word1_count == word2_count
    
    def get_anagrams(self, word: str) -> list[str]:
        """
        finds all anagrams for the given word
        
        :param word: a word
        :type word: str
        :return: a list of all anagrams of the given word
        :rtype: list[str]
        """
        return [anagram for anagram in self.word_list if anagram != word and AnagramChecker.is_anagram(word, anagram)]