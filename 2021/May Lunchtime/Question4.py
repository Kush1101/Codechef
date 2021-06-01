"""
There are N subatomic particles lined up in a row. There are two types: protons and electrons. Protons have a positive charge and are represented by 1, while electrons have a negative charge and are represented by 0.

Our current understanding of physics gives us a way to predict how the particles will be spaced out, if we know their charges. Two adjacent particles will be separated by 1 unit if they have opposite charges, and 2 units if they have the same charge.

When Chef is not in the kitchen, he is doing physics experiments on subatomic particles. He is testing the hypothesis by having N particles in a row, and he will change the charge of a particle K times. In the i-th update, he will change the charge of the Qi-th particle. After each update, find the distance between the first and last particle.

Note: Each update is persistent for further updates.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains three lines of input.
The first line contains two integers N, K.
The second line contains a string S of length N, where Si represents the initial charge on i-th particle.
The third line contains K integers Q1,Q2,…,QK, the positions of the changed particles.
Output
For each test case, output K lines, where the i-th line contains the answer after the updates Q1,…,Qi have been made.

Constraints
1≤T≤5
1≤N,K≤105
S contains only 0 and 1 characters.
1≤Qi≤N
The sum of K over all testcases is at most 2⋅105
Subtasks
Subtask #1 (100 points): original constraints

Sample Input
1
3 3
010
2 1 3
Sample Output
4
3
2
Explanation
Update 1: After reversing the parity of particle 2, the new configuration is 000. Since all the particles have a similar charge, each is separated from the previous by a distance of 2 units. So the location of particle 3 is 2+2=4 units from the first particle.

Update 2: After reversing the parity of particle 1, the new configuration is 100. Here, the charges of particles 1 and 2 differ, so they are separated by 1 unit. The charges of particles 2 and 3 agree, so they are separated by 2 units. So, the location of particle 3 is 1+2=3 units from the first particle.

Update 3: After reversing the charge of particle 3, the new configuration is 101. Here, particles 1 and 2 are separated by 1 unit and particles 2 and 3 are separated by 1 unit. So the location of particle 3 is 1+1=2 units from the first particle.
"""
"""
One of the more interesting problems from the Contets
So here we can ompute the distance after every update, but instead, a flip can affect atmost two partcles on its left and right, and ony one if it is a corner particle,
So we compute the distance initially, then calculate the distance in the window where the update has happened and update the original result.
We need separarte cases for if the particle is the first in the row or if its the last in the row
"""
#cook your dish here
def dist(l):
    d=0
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            d+=2
        else:
            d+=1 
    return d 
t = int(input())
for tc in range(t):
    f = list(map(int,input().split()))
    s=input()
    l = [int(i) for i in s]
    q = list(map(int,input().split()))
    d=dist(l)
    for i in q:
        if i-2<0:
            prev = dist(l[:i+1])
            l[i-1]=1-l[i-1]
            curr=  dist(l[:i+1])

        elif i+1>len(l)-1:
            prev = dist(l[i-2:])
            l[i-1]=1-l[i-1]
            curr = dist(l[i-2:])
        else:
            prev = dist(l[i-2:i+1])
            l[i-1]=1-l[i-1]
            curr = dist(l[i-2:i+1])
        d+=curr-prev
        print(d)






















