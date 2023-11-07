import re
from collections import Counter
import nltk
nltk.download('punkt')
from nltk.corpus import cmudict
nltk.download('cmudict')
cmudict = cmudict.dict()

# Function for counting words and sentences
def count_words_sentences(text):
    sentences = nltk.sent_tokenize(text)
    words = re.findall(r'\w+', text)
    word_count = len(words)
    sentence_count = len(sentences)
    number_of_digits = len(re.findall(r'\d', text))  # Number of digits in the text
    return word_count, sentence_count, number_of_digits

# Function for word frequency analysis
def word_frequency(text):
    words = re.findall(r'\w+', text)
    words = [word.lower() for word in words]
    word_frequency = Counter(words)
    most_common_words = word_frequency.most_common(10)
    return most_common_words

# Function to calculate sentence length without spaces and punctuation marks
def sentence_length(text):
    return len(re.findall(r'\w', text))  # Number of letters and digits in the sentence

# Function to calculate text statistics
def text_statistics(text):
    sentences = nltk.sent_tokenize(text)
    words = re.findall(r'\w+', text)
    average_sentence_length = sum(sentence_length(sentence) for sentence in sentences) / len(sentences)  # Average sentence length without spaces and punctuation
    average_word_count = len(words) / len(sentences)
    return average_sentence_length, average_word_count

# Function to detect the longest and shortest sentence
def longest_shortest_sentence(text):
    sentences = nltk.sent_tokenize(text)
    sentences.sort(key=len)
    shortest = sentences[0]
    longest = sentences[-1]
    return shortest, longest

# Function for text difficulty analysis
def text_difficulty(text):
    sentences = nltk.sent_tokenize(text)
    words = re.findall(r'\w+', text)
    sentence_count = len(sentences)
    word_count = len(words)
    syllable_count = sum([sum([1 for phoneme in pronunciation if phoneme[-1].isdigit()]) for word in words for pronunciation in cmudict.get(word.upper(), [[]])[0]])

    flesch_kincaid = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
    return flesch_kincaid

# Function for results visualization
def visualize_results(text, word_count, sentence_count, number_of_digits, most_common_words, average_sentence_length, average_word_count, shortest, longest, flesch_kincaid):
    print("Text analysis:")
    print("Word count:", word_count)
    print("Sentence count:", sentence_count)
    print("Number of digits:", number_of_digits)
    print("Most common words:")
    for word, frequency in most_common_words:
        print(f"{word}: {frequency}")
    print("Average sentence length:", average_sentence_length)
    print("Average word count per sentence:", average_word_count)
    print("Shortest sentence:", shortest)
    print("Longest sentence:", longest)
    print("Text difficulty (Flesch-Kincaid):", flesch_kincaid)

# Example usage
text = "Example text. This is an example of text analysis. It contains words and sentences. 12345 is a number."
number_of_letters = len([character for character in text if character.isalpha()])
print("Number of letters in the text:", number_of_letters)

word_count, sentence_count, number_of_digits = count_words_sentences(text)
most_common_words = word_frequency(text)
average_sentence_length, average_word_count = text_statistics(text)
shortest, longest = longest_shortest_sentence(text)
flesch_kincaid = text_difficulty(text)
visualize_results(text, word_count, sentence_count, number_of_digits, most_common_words, average_sentence_length, average_word_count, shortest, longest, flesch_kincaid)
