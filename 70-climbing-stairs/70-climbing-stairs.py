class Solution:
    def climbStairs(self, n: int) -> int:
        mem_dict = {0: 1, 1: 1, 2: 2, 3: 3}
        
        def dp(x: int) -> int:
            if x in mem_dict:
                return mem_dict[x]
            
            tmp = dp(x-1) + dp(x-2)
            mem_dict[x] = tmp
            
            return tmp
        
        return dp(n)