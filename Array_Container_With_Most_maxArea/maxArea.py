"""
Array
Problem : Container With Most Water (maxArea)
    You are given an integer array height of length n. There are n vertical lines
    drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water. Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Algorithm : function => maxArea2 
    1: Find => low index = 0 , high index = len(array) - 1 , for starting volume=0 
    2: Repeat till low >= high , 
    3: if array index low > from array index high => v=(high-low)*array[high] (v=>value)
       if array index low < from array index high => v=(high-low)*array[low]
    4: if v > from volume => volume=v (it save only the biggest volume)
    5: if array index low < from array index high (low + 1) and back to third step (3:)
       if array index low > from array index high (high + 1) and back to third step (3:)

Function maxArea1 is working only the function spends too much time and 
failed on the website leetcode.com with Time Limit Exceeded

on the website => leetcode.com (maxArea2 resalt)
Runtime
Details
558ms
Beats 92.91%of users with Python

Memory
Details
23.67mb
Beats 98.00%of users with Python

"""

def maxArea1(array):
    volume=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]>array[j]:                
                v=(j-i)*array[j]
            else:
                v=(j-i)*array[i]
            if v>volume:
                volume=v
    return volume

def maxArea2(array):
    low = 0
    high = len(array) -1
    volume = 0     
    while low < high:
        if array[low]>array[high]:                
            v=(high-low)*array[high]
        else:
            v=(high-low)*array[low]
        if v>volume:
            volume=v
     
        if array[low] < array[high]:
            low += 1
        else:
            high -= 1
    return volume


array = range(10000)
print(maxArea2(array))   
    
    

  

 



