class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ss = s.split()[-1]
        return len(ss)


class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        ss = list(s.strip())
        i = 0
        for j in range(len(ss)):
            if ss.pop() != ' ':
                i += 1
            else:
                break
        return i


class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        ss = list(s.strip())
        i = 0
        while len(ss) > 0 and ss.pop() != ' ':
            i += 1
        return i
