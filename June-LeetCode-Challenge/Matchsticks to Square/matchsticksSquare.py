class Solution(object):
    def makesquare(self, matchsticks):
        if not matchsticks:
            return False
        L = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side =  perimeter // 4
        if possible_side * 4 != perimeter:
            return False
        matchsticks.sort(reverse=True)
        
        def dfs(a,b,c,d,k):
            if k == L:
                if a == b == c == d:
                  return True
                return False
            m = matchsticks[k]
            if a+m <= side and dfs(a+m,b,c,d,k+1):
              return True
            if b+m <= side and dfs(a,b+m,c,d,k+1):
              return True
            if c+m <= side and dfs(a,b,c+m,d,k+1):
              return True
            if d+m <= side and dfs(a,b,c,d+m,k+1):
              return True
            return False
        return dfs(0,0,0,0,0)
        
