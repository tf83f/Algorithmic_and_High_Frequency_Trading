
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()

        def insert_dict(current_dict: dict, index:int, product:str) -> dict:
            letter = product[index]
            if letter not in current_dict:
                current_dict[letter] = dict()
            next_dict = current_dict[letter]
            if index == len(product)-1:
                next_dict['word'] = product
                #print(product)
            return next_dict
       
        def insert(product):
            dict_to_fill = trie
            for index in range(len(product)):
                dict_to_fill = insert_dict(dict_to_fill, index, product)
        
        def find(product):
            found = []
            dict_to_search = trie
            for letter in product:
                dict_to_search = dict_to_search.get(letter, -1)
                if dict_to_search == -1:
                    return found
            
            def search(dict_to_scan):
                for key, value in dict_to_scan.items():
                    if key == 'word':
                        found.append(value)
                    else:
                        search(value)
            search(dict_to_search)
            found = sorted(found)
            if len(found) > 3:
                return found[:3]
            return sorted(found)

        for product in products:
            insert(product)
        #print(trie)
        
        solution = []
        for i in range(1, len(searchWord)+1):
            solution.append(find(searchWord[:i]))
        return solution
        
    ###################

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)       # required characters and counts
        have = {}               # current window characters
        required = len(need)    # number of unique chars we need
        formed = 0              # number of unique chars matched with correct count
        
        l = 0
        ans = (float('inf'), None, None)  # (window length, left index, right index)
        
        for r, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            
            # If char's count matches target count, we have one more satisfied char
            if ch in need and have[ch] == need[ch]:
                formed += 1
            
            # Shrink window from the left while it's valid
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove leftmost char from window
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

         
        for i in range(len(s)):
            if s[i] in mp.keys():
                mp[s[i]].remove(min(mp[s[i]]))
                mp[s[i]].append(i)
                

            minimum = min([min(v) for v in mp.values()])
            maximum = max([max(v) for v in mp.values()])
            if minimum >= 0:
                if (maximum - minimum) < substring:
                    mini = minimum
                    maxi = maximum
                    substring = maxi - mini
              
        
        if substring == len(s)+1:
            return ""
        else:
            return s[mini:maxi+1]

#################


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)       # required characters and counts
        have = {}               # current window characters
        required = len(need)    # number of unique chars we need
        formed = 0              # number of unique chars matched with correct count
        
        l = 0
        ans = (float('inf'), None, None)  # (window length, left index, right index)
        
        for r, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            
            # If char's count matches target count, we have one more satisfied char
            if ch in need and have[ch] == need[ch]:
                formed += 1
            
            # Shrink window from the left while it's valid
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove leftmost char from window
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

         
        for i in range(len(s)):
            if s[i] in mp.keys():
                mp[s[i]].remove(min(mp[s[i]]))
                mp[s[i]].append(i)
                

            minimum = min([min(v) for v in mp.values()])
            maximum = max([max(v) for v in mp.values()])
            if minimum >= 0:
                if (maximum - minimum) < substring:
                    mini = minimum
                    maxi = maximum
                    substring = maxi - mini
              
        
        if substring == len(s)+1:
            return ""
        else:
            return s[mini:maxi+1]


########################

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l1, l2 = len(s1), len(s2)
        for i in range(0, l2-l1+1):
            if s2[i] in c1:
                if c1 == Counter(s2[i:i+l1]):
                    return True
        return False


##################


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result


#####################


from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        visited = {0}
        queue = deque()
        queue.append(0)

        def visit(start):
            for word in wordDict:
  
                if (end := start+len(word)) <= len(s):
 
                    if s[start:end] == word:
                        if end not in visited:
                            queue.append(end)
                            visited.add(end)
                            dp[end-1] = True
                   
                

        while queue:
        
            visit(queue.popleft())




        return dp[len(s)-1] 



#################



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            temp = []
            for coin in coins:
                if ((i - coin) >= 0) and (dp[i - coin] != -1):
                    temp.append(dp[i - coin]+1)
            if temp:
                dp[i] = min(temp)
                
        return dp[amount]



########################

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._hasNext = self.iterator.hasNext()
        self._next = None
        if self._hasNext:
            self._next = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        
    def next(self):
        """
        :rtype: int
        """
        value = self._next
        self._hasNext = self.iterator.hasNext()

        self._next = self.iterator.next() if self._hasNext else None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._hasNext
###############

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        return [element[0] for element in Counter(nums).most_common(k)]


############


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])

        def clean_grid(i, j):
            if 0 <= i and i < row and 0 <= j and j < column and grid[i][j] == "1":
                grid[i][j] = "0"
                clean_grid(i-1, j)
                clean_grid(i+1, j)
                clean_grid(i, j-1)
                clean_grid(i, j+1)
            return 

        number = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1":
                    number += 1
                    clean_grid(i, j)
        return number


##################

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        Pacific = [[False] * m for _ in range(n)]
        Atlantic = [[False] * m for _ in range(n)]

        def propagate(x, y, visited, previous_height):
            if x < 0 or x >= n or y < 0 or y >= m or heights[x][y] < previous_height or visited[x][y]:
                return 
            visited[x][y] = True

            propagate(x-1, y, visited,heights[x][y])
            propagate(x+1, y, visited,heights[x][y])
            propagate(x, y-1, visited,heights[x][y])
            propagate(x, y+1, visited,heights[x][y])
        
        for i in range(n):
            propagate(i,0, Pacific, 0)
            propagate(i,m-1, Atlantic, 0)

        
        for j in range(m):
            propagate(0,j, Pacific, 0)
            propagate(n-1,j, Atlantic, 0)

        solution = []
        for i in range(n):
            for j in range(m):
                if Pacific[i][j] and Atlantic[i][j]:
                    solution.append([i,j])
        return solution


##############


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)




        

            
            


            
