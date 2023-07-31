from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        depend = defaultdict(list)
        cnt = Counter()
        for i in range(n):
            for ing in ingredients[i]:
                depend[ing].append(recipes[i])
            cnt[recipes[i]] = len(ingredients[i])

        ans = list()
        q = deque(supplies)

        while q:
            cur = q.popleft()
            if cur in depend:
                for rec in depend[cur]:
                    cnt[rec] -= 1
                    if cnt[rec] == 0:
                        ans.append(rec)
                        q.append(rec)
        return ans







sol = Solution()
print(sol.findAllRecipes(recipes=["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]))
print(sol.findAllRecipes(recipes=["bread", "sandwich"], ingredients=[["yeast", "flour"], ["bread", "meat"]],
                         supplies=["yeast", "flour", "meat"]))
print(sol.findAllRecipes(recipes=["bread", "sandwich", "burger"],
                         ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                         supplies=["yeast", "flour", "meat"]))

print(sol.findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
                         [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                          ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"],
                          ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]],
                         ["f", "hveml", "cpivl", "d"]))
