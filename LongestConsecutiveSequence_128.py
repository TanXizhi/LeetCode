class Solution1:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_length = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                cur_length = 1
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_length += 1
                max_length = max(cur_length, max_length)
        return max_length


"""
用哈希表存储每个端点值对应连续区间的长度
若数已在哈希表中：跳过不做处理
若是新数加入：
    取出其左右相邻数已有的连续区间长度 left 和 right
    计算当前数的区间长度为：cur_length = left + right + 1
    根据 cur_length 更新最大长度 max_length 的值
    更新区间两端点的长度值
"""
class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash_dict = dict()
        max_length = 0

        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = left + 1 + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num-left] = cur_length
                hash_dict[num+right] = cur_length

        return max_length
