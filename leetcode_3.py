## 给定一个字符串，找出不含有重复字符的最长子串的长度。
#示例：
#给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#给定 "pwwkew" ，最长子串是 "wke" ，长度是3。

s = 'qqqhvykfjhnlhgktqq'
res = 0
if s is None or len(s) == 0:
    print (res)
d = {}
tmp = 0
start = 0
for i in range(len(s)):
    if s[i] in d and d[s[i]] >= start:
        start = d[s[i]] + 1
    tmp = i - start + 1
    d[s[i]] = i
    res = max(res, tmp)
print (res)
