## No.3 题目大意：给出一个字符串，找到最长的没有重复字符的子字符串，并返回该子字符串的长度。
- Given "abcabcbb", the answer is "abc", which the length is 3.
- Given "bbbbb", the answer is "b", with the length of 1.
- Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
1. 第一层循环从字符串的最左侧到最右侧第二个，即for i in range(0,len(s)-1)，第二层循环则从第一层紧跟着的一个到最后一个字符。即for j in range(i+1,len(s));之后通过找出所有不重复的子字符串，比较长度得到最大长度的子字符串。代码如下：（需要注意当字符串长度为0或1的特殊情况）

```
def lengthOfLongestSubstring(self, s):
        max_len = 0 #用这个值记录我们要返回的最长子字符串长度
        #当原字符串长度为0或1的特殊情况
        if (len(s) == 1 or len(s) == 0):
            max_len = len(s)
        #开始遍历每一个子字符串，并进行长度比较，得到最长的那个
        for i in range(0,len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    if j-i > max_len:
                        right = j
                        left = i
                        #这里小詹本想返回对应子字符串的左右索引值，之后发现题目没有要求
                        max_len = right-left
                    break
                elif j == len(s) - 1:
                    if max_len < j - i + 1:
                        max_len = j - i + 1
        return max_len
```
2. 利用字典进行解读

```
def lengthOfLongestSubstring(self, s):
        #创建一个空字典，其存放的形式是“单字符:出现位置的索引”
        indexDict = {}
        #存放记录最大长度和当前循环下的长度
        maxLength = currMax = 0
        for i in range(len(s)):
            #这里是关键，小詹看了挺久的，小伙伴们比我强，应该比较快
            #这里是当s[i]没有在之前出现过，则当前长度currMax自动加一
            #当出现了重复字符，则比较当前找到的子字符串长度和历史最大长度
            #重点是这里i - indexDict[s[i]] - 1 的含义，代表了当前找到子字符串的长度。
            if s[i] in indexDict and i - indexDict[s[i]] - 1 <= currMax:
                if maxLength < currMax:
                    maxLength = currMax
                currMax = i - indexDict[s[i]] - 1
            currMax = currMax + 1                
            indexDict[s[i]] = i 
        return maxLength if currMax < maxLength else currMax
```
