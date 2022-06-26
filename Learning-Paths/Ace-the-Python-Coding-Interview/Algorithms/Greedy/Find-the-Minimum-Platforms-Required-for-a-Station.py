"""
Time: O(n log n)
Space: O(1)
"""

def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    n = len(arrival)

    mx = 0

    c = 0

    for index in range(n):
        for next_train in range(1, n):
            if arrival[index] <= arrival[next_train] < departure[index]:
                c += 1
        
        mx = max(mx, c)
        c = 0
    
    return mx
  
  
  """
  Time: O(n^2)
  Space: O(1)
  """
  def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station

    """
    n = len(departure)

    arrival.sort()
    departure.sort()

    arr_index = 1
    dep_index = 0

    cnt = 1
    mx = 0

    while arr_index < n and dep_index < n:

        if arrival[arr_index] < departure[dep_index]:

            cnt += 1
            arr_index += 1

            mx = max(mx, cnt)

        else:
            cnt -= 1
            dep_index += 1
    
    return mx

           
