# Movie Review Sentiment Analyzer

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Function to count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)


# Function to find most common word
def most_common_word(reviews):
    words = {}

    for review in reviews:
        for word in review.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    max_word = ""
    max_count = 0

    for word in words:
        if words[word] > max_count:
            max_count = words[word]
            max_word = word

    return max_word


# Function to find longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest


# Function to display reviews with keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword, ":")

    for review in reviews:
        if keyword in review:
            print(review)


# Main Program

count_sentiments(reviews)

print("Most Common Word:", most_common_word(reviews))

print("Longest Review:", longest_review(reviews))

reviews_with_keyword(reviews, "excellent")