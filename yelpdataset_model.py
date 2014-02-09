from nltk import word_tokenize
import parser

class Model:
	MAXFEATNUM = 99999999 # max feature number supported by SVMlight, scikit may be different, irrelevant as not using this many
	

	
	# adds ngrams of a review to a dictionary which is returned
	def createGramDict(review, n=1, gram_count_dict = {}):
		START = "SENT_START" #these are for n>1, they capture "start" and "end" of sentence.
		END = "SENT_END" ## so for tri-gram, sentence looks like "SENT_START SENT_START WORD1 WORD2 WORD3 SENT_END SENT_END"

		tokenized = word_tokenize(review.lower())
		numGrams = 0 #holds how many ngrams there are
		numString = "numberOf" + n + "Grams" #holds string to put into dict
		 
		if n == 1: # uni-gram
			for t in tokenized:
				gram_count_dict[t] = gram_count_dict.get(t, 0) + 1
				numGrams += 1
			gram_count_dict[numString] = numGrams
			n += 1
			createGramDict(review, n, gram_count_dict) #recurse
		
		elif n <= 6: # n-gram
			window = [START] * (n - 1)
			window.extend(tokenized)
			window.extend(([END] * (n - 1)))
			for i in xrange(len(tokenized) + (n-1)):
				ngram = " ".join(window[i : i + n])
				gram_count_dict[ngram] = gram_count_dict.get(ngram, 0) + 1
				numGrams += 1
			gram_count_dict[numString] = numGrams
			n += 1
			createGramDict(review, n, gram_count_dict) #recurse

		else:
			return gram_count_dict #end when over 6 grams

	# return a list of the dictionary
	def toSVMArray(review):
		return list(createGramDict(review))

# returns 2D array of samples x features given a dictionary of review objects
def dictionaryMain(adict):
  model = Model() #create new model
  list2D = [] #the 2D array to be returned
  for review in adict.values():
  	list2D.append(model.toSVMArray(review.text)) #create dictionary then list then append it to list2D
  return list2D