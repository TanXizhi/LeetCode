class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        for prefix in zip(*strs):  # 列表中字符串按照索引顺序将同位置的字符打包成元组
            prefix_set = set(prefix)  # 由于集合的无序和不可重复性，将以上元组转换成集合，只保留唯一不重复字符
            if len(prefix_set) == 1:  # 如果集合长度为1，说明列表中同位置字符串的字符相同
                ans += prefix[0]
            else:
                break
        return ans
