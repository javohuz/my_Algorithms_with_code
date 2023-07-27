"""
Array
Problem : twosum
    Given an array of integers nums and an integer target, return indices of the two 
    numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

Algorithm :
    1: Find => low index = 0 , high index = len(nums) - 1
    2: Find summed up the two indexs value = x
    3: repeat till x=target  , if x=target stop and return [low,high] 
    4: if low+1!=high =>  high - 1 and back to second step (2:)
    5: if low==high => high=len(nums)-1 and 
            if low==high => have to stop the repiation (when this time all index value has been checked )
            if low!=high => low + 1 and back to second step (2:)

on the website => leetcode.com
Memory
Details
13.90mb
Beats 98.13%of users with Python

Runtime
Details
4065ms
Beats 13.07%of users with Python

"""

def twosum(nums,target):
    low=0
    high=len(nums)-1
    
    while True:
        x=nums[low]+nums[high]
        if x==target:
            result=[low,high] 
            break

        if low+1!=high :
            high -= 1
        else :
            high=len(nums)-1
            if low==len(nums)-1:
                result= 'Error'
                break
            else :
                low+=1
                
    return result
    

array=[3,2,4]
twosum(array,5)  




















