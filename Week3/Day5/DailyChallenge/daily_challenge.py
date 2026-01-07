# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class
# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).

# Step 2: Implement word_frequency Method
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

# Step 3: Implement most_common_word Method
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

# Step 4: Implement unique_words Method
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

# Bonus: Text Modification

# Step 6: Create the TextModification Class
# Create a class called TextModification that inherits from Text.

# Step 7: Implement remove_punctuation Method
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

# Step 8: Implement remove_stop_words Method
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

# Step 9: Implement remove_special_characters Method
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.
import re

class Text:
    def __init__(self, text: str):
        self.text = text

    def create_word_list(self) -> list[str]:
        """
        creates a list of all words in Text object (with repetitions)
        
        :return: list of word occurrences
        :rtype: list[str]
        """
        return re.findall(r"[A-Za-z]+(?:[A-Za-z])*", self.text)

    def word_frequency(self, word: str) -> int|None:
        """
        counts the occurrences of the given word in the Text object.
        
        :param word: a word
        :type word: str
        :return: number of times the word occurs
        :rtype: int | None
        """
        word_list = self.create_word_list()
        if word_list.count(word):
            return word_list.count(word)
        else:
            return None
    
    def most_common_word(self) -> str:
        """
        finds the most common word in the Text object
        
        :return: the most common word
        :rtype: str
        """
        word_list = self.create_word_list()
        word_dict = dict()
        for item in word_list:
            if item not in word_dict:
                word_dict[item] = word_list.count(item)
        return max(word_dict.keys(), key=lambda x: word_dict[x])
    
    def unique_words(self) -> list[str]:
        """
        generates the list of words in the Text objects, without repetition
        
        :return: a list of unique words
        :rtype: list[str]
        """
        word_list = self.create_word_list()
        word_set = {word for word in word_list}
        return list(word_set)
    
    @classmethod
    def from_file(cls, file_path: str) -> Text:
        """
        creates a Text instance with the file content as the text.
        
        :param file_path: the directory path of the text file
        :type file_path: str
        :return: a Text object with the text as its atributte
        :rtype: Text
        """
        try:
            with open(file_path, 'r') as f:
                text = f.read()
            return Text(text)
        except FileNotFoundError:
            print(f"{file_path}: file not found.")

text = """As the voluminous literature on the “scientific method” makes clear, this version of it is simplified to the point of caricature. Not the least of the caveats is that “disagreement with experiment” is a complicated matter – we cannot, for example, be sure the experiment has tested what we want it to test, or that it has been conducted properly. Another physics Nobel Laureate, Steven Weinberg, admitted to the truth of the matter: “We do not have a fixed scientific method to rally around and defend.” [1]
Much of this discussion about scientific methodology focuses on how we might abstract observations and experiments into theories – which are expected to have predictive and not just descriptive capability. Physicist and philosopher Pierre Duhem states that “A physical theory is… a system of mathematical propositions, deduced from a small number of principles, which aim to represent as simply, as completely, and as exactly as possible a set of experimental laws.”[2] There speaks the physical scientist; other disciplines, such as biology and the Earth sciences, are content to accept theories that are not expressed in abstract, mathematical terms – the theory of plate tectonics, for example – yet still serve to rationalize a set of observations and to make predictions about the world.
All the same, these efforts to distil what scientists do into a formula that generates knowledge tend to imply that the knowledge is ultimately expressed in theories. But that is not the same as providing an explanation for what we see. Duhem himself admits that “A physical theory is not an explanation”. His view of an explanation, however, is grand and abstract (as well as being framed in the antiquated sexualized manner): “To explain is to strip reality of the appearances covering it like a veil, in order to see the bare reality itself.”[3]
"""

# testing the program:

# create a Text object
my_text = Text(text)

# find the frequency of 'you' in the text
you_freq = my_text.word_frequency('you')
print(you_freq)

# find the most common word in my_text
most_common = my_text.most_common_word()
print(most_common)

#print the list of the unique words in my_text
print(my_text.unique_words())

# create a Text object by supplying a text file
new_text = Text.from_file("Week3/Day5/DailyChallenge/sample_text.txt")
print(new_text)