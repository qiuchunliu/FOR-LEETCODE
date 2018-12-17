# 只出现一次的数字

a = [3, 3, 5, 4, 6, 5, 7, 4, 6, 8, 8, 9, 9, 0, 0]
'''
for i in a:
    if a.count(i) == 1:
        print(i)
        break
    # 运行时间过长
'''
aa = set(a)
print(sum(list(aa))*2-sum(a))

