


# provides function my_averages that takes a dataframe containing numbers as input
# and returns the average for each row

import pandas as pd

def my_averages_a_b( indata : pd.DataFrame) -> pd.DataFrame :
    """to make it simple: indata must have columns "a" and "b"
    """
    result = indata.copy()
    result["average"] = (indata["a"] + indata["b"]) / 2.0
    return result


# test in Terminal: python compute_averages.py
#
if __name__ == "__main__" :
    mydata = pd.DataFrame([[1,1],[2,4]],columns=["a","b"])
    print(mydata)
    print(my_averages_a_b(mydata))
    
    