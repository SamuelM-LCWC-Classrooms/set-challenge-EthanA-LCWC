def task(): # Hint - you may need to create new, mid-point sets for the individuals, then combine them
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}

    duplicate_fruits = None # This should be a tuple containing all the fruits in both tuples
    individual_fruits = None # This should be a tuple containing only the individual fruits

    
    duplicate_fruits = fruits_1.intersection(fruits_2)
    individual_fruits = fruits_1.symmetric_difference(fruits_2)
    individual_fruits.discard("sprite")
    individual_fruits.discard("steak")

    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list
