class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = row
        
        ans = []
        d = 0

        for r in range(row-2):
            ans_row = []
            for c in range(row-2):
                max_tmp = []
                tmp = grid[r:r+3]
                for i in tmp:
                    max_tmp.extend(i[c:c+3])
            
                ans_row.append(max(max_tmp))
            
            ans.append(ans_row)
            
        return ans
