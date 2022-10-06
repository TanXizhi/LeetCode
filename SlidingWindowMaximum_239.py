import heapq
class Solution1:
    def maxSlideWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        que = [(-nums[i], i) for i in range(k)]  # Python默认的优先队列是小根堆（递增），取负号变成大根堆（递减）
        heapq.heapify(que)

        ans = [-que[0][0]]
        for i in range(k, n):
            heapq.heappush(que, (-nums[i], i))
            while que[0][1] <= i-k:
                heapq.heappop(que)
            ans.append(-que[0][0])
        return ans



import collections
class Solution2:
    def maxSlideWindow(self, nums: list[int], k: int) -> list[int]:
        que = collections.deque()
        n = len(nums)
        for i in range(k):
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)

        ans = [nums[que[0]]]
        for i in range(k, n):
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)
            while que[0] <= i - k:
                que.popleft()
            ans.append(nums[que[0]])
        return ans





class MyDeque:
    def __init__(self):
        self.deque = []

    def pop(self, value):
        if self.deque and value == self.deque[0]:
            self.deque.pop(0)

    def push(self, value):
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)

    def front(self):
        return self.deque[0]

class Solution3:
    def maxSlideWindow(self, nums: list[int], k: int) -> list[int]:
        que = MyDeque()
        ans = []
        for i in range(k):
            que.push(nums[i])
        ans.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            ans.append(que.front())
        return ans


        
