import collections

# 排序
class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 创建散列表用于储存异位词，key为同组异位词的排序后的字符串，values为同组的异位词
        map = collections. defaultdict(list)
        for s in strs:  # 遍历字符串组
            key = ''.join(sorted(s))  # 将同组异位词字符排序
            map[key].append(s)  # 将同组异位词加到字符排序相同的key下，为对应的value值
        return list(map.values())  # 将散列表的values提取出来即位分组后的字母异位词



"""
计数：由于互为字母异位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，
故可以将每个字母出现的次数作为哈希表的键。做法和排序相似
"""
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = collections. defaultdict(list)
        for s in strs:
            counts = [0]*26
            for word in s:
                counts[ord(word)-ord('a')] += 1
            map[tuple(counts)].append(s)
        return list(map.values())
