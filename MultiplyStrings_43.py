class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m = len(num1)
        n = len(num2)
        store = [0] * (m+n) #用于存储num1的第i位和num2的第j位相乘的结果, 乘积中的位置是[i+j, i+j+1]
        for i in range(m - 1, -1, -1):  #从右至左开始计算，先乘再累加到对应的位置存储
            for j in range(n - 1, -1, -1):
                store[i+j+1] += int(num1[i]) * int(num2[j])
        
        for i in range(m+n-1, -1, -1): 
            store[i-1] += store[i] // 10  #注意整除和取余的顺序不能颠倒
            store[i] %= 10
        
        if store[0] == 0:  #如果最高位为0，则舍弃最高位
            index = 1
        else:
            index = 0 
        return ''.join(str(x) for x in store[index:])

