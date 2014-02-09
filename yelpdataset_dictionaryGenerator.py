import re
import yelpdataset_model
import yelpdataset_tagByStatisticalSignificance



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

# print the tagged output to a certain file
def printTaggedOutput(filename, taggedDict):
    taggedOuput = open(filename, 'w')

    for review in taggedDict
        taggedOutput.write("review|")
        taggedOutput.write("" + review.user_id + review.business_id + "|") #review_id = user_idbusiness_id
        taggedOutput.write("?|") #tag position
        taggedOutput.write("" + review.text + "|")
        taggedOutput.write("" + review.user_id + "|")
        taggedOutput.write("" + review.business_id + "|")
        taggedOutput.write("" + str(review.stars) + "|")
        taggedOutput.write("" + str(review.useful) + "|")
        taggedOutput.write("" + str(review.cool) + "|")
        taggedOutput.write("" + str(review.funny) + "|")
        taggedOutput.write("" + review.date + "\n")

# create the tagged dataset and the test dataset (as new text files to parse)
def createTagAndTestDatasets():
    taggedOuput = "dataset-taggedReviews.txt" #filepath for tagged output
    newlyTaggedOutput = "dataset-newlyTaggedReviews.txt" #filepath for newly tagged output (which the svm fits)
    testOutput = "dataset-testReviews.txt" #filepath for reviews to be tested
    
    data = parse_reviews('dataset-reviews.txt') # parse the review txt into dictionaries of review objects
    taggedDict, testDict = yelpdataset_tagByStatisticalSignificance.tagStatisticalSignificance(data) # get the test data and the tagged data
    
    printTaggedOutput(taggedOutput, taggedDict) #print to file
    printTaggedOutput(testOutput, testDict)

if __name__ == '__main__':
    createTagAndTestDatasets()
    
    #for review in data.values():
     #   print("thetype: %s review_id: %s tag: %s text: %s user_id: %s business_id: %s stars: %s useful: %s cool: %s funny: %s date: %s" % (review.thetype, review.review_id, review.tag, review.text, review.user_id, review.business_id, review.stars, review.useful, review.cool, review.funny, review.date))

