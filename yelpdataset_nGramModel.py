from nltk import word_tokenize
import parser

class Model:
	MAXFEATNUM = 99999999 # max feature number supported by SVMlight, scikit may be different, irrelevant as not using this many
	

	##
	# processes a single review, adding the words processed to a dictionary which is returned
	##
	def createGrams(review, n=1):
		gram_count_dict = {} # dictionary to hold ngram counts
		START = "SENT_START" #these are for n>1, they capture "start" and "end" of sentence.
		END = "SENT_END" ## so for tri-gram, sentence looks like "SENT_START SENT_START WORD1 WORD2 WORD3 SENT_END SENT_END"

		tokenized = word_tokenize(review.lower())
		
		if n == 1: # uni-gram
			for t in tokenized:
				gram_count_dict[t] = gram_count_dict.get(t, 0) + 1
		
		else: # n-gram
			window = [START] * (n - 1)
			window.extend(tokenized)
			window.extend(([END] * (n - 1)))
			for i in xrange(len(tokenized) + (n-1)):
				ngram = " ".join(window[i : i + n])
				gram_count_dict[ngram] = gram_count_dict.get(ngram, 0) + 1

		return gram_count_dict

  ##
	# return a list of the dictionary
  ##
	def toSVMArray(review, n=1):
		return list(createGrams(review, n))
##
# main function if file isn't lines of text but instead a dictionary, returns 2D array of samples x features
##
def dictionaryMain(adict):
  model = Model() #create new model
  list2D = [] #the 2D array to be returned
  for review in adict.values():
  	list2D.append(model.toSVMArray(review.text)) #create dictionary then list then append it to list2D
  return list2D
  	


if __name__ == '__main__':
	train = parser.parse_data("filename") #what data is this? The review text? ##yes

	n = Model()

	n.resetOutput("model_train")
	for r in train:
		n.trainGrams(r)
		n.outputSVM("model_train")
		n.resetGrams()