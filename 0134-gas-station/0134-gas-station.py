class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalGas, totalCost = 0, 0
        start, currentGas = 0, 0
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            currentGas += gas[i] - cost[i]

            if currentGas < 0:
                start = i + 1
                currentGas = 0
        if totalGas < totalCost:
            return -1
        else:
            return start
        
        
        