
import re




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


if __name__ == '__main__':
    data = parse_reviews('dataset-reviews.txt')
    for review in data.values():
        print("thetype: %s review_id: %s tag: %s text: %s user_id: %s business_id: %s stars: %s useful: %s cool: %s funny: %s date: %s" % (review.thetype, review.review_id, review.tag, review.text, review.user_id, review.business_id, review.stars, review.useful, review.cool, review.funny, review.date))

