# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random
from nltk.book import *
from nltk import word_tokenize,sent_tokenize
print("START*******")

txt = text2[:151]

debug = False #True

if debug:
	print ("Getting information from file madlib_test.txt...\n")

tagged_tokens = nltk.pos_tag(txt) 


tagmap = {"NN":"a noun","NNS":"a plural noun","RB":"adverb","JJ":"an adjective","VBD":"a past-tense verb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"RB":.1,"JJ":.1, "VBD":.1}

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
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))


print ("".join(final_words))

print("\n\nEND*******")