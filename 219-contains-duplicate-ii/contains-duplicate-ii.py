class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = deque()
        for i in range(len(nums)):
            if nums[i] in data: return True
            data.append(nums[i])
            if len(data) > k: data.popleft()
        return False