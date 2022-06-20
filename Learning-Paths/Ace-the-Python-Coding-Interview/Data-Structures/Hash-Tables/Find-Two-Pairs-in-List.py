"""
In this problem, you have to implement the find_pair() function which will find two pairs, [a, b] and [c, d], in a list such that :

a+b = c+d
a+b=c+d

You only have to find the first two pairs in the list which satisfies the above condition.

Sample input:
  my_list = [3, 4, 7, 1, 12, 9]
 
Sample output:
  [[4,12],[7,9]]

"""
def find_pair(my_list):
    
    d = {}

    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):

            current_pair = [my_list[i], my_list[j]] 
            current_sum = sum(current_pair)

            if current_sum not in d:
                d[current_sum] = current_pair
            else:

                return [d[current_sum], current_pair]
    
    return []
