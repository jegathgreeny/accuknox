# restaurant.py - finds the most ordered foods in the restaurant


def main():

    the_log = {
        1: [["a", "b", "c"]],
        2: [["d", "e", "f"]],
        3: [["a", "c", "g"]],
        4: [["a", "c", "g"]],
        5: [["h", "j", "k"]],
        6: [["l", "m", "n"]],
    }
    check = unique_orders(the_log)
    top_foods = find_top_foods(check)
    print(top_foods)


def find_top_foods(the_log):
    """find the top three foods that was ordered"""
    # keeps track of the number of times a food is ordered
    count = {}

    for key, value in the_log.items():
        for one_list in value:
            for i in range(len(one_list)):
                # add the food if it doesn't already exist in the dictionary
                if one_list[i] not in count:
                    count[one_list[i]] = 1
                # increment the value by 1 if the food already exists in the dictionary
                else:
                    count[one_list[i]] += 1

    # holds the most ordered foods
    most_ordered_food = set()

    # get the list of values and sort them and slice only the top three values
    the_values = list(count.values())
    the_values.sort(reverse=True)
    the_values = the_values[:3]

    # get the key associated with the value.
    for value in the_values:
        for key in count.keys():
            if count[key] == value:
                # add values if there are less than three values in the set
                if len(most_ordered_food) < 3:
                    most_ordered_food.add(key)

    return most_ordered_food


def unique_orders(the_log):
    """check to see if there is repetition of eater and food"""
    for key in the_log.keys():
        if len(the_log[key]) > 1:
            for i in range(len(the_log[key]) - 1):
                for j in range(1, len(the_log[key])):
                    for k in the_log[key][i]:
                        for l in the_log[key][j]:
                            # check for duplicate values
                            if k == l:
                                return "error"
    return the_log



if __name__ == "__main__":
    main()
