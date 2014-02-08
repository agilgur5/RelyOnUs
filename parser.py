
import re




class Review:
    def __init__(self, type, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date):
		self.type = type
        self.review_id = review_id
        self.tag = tag
        self.text = text
        self.user_id = user_id
        self.business_id = busines_id
        self.stars = stars
        self.useful = useful
        self.cool = cool
        self.funny = funny
        self.date = date

class Business:
    def __int__(self, type, business_id, stars, review_count):
        self.type = type
        self.business_id = business_id
        self.stars = stars
        self.review_count = review_count

class User:
    def __init__(self, user_id, tag, name, review_count, average_stars, useful, cool, funny):
        self.user_id = user_id
        self.tag = tag
        self.name = name
        self.review_count = review_count
        self.average_stars = average_stars
        self.useful = useful
        self.cool = cool
        self.funny = funny

def parse_reviews(filename):
	matcher = re.compile(r'([01])|([01?])|(.+)|(.+)|(.+)|(.+)|(.+)|(.+)|(.+)|(.+)')
	reviews = {}
	with open(filename, 'r') as f:
		for line in f:
			# extract data from line
			reviews = matcher.match(line)
			if(not reviews):
				continue
            type, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date = matcher.match(line).groups()
            reviews[review_id] = Review(type, review_id, tag, text, user_id, business_id, stars, useful, cool, funny, date)
	return reviews


if __name__ == '__main__':
	data = parse_data('../data/Train data')
	for review in data:
		print "type: %s review_id: %s tag: %s text %s user_id %s business_id %s stars %s useful %s cool %s funny %s date %s" % (review.type, review.review_id, review.tag, review.text, review.user_id, review.business_id, review.stars, review.useful, review.cool, review.funny, review.date)

