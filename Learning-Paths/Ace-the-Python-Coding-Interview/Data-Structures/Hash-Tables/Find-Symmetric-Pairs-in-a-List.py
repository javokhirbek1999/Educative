def find_symmetric(my_list):
    # Write your code here
    
    res = []

    pair_dict = {}

    for pair in my_list:

        pair_tuple = tuple(pair)
        pair.reverse()
        reverse_tuple = tuple(pair)

        if str(reverse_tuple) in pair_dict:
            res.append(list(pair_tuple))
            res.append(list(reverse_tuple))
        else:
            pair_dict[str(pair_tuple)] = 1


    return res
