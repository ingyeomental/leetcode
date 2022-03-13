class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def subParenthesis(p, o, c):
            if o < c or o > n:
                return
            elif o == n and c == n:
                ans.append(p)
            else:
                subParenthesis(p + "(", o + 1, c)
                subParenthesis(p + ")", o, c + 1)
        
        subParenthesis("", 0, 0)
        
        return ans