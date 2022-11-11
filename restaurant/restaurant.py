def main():

    the_log = {
        1: [["a", "b", "c"]],
        2: [["d", "e", "f"]],
        3: [["a", "c", "g"]],
        4: [["h", "j", "k"]],
        5: [["l", "m", "n"]],
        6: [["l", "j", "q"]],
    }

    message = unique_orders(the_log)
    if message != "error":
        top_foods = find_top_foods(the_log)
        print(top_foods)
    else:
        print(message)
        


def unique_orders(the_log):
    '''find if same food is ordererd by the same person more than once'''
    check_log = {}

    for key in the_log.keys():
        check_log[key] = {}
        for order_list in the_log[key]:
            for item in order_list:
                # if the food_id is already present for a particular diner_id, "error" gets returned
                if check_log[key].get(item) != None:
                    return "error"
                else:
                    check_log[key][item] = 0
    return "no error"


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

    # get the list of values and sort them
    the_values = list(count.values())
    the_values.sort(reverse=True)

    # get the key associated with the value.
    for value in the_values:
        for key in count.keys():
            if count[key] == value:
                # add values if there are no more than three values in the set
                if len(most_ordered_food) < 3:
                    most_ordered_food.add(key)

    return most_ordered_food


if __name__ == "__main__":
    main()
