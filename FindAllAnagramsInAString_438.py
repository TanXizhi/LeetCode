#滑动窗口
class Solution1:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        
        res = []
        s_count = [0]*26
        p_count = [0]*26
        for i in range(lp):
            s_count[ord(s[i])-ord('a')] += 1
            p_count[ord(p[i])-ord('a')] += 1
        
        if s_count == p_count:
            res.append(0)
        
        for i in range(ls-lp):
            s_count[ord(s[i])-ord('a')] -= 1
            s_count[ord(s[i+lp])-ord('a')] += 1

            if s_count == p_count:
                res.append(i+1)

        return res
            

#优化滑动窗口
class Solution2:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        
        res = []
        count = [0]*26
        for i in range(lp):
            count[ord(s[i])-ord('a')] += 1 #s中的字母对应的字母个数都+1
            count[ord(p[i])-ord('a')] -= 1 #p中的字母对应的字母个数都-1
        
        differ = [c != 0 for c in count].count(True)
        
        if differ == 0:  # 如果差异个数为0 则说明此时个数相等
            res.append(0)
        
        for i in range(ls-lp):
            #窗口右移，最左边的元素s[i]要弹出窗口
            #这里只考虑count中对应的值为1和0的情况，是因为窗口右移只弹出一个字母，count对应的那个值会减1，只有当原先那个值为1和0时，differ才会发生变化
            if count[ord(s[i])-ord('a')] == 1: #窗口中字母s[i]的数量与字符串p中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i])-ord('a')] == 0: #窗口中字母s[i]的数量与字符串p中的数量从相同变得不同
                differ += 1
            count[ord(s[i])-ord('a')] -= 1

            #窗口右移，最右边的元素s[i+lp]要加进窗口
            if count[ord(s[i+lp])-ord('a')] == -1: #窗口中字母s[i+p_len]的数量与字符串p中的数量从不同变得相同
                differ -= 1
            elif count[ord(s[i+lp])-ord('a')] == 0:  #窗口中字母s[i+p_len]的数量与字符串p中的数量从相同变得不同
                differ += 1
            count[ord(s[i+lp])-ord('a')] += 1

            if differ == 0:  # 如果差异个数为0 则说明此时个数相等
                res.append(i+1)

        return res


#下面两种方法超时，但思路也可参考
class Solution3:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []

        res = []
        for i in range(ls-lp+1):
            counts = [0]*26
            for word in s[i:i+lp]:
                counts[ord(word)-ord('a')] += 1
            for word in p:
                counts[ord(word)-ord('a')] -= 1
            if counts == [0]*26:
                res.append(i)          
        return res

class Solution4:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []

        res = []
        for i in range(ls-lp+1):
            if sorted(s[i:i+lp]) == sorted(p):
                res.append(i)        
        return res