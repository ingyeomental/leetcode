class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem_dict = {0 : 0, 1: 0}
        
        def dp(x: int) -> int:
            
            if x in mem_dict:
                return mem_dict[x]
            
            cost_val_1 = dp(x-1) + cost[x-1]
            cost_val_2 = dp(x-2) + cost[x-2]
            
            min_cost = min(cost_val_1, cost_val_2)
            
            mem_dict[x] = min_cost
            
            return min_cost
        
        
        return dp(len(cost))
            
