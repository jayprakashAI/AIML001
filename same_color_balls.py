#same_color_balls.py

"""
The problem statement goes below
    There is bag that contains 3 colours of ball (Red, Green & Blue)
    Numbers of ball count of each colours are A, B, and C respectively
    We will 3 picks and in each pick we will take 2 balls out and we won’t replace the picked balls for subsequent picks or draws.
    We wanted to find out the probability of picking same of colour of balls in 3rd draw.
    You are NOT allowed to use “conditional probability” formulae to solve this, instead solve algorithmically using data structure.
"""


import numpy as np
import random
# Let's prepare the  container which will have coloured balls
# in our case we will use dictionary to be container 
# This container helps in labeling the ball's color & choose a random color
d ={}
A=100 # Enter value more than 2 
B=243 # Enter  value more than 2
C=51 # Enter  value more than 2
for i in range(A+B+C):
    if i < A:
        d[i] = 'red'
    elif i > (A-1) and i < (A+B):
        d[i] = 'green'
    else:
        d[i] = 'blue'

# setup the conditional probability parameters
no_of_simulations = 3
part_a_total = 0
repeatKeys=[]
for i in range(no_of_simulations):

    #make a list of the colors  that we choose
    lst = []
    keyss=[]
    for j in range(2):

        k = random.randint(0,(A+B+C-1))
        # random key is duplicate so generate it again
        while k in repeatKeys:
            k = random.randint(0,(A+B+C-1))
        repeatKeys.append(k)
        keyss.append(k)
        print('repeatKeys',repeatKeys)
        lst.append(d[k])

    #convert list of chosen balls to a numpy array
    lst = np.array(lst)

    #find the number of each that we picked
    redballs = sum(lst=='red')
    greenballs=sum(lst=='green')
    blueballs=sum(lst=='blue')

    # Verify if the combination of balls is all same color
    if (redballs==2 or greenballs==2 or blueballs==2) and (i==2):
        part_a_total+=1
    print("keyss",keyss)
    print("total same color balls",part_a_total)
    print("colors choosen",lst)
    probability_same_color = part_a_total/len(d) ## Computing the probability for given sample space.
    for r in keyss:
        d.pop(r)
print( "The probability of all the same color is: (part_a_total/len(d)) ", probability_same_color * 100, '%')
