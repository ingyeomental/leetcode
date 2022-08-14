class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        n = len(edges)
        cnt = defaultdict(int)
        ans = 0
        
        for i in range(n):
            cnt[edges[i]] += i

        m = max(cnt.values())
        
        for i in range(n):
            if cnt[i] == m:
                ans = i
                break
        
        return ans