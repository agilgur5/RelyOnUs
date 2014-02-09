from nltk import word_tokenize
import parser
import sklearn.feature_extraction.text

class Model:
	MAXFEATNUM = 99999999 # max feature number supported by SVMlight, scikit may be different, irrelevant as not using this many
	

	
	# adds ngrams of a review to a dictionary which is returned
	def createGramDict(self, review, n=1, gram_count_dict = {}):
		START = "SENT_START" #these are for n>1, they capture "start" and "end" of sentence.
		END = "SENT_END" ## so for tri-gram, sentence looks like "SENT_START SENT_START WORD1 WORD2 WORD3 SENT_END SENT_END"

		tokenized = word_tokenize(review.lower())
		numGrams = 0 #holds how many ngrams there are
		numString = "numberOf" + str(n) + "Grams" #holds string to put into dict
		 
		if n == 1: # uni-gram
			for t in tokenized:
				gram_count_dict[t] = gram_count_dict.get(t, 0) + 1
				numGrams += 1
			gram_count_dict[numString] = numGrams
			n += 1
			return gram_count_dict
			# getss memory error return self.createGramDict(review, n, gram_count_dict) #recurse
		
		elif n <= 5: # n-gram
			window = [START] * (n - 1)
			window.extend(tokenized)
			window.extend(([END] * (n - 1)))
			for i in range(len(tokenized) + (n-1)):
				ngram = " ".join(window[i : i + n])
				gram_count_dict[ngram] = gram_count_dict.get(ngram, 0) + 1
				numGrams += 1
			gram_count_dict[numString] = numGrams
			n += 1
			return self.createGramDict(review, n=n, gram_count_dict=gram_count_dict) #recurse

		else:
			return gram_count_dict

	# return a list of the dictionary
	def toSVMArray(self, reviews):
		#adict = self.createGramDict(review)
		#print(adict)
		#theList = []
		#for k, v in adict.items():
		#	theList.append(v)
		#return theList
		learnfile = open("dataset-learnreviews.txt", 'r')
		tfidf = sklearn.feature_extraction.text.TfidfVectorizer(input=learnfile, ngram_range=(1, 1),stop_words='english',max_features=100)
		predictfile = open(reviews, 'r')
		return tfidf.fit_transform(predictfile)

# returns 2D array of samples x features given a dictionary of review objects
def dictionaryMain(reviewfile):
  model = Model() #create new model
  list2D = model.toSVMArray(reviewfile) #the 2D array to be returned
  #for review in adict.values():
  #	list1D = model.toSVMArray(review.text) # creates a list from the dictionary from the text
  #	list2D.append(list1D) #create dictionary then list then append it to list2D
  return list2D