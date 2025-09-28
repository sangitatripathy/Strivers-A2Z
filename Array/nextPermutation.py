
# def nextPermutation(self, nums) -> None:
#     def gen_permutation(nums,start,res):
#         if(start==len(nums)):
#             res.append(nums[:])
#             return
#         for i in range (start,len(nums)):
#             nums[start],nums[i]=nums[i],nums[start]
#             gen_permutation(nums,start+1,res)
#             nums[i],nums[start]=nums[start],nums[i]
#     res=[]
#     gen_permutation(nums,0,res)
#     res.sort()
#     ind=res.index(nums)
#     nextind=(ind+1)%len(nums)
#     nums[:]=res[nextind]

def permutation(arr):
    n=len(arr)
    i=n-2
    while arr[i+1] <= arr[i]:
        i-=1
    if i >= 0:
        j=n-1
        while arr[j] <= arr[i]:
            j-=1
        temp=arr[j]
        arr[j]=arr[i]
        arr[i]=temp
    arr[i+1:]=reversed(arr[i+1:])
        