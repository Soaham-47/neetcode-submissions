class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        result=[]
        q=deque()
        for i in range(k):
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
        l,r=0,k-1
        while r<n:
            result.append(q[0])
            if nums[l]==q[0]:
                q.popleft()
            l+=1
            if r+1<n:
                while q and q[-1]<nums[r+1]:
                    q.pop()
                q.append(nums[r+1])
            r+=1
        return result
            



                

        




        