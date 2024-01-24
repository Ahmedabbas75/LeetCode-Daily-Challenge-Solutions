class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:

        tpse = Counter(zip(*grid))                

        grid = Counter(map(tuple,grid))            

        return  sum(tpse[t]*grid[t] for t in tpse) 

    
        