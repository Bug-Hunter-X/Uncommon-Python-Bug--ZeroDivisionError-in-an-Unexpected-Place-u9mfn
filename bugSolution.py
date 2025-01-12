def function_with_uncommon_error_solved(x):
    if x == 0:
        return float('inf') #Handle zero division error. 
    else:
        return x + 1