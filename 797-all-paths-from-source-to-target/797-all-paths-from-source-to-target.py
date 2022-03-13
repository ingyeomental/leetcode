class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        ans = []
        
        def subPath(sub_graph):
            
            if sub_graph[-1] == n-1:
                ans.append(sub_graph)
                
            else:
                final_node = sub_graph[-1]
                
                next_node = graph[final_node]
                
                for i in next_node:
                    subPath(sub_graph + [i])
                    
                    
        subPath([0])
        
        return ans