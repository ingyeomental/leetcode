class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dic = {}
        
        for i in range(len(strs)):
            st = strs.pop()
            st_sort = ''.join(sorted(st))
            
            if st_sort not in tmp_dic.keys():
                tmp_dic[st_sort] = [st]
            else:
                tmp_dic[st_sort].append(st)
                
        return list(tmp_dic.values())