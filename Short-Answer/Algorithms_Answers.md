#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -

This loop runs while a is less than N*N*N
BUT A is set equal to a + N*N in each loop. So the loop is entirely based on n. If n 3, the loop runs 3x. 

loop 1
a = 0 --> 9
n = 3 

loop 2
a = 9 --> 18
n = 3

loop 3
a = 18 --> 27
n = 3

loop ends


b) O (n log n)

There are two loops here. For every first loop, for i in range(n)is tied to n so as n gets bigger so does the time O(n)

The nested inner loop runs only when j < n and j is doubled every loop. 


This would usually be O(n^2), BUT the nested inner loop only runs when j is less than n and j doubles every loop we run until it hits maximum n. As input n increases, the # of j loops increases at a  SLOWER rate of n. 

Therefore this is O(n log n)



c) O(n) - it iterates a recursive call once for every number from n to 0, if bunnies is 1, runs 1x, if bunnies is 2, runs 2x, etc. It's linear! The recursion is based on bunnies decreasing by 1 until 0 is hit. 

## Exercise II


On a sorted n of stairs, a binary search approach would be my approach. This has a runtime complexity of O(log n).

It works the following way

1. Create a function named binary search which receives an input of n stories

You have eggs that are unlimited and floors that are unlimited

Create a variable isBroken to keep track of whether the egg is broken or not

2. Find the midpoint of n and select that middle floor. 

low = 0
high = len(n)-1
midpoint floor = (high - low) //2

3. Create a while loop to perform only while is_ broken is false

3. Through an egg out to see if it breaks


4. If it breaks --> we know that f floor is below us. Update our data to only include those floors, setting the array to 0 to midpoint -1

The array should be set equal to 
arr[:midpoint]
- The high is now the middle - 1
- The low is still 0


If it doesn't break --> we know f floor is above us. Update our data to only include those floors.

The array should now be equal tp arr[midpoint:]
- The low is now middle + 1
- The high is still len(n)-1

5. Take our new halved array and recursively call binary search on it

6. Do this until we hit a base case of 2 remaining floors or n =2

At this point, we'll either be on a floor where a) isBroken is true OR b) isBroken is not true, so use an if/else conditional to return return the f number of floors if it's broken