"""
There is a grid of size 10^5×10^5, covered completely in railway tracks. Tom is riding in a train, currently in cell (a,b), and Jerry is tied up in a different cell (c,d), unable to move. The train has no breaks. It shall move exactly K steps, and then its fuel will run out and it shall stop. In one step, the train must move to one of its neighboring cells, sharing a side. Tom can’t move without the train, as the grid is covered in tracks. Can Tom reach Jerry’s cell after exactly K steps?
Note: Tom can go back to the same cell multiple times.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, five integers a,b,c,d,K.
Output
For each testcase, output in a single line "YES" if Tom can reach Jerry's cell in exactly K moves and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints
1≤T≤105
0≤a,b,c,d≤105
(a,b)≠(c,d)
1≤K≤2⋅105
Subtasks
Subtask #1 (100 points): original constraints

Sample Input
3
1 1 2 2 2
1 1 2 3 4
1 1 1 0 3
Sample Output
YES
NO
YES
Explanation
Test Case 1: A possible sequence of moves is (1,1)→(1,2)→(2,2).

Test Case 2: There is a possible sequence in 3 moves, but not in exactly 4 moves.

Test Case 3: A possible sequence of moves is (1,1)→(1,0)→(0,0)→(1,0).
"""
"""
The total steps that we need to take is equal to, steps = abs(d-b) + abs(c-a).
if k < steps, no path possible.
if k == steps, return 'YES'
if k > steps,
since we can return to previous cells, we must have (k-steps) as an even number, so we can move away and return to the required cell.
i,e. (k-steps)%2==0
"""
# cook your dish here
t = int(input())
for tc in range(t):
    l = list(map(int,input().split()))
    a,b = l[0],l[1]
    c,d = l[2],l[3]
    k = l[-1]
    steps = abs(d-b)+abs(c-a)
    if steps == k:
        print('YES')
    elif k < steps:
        print('NO')
    else:
        rem = k - steps
        if rem%2==0:
            print('YES')
        else:
            print('NO')






























