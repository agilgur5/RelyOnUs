import re
import yelpdataset_model
import yelpdataset_tagByStatisticalSignificance
from sklearn import svm



class Review:
    def __init__(self, thetype, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date):
        self.thetype = thetype
        self.review_id = review_id
        self.tag = tag
        self.text = text
        self.user_id = user_id
        self.business_id = business_id
        self.stars = stars
        self.useful = useful
        self.cool = cool
        self.funny = funny
        self.date = date

class Business:
    def __int__(self, thetype, business_id, stars, review_count):
        self.thetype = thetype
        self.business_id = business_id
        self.stars = stars
        self.review_count = review_count

class User:
    def __init__(self, thetype, user_id, tag, name, review_count, average_stars, useful, cool, funny):
        self.thetype = thetype
        self.user_id = user_id
        self.tag = tag
        self.name = name
        self.review_count = review_count
        self.average_stars = average_stars
        self.useful = useful
        self.cool = cool
        self.funny = funny

def parse_reviews(filename):
    matcher = re.compile(r'(.+)\|(.+)\|([01?])\|(.+)\|(.+)\|(.+)\|(.+)\|(.+)\|(.+)\|(.+)\|(.+)')
    reviews = {}
    with open(filename, 'r') as f:
        for line in f:
            # extract data from line
            reviewMatch = matcher.match(line)
            if(not reviewMatch):
                continue
            thetype, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date = matcher.match(line).groups()
            reviews[review_id] = Review(thetype, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date)
    return reviews

# print the dictionary output to a certain file
def printDictOutput(filename, aDict):
    theOutput = open(filename, 'w')

    for review in aDict.values():
        theOutput.write("review|")
        theOutput.write("" + review.user_id + review.business_id + "|") #review_id = user_idbusiness_id
        theOutput.write("" + review.tag + "|") #tag position
        theOutput.write("" + review.text + "|")
        theOutput.write("" + review.user_id + "|")
        theOutput.write("" + review.business_id + "|")
        theOutput.write("" + review.stars + "|")
        theOutput.write("" + review.useful + "|")
        theOutput.write("" + review.cool + "|")
        theOutput.write("" + review.funny + "|")
        theOutput.write("" + review.date + "\n")

# create the tagged dataset and the test dataset (as new text files to parse)
def createTagAndTestDatasets():
    taggedOutput = "dataset-taggedReviews.txt" #filepath for tagged output
    newlyTaggedOutput = "dataset-newlyTaggedReviews.txt" #filepath for newly tagged output (which the svm fits)
    testOutput = "dataset-testReviews.txt" #filepath for reviews to be tested
    
    data = parse_reviews('dataset-reviews.txt') # parse the review txt into dictionaries of review objects
    taggedDict, testDict = yelpdataset_tagByStatisticalSignificance.tagStatisticalSignificance(data) # get the test data and the tagged data
    
    printDictOutput(taggedOutput, taggedDict) #print to file
    printDictOutput(testOutput, testDict)

def fitAndPredict():
    newlyTaggedOutput = "dataset-newlyTaggedReviews.txt" #filepath for newly tagged output (which the svm fits)
    
    data = parse_reviews('dataset-taggedReviews.txt') # parse the tagged review txt into dictionaries of review objects
    tagList = [] # list of tags to fit the data to
    for review in data.values():
        tagList.append(review.tag)

    list2D = yelpdataset_model.dictionaryMain(data) # create 2D array
    classifier = svm.SVC() # create classifer to learn to classify things
    classifier.fit(list2D, tagList) # fit the 2D array to the tagList (learn)

    newData = parse_reviews('dataset-testReviews.txt') # parse the test review txt into dictionaries of review objects
    newList2D = yelpdataset_model.dictionaryMain(newData) # create new 2D array
    newTagList = classifier.predict(newList2D) # predict the new tags

    # change tags in the newData dictionary
    count = 0
    for review in newData.values():
        review.tag = newTagList[count]
        count += 1

    #output dataset
    printDictOutput(newlyTaggedOutput)


if __name__ == '__main__':
    fitAndPredict()
    
    #for review in data.values():
     #   print("thetype: %s review_id: %s tag: %s text: %s user_id: %s business_id: %s stars: %s useful: %s cool: %s funny: %s date: %s" % (review.thetype, review.review_id, review.tag, review.text, review.user_id, review.business_id, review.stars, review.useful, review.cool, review.funny, review.date))

