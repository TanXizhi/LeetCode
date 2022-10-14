class Solution1:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):  #总油量必须大于等于总消耗量，否则不能完成绕行
            return -1

        n = len(gas) 
        container = 0   
        start = 0
        for i in range(n):
            container += gas[i] - cost[i]   #记录到达i的下一站时的剩余油量
            if container < 0:     #如果到达i的下一站时的剩余油量为负，则就以i的下一站为起点重新计算
                container = 0
                start = i+1      
        return start
"""
起点为什么选择i+1而不考虑i之前的站点？
因为汽车到达0->i之间的每一个站点时的container肯定都是大于0的，如果当一个大于0的container值加上当前的gas都不能完成的话，
那么当container为0时即以0->i之间的站点作为起点的话是更加不能完成的。所以应该考虑将i的下一站作为新起点
"""

#以下解法超时，但是也能获得正确解
class Solution2:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas) 
        for i in range(n):   #考虑从每一个点出发，循环一圈到出发的站点
            container = gas[i]
            j = i
            while container >= cost[j]:  #当前剩余的油大于即将消耗的油时才能到下一个站点
                container += gas[(j+1)%n] - cost[j]  #到下一个站点剩余的油=即将消耗的油+新的站点的补给
                j = (j+1)%n    #标记新的站点index
                if j == i:
                    return i 
        return -1  #以上所有站点都不可以的话返回-1
