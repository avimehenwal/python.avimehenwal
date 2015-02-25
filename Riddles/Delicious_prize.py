"""Multunus Hiring Challenge
Lissa has just won the HackerEarth Online Coding Contest. Kuldeep decided to offer her N chocolate boxes each containing at least one chocolate in it. But he knows that Lissa does not like chocolates very much so he wants to place chocolates in the boxes such that the total number of chocolates is minimum.
Given a number N denoting the number of boxes and a number K denoting the product of the number of chocolates in the N boxes, you need to tell Kuldeep the minimum of total number of chocolates that can be placed in the boxes.

INPUT:
First line of input contains an integer T denoting the total number of test cases.
Each test case consists of a single line containing two space separated integers N and K denoting the number of boxes and the product of the chocolates in n boxes.

OUTPUT:
Output consists of T lines each containing an integer denoting the minimum of total number of chocolates in the N boxes.
CONSTRAINTS:
T<=1000
N<=1000
K<=10^9

Sample Input (Plaintext Link)
4
2 24
3 24
3 60
4 60
Sample Output (Plaintext Link)
10
9
12
12
Explanation
test1: 1st box contains 6 chocolates and 2nd box contains 4 chocolates . So, the total number of chocolates in N boxes are 10 and their product is 24. 

test2: 1st box contains 4 chocolates and 2nd box contains 3 chocolates and 3rd box contains 2 chocolates.So, the total number of chocolates in N boxes are 9 and their product is 24.
Time Limit 1 sec(s) (Time limit is for each input file.)
Memory Limit256 MB
Source Limit1024 KB
"""


def tuple_count(tup):
    if not isinstance(tup, tuple):
        print("%s is not tuple type. Error")
        return False
    count = 0
    for i in tup:
        if isinstance(i, int):
           count += i
        else:
            print("Skipping %d as not integer type"%(i))
            continue
    return count

def delicious_prize(n):
    ##N no of boxes
    ##K product number of chocklates in N boxes 
    ##T total no of test cases
    print("n = ", n)
    if not isinstance(n, int):
        print("Not integer type. Only int accepted. Aborting")
        return False
    elif not n <= 1000:
        print("Inpute n: %s is not in range. Should be less than or equal to 1000"%(n))
        exit
    elif n < 0:
        print("No of boxes cannot be negative. Taking positve magnitude as %s"%(abs(n)))
        n = abs(n)
    elif n == 0:
        print("No chocklate boxes offered !")
        exit
    
    num_list = []
    for i in range(n):
        num = input("Enter no of chocklates in %sth box : "%(i))
        num_list.append(int(num))
    num_tuple = tuple(num_list)
    print(num_tuple)
    return tuple_count(num_tuple)


if __name__=='__main__':

##    print(delicious_prize(2))
##    print(delicious_prize(0))
##    print(delicious_prize(-3))
##    print(delicious_prize('wqete'))

    from unittest import mock
    with mock.patch('__main__.input', create=True) as mocked_input:
        mocked_input.side_effect = [4, 5, 6]
        delicious_prize(3)
