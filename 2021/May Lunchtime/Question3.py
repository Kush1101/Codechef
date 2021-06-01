"""
It’s Chef's birthday. He and his twin have received N gifts in total. The i-th gift has a price of Ai. Each twin wants to keep the most expensive gifts for himself.

The twins take K turns alternately (each has K turns, for 2⋅K turns in total). It is given that 2⋅K+1≤N. In a turn, a person may choose one gift. The only exception is the last turn of the twin who moves second, where he gets to choose two gifts instead of one. Assuming they both choose gifts optimally and you can choose who takes the first turn, find the maximum total cost of the gifts that Chef keeps.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains two lines of input.
The first line contains two space-separated integers N, K.
The second line contains N space-separated integers A1,A2,…,AN, the price of the gifts.
Output
For each test case, output in a single line the answer to the problem.

Constraints
1≤T≤100
3≤N≤103
1≤K≤N−12
1≤Ai≤109
Subtasks
Subtask #1 (100 points): original constraints

Sample Input
3
3 1
1 3 2
3 1
3 1 3
5 2
5 1 3 2 4
Sample Output
3
4
8
Explanation
Test Case 1: Chef moves first and he chooses the gift with cost 3. His twin then chooses the gifts of costs 1 and 2.

Test Case 2: Chef allows his brother to choose first and his brother chooses a gift with cost 3. Then Chef chooses the remaining gift with cost 3. Since Chef moves second, he is allowed to choose one more gift, so he chooses gift with cost 1. The total cost of Chef's gifts is 3+1=4.

Test Case 3: Chef moves first and at the end he will have the gifts with costs 5 and 3. Hence, the total cost of gifts with Chef = 5+3=8.
"""
"""
If we sort the array of price from greatest to lowest. The total score for first twin will be the sum of first k elements taken alternatively that is with indices 0,2,...,k
for second twin, sum of k+1 elements at odd indices.
We have to return the maximum between them
"""
def score(l,k):
    first,second=0,0
    l.sort(reverse = True)
    if k==1:
        return max(l[0],l[1]+l[2])
    first= [l[i*2] for i in range(k)]
    second = [l[i*2+1]for i in range(k)]
    second += [l[2*k]]
    return max(sum(first),sum(second))
t = int(input())
for tc in range(t):
    l1 = list(map(int,input().split()))
    n,k = l1[0],l1[1]
    l = list(map(int,input().split()))
    ans = score(l,k)
    print(ans)
















