class Solution:
    def countAndSay(self, n: int) -> str:
        #先设置上一项为‘1’
        prev = '1'
        #开始外循环
        for i in range(1, n):
            #每次外循环先设置当前项为空字符串，待处理的字符num为上一项的第一位，设置出现的次数为1
            curr = ''
            num = prev[0]
            count = 1
            #开始内循环，遍历上一项的数，如果数是和num一致的，则count增加
            #若不一致，则将count和num一同添加到curr项的数中，同时更新num和count
            for j in range(1, len(prev)):
                if prev[j] == num:
                    count += 1
                else:
                    curr += str(count) + num
                    num = prev[j]
                    count = 1
            #最后要记住更新curr的最后两个数为上一项最后一个字符以及出现的次数
            curr += str(count) + num
            prev = curr

        return prev

                

