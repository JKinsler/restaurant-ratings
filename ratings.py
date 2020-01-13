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

    # pull the items from the dictionary
    # sort the items in the dictionary
    alpha_sorted_ratings = sorted(scores.items())

    # print recommended statement
    for restaurant, rating in alpha_sorted_ratings:
        print(f"{restaurant} is rated at {rating}.")


restaurant_scorer('scores.txt')
