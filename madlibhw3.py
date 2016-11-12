# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk 
import random
from nltk.book import *
from nltk import word_tokenize,sent_tokenize
print("START*******")
nltk.download('punkt')

txt = text2[:151]

debug = False #True

#gets file
if debug:
	print ("Getting information from file madlib_test.txt...\n")

tagged_tokens = nltk.pos_tag(txt) #list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "RB":.1} #Abbreviations and percentage of time the program prompts for them

def spaced(word):
	if word in ["", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word
print("".join([spaced(x) for x in txt]))
final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word)) 
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag])) #prompts user for new word
		final_words.append(spaced(new_word)) #adds words to list new_word


print ("".join(final_words)) #prints the new words in the test

print("\n\nEND*******")