import json

# Also need to remove \u2122, \u20ac, \xae from reviews
# Also need to replace \xe3, \xc0 with a, \u0153 with o, \xcc with i, \xda with u, \xc1 with a, \xd3 with o from reviews
datasetFilepath = "yelp_phoenix_academic_dataset_reencoded.txt"  #yelp dataset with all unix encoding and check ins removed
#startLine = 1314 #first review/business/user in file

businessDataset = open("dataset-business.txt", 'w') #output for businesses
userDataset = open("dataset-users.txt", 'w') #output for users
reviewDataset = open("dataset-reviews.txt", 'w') #output for reviews

jsonDecoder = json.JSONDecoder()

with open(datasetFilepath, 'r') as text:
  lineCount = 1
  for line in text:
    # skip lines until startLine
    #if lineCount < startLine:  
     # lineCount += 1 
      #continue
    #print(line)
    if lineCount == 1:
      adict = jsonDecoder.decode(line[3:]) #read in JSON as dictionary
    else:
      adict = jsonDecoder.decode(line)
    lineCount += 1

    if adict['type'] == 'business': #if business
      #write to businessDataset
      businessDataset.write("business|")
      businessDataset.write("" + adict['business_id'] + "|")
      businessDataset.write("" + str(adict['stars']) + "|")
      businessDataset.write("" + str(adict['review_count']) + "\n")

    elif adict['type'] == 'user': #if user
      #write to userDataset
      userDataset.write("user|")
      userDataset.write("" + adict['user_id'] + "|")
      userDataset.write("?|") #tag position
      userDataset.write("" + adict['name'] + "|")
      userDataset.write("" + str(adict['review_count']) + "|")
      userDataset.write("" + str(adict['average_stars']) + "|")
      #print(adict['votes'])
      voteDict = jsonDecoder.decode(str(adict['votes']).replace("\'","\"")) #votes are also in json
      userDataset.write("" + str(voteDict['useful']) + "|")
      userDataset.write("" + str(voteDict['cool']) + "|")
      userDataset.write("" + str(voteDict['funny']) + "\n")

    elif adict['type'] == 'review': #if review
      #write to reviewDataset
      reviewDataset.write("review|")
      reviewDataset.write("" + adict['user_id'] + adict['business_id'] + "|") #review_id = user_idbusiness_id
      reviewDataset.write("?|") #tag position
      reviewDataset.write("" + adict['text'].replace("\n"," ") + "|")
      reviewDataset.write("" + adict['user_id'] + "|")
      reviewDataset.write("" + adict['business_id'] + "|")
      reviewDataset.write("" + str(adict['stars']) + "|")
      #print(adict['votes'])
      voteDict = jsonDecoder.decode(str(adict['votes']).replace("\'","\"")) #votes are also in json
      reviewDataset.write("" + str(voteDict['useful']) + "|")
      reviewDataset.write("" + str(voteDict['cool']) + "|")
      reviewDataset.write("" + str(voteDict['funny']) + "|")
      reviewDataset.write("" + adict['date'] + "\n")