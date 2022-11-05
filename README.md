## Problem 1
#### (restaurant/restaurant.py)
#### for test (restaurant/test_restaurant.py)

The unique_orders function will return 'no error' if there is no repetition of orders for single eater.
But if there is repetition then it returns 'error'.
It does this by checking whether the key already exists for that eater.
Then the find_top_foods function will only run if unique_orders function returns 'no error'.
This function then checks for the foods that was most ordered and return them.


## Problem 2

#### (node.py)

The children list in the Node class should be made specific to each node, but in the original code it is written as a common list.
In the original code, the same root.children list was getting looped in every recursive call.
There will never be an empty list in any of the recursive calls.
When we make the list specific to each node, the lowermost level of nodes will have empty children lists, and recursion won’t continue further.
