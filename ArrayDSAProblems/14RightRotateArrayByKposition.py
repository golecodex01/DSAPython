'''
14. Rotate the array right by K positions 
Input: 
A = [10, 20, 30, 40, 50] 
K = 2 
Output: 
[40, 50, 10, 20, 30] 

'''

def rightrotate(nums, k):
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        print(nums)
data=list(map(int,input("Enter Your Array Elements :: ").split()))
rightrotate(data,2)