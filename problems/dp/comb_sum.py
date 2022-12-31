class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for i in range(1, target + 1):
            if i in candidates:
                dp[i].append({i: 1})
            
            for c in candidates:
                if i - c < 0:
                    continue
                new = [dict(d) for d in dp[i - c]]
                for n in new:
                    n[c] = n.get(c, 0) + 1
                    if n not in dp[i]:
                        dp[i].append(n)
    
        ans = []
        for l in dp[-1]:
            level = []
            for x, i in l.items():
                for _ in range(i):
                    level.append(x)
            ans.append(level)
        
        return ans

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c, target+1):
                if i == c: 
                    dp[i].append([c])
                for comb in dp[i-c]: 
                    dp[i].append(comb + [c])
        return dp[-1]