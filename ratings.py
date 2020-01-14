"""Restaurant rating lister."""


# put your code here
def restaurant_scorer(filename):
    with open(filename, 'r') as f:

        # make a dictionary
        scores = {}

        for line in f.readlines():
            # read lines to fill the dictionary
            restaurant, rating = line.rstrip().split(':')
            scores[restaurant] = rating

    new_restaurant, new_rating = gets_review()
    scores[new_restaurant] = new_rating

    # pull the items from the dictionary
    # sort the items in the dictionary
    alpha_sorted_ratings = sorted(scores.items())

    # print recommended statement
    for restaurant, rating in alpha_sorted_ratings:
        print(f"{restaurant} is rated at {rating}.")


def gets_review():
    '''Asks user for their own restaurant name and review.'''

    restaurant_name = input("Please write a restaurant name: ")

    while True:
        restaurant_score = input("Please give the score for your restaurant (1-5): ")
        if validate_score(restaurant_score):
            break

    return (restaurant_name, restaurant_score)


def validate_score(score):
    try:
        score = int(score)
    except ValueError:
        print("The score must be an integer between 1 and 5.")
        return False

    return 1 <= score <= 5


restaurant_scorer('scores.txt')
