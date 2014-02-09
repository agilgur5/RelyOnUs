import math

# tag a dictionary based on the statiscal significance of the useful field
ALPHA = .05 # .05 alpha
ZSCORE = 1.96 # positive z-score of a 95% confidence interval
def tagStatisticalSignificance(adict):
  reviewCount = 1 #stores count of reviews
  reviewLimit = 161000 # ~70% to be used as training
  
  totalUseful = 0 #total number of useful votes
  #calculate useful votes
  #at the same time create a new dict that has only reviews from 1 - 161000
  taggedDict = {} # it will later be tagged
  testDict = {} # dict to later test (it is returned in this function without changes)
  for review_id, review in adict.items():
    if reviewCount <= reviewLimit:
      reviewCount += 1
      totalUseful += int(review.useful)
      taggedDict[review_id] = review
    else:
      testDict[review_id] = review

  sampleMean = float(totalUseful) / float(reviewCount) # figure out sample mean

  sampleStandardDeviation = float(0) #start calculating standard dev
  for review in taggedDict.values():
    sampleStandardDeviation += math.pow((float(review.useful) - sampleMean), float(2))

  sampleStandardDeviation = math.sqrt(sampleStandardDeviation / float(reviewCount + 1)) #new sample standard deviation

  print(sampleMean)
  print(sampleStandardDeviation)
  
  # tag the reviews if their useful rating is statistically significant
  for review in taggedDict.values(): 
    reviewZScore = (float(review.useful) - sampleMean) / sampleStandardDeviation # calculate z-score
    if reviewZScore > ZSCORE: # rating is above the confidence interval
      review.tag = "1"
    elif reviewZScore < (float(-1) * ZSCORE): #rating is below the confidence interval
      review.tag = "0"
  
  return taggedDict, testDict #return the fully tagged dictionary and the test dictionary

  #the split is done in this file to be most efficient 

  