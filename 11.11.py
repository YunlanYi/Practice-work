# 牛牛去超市采购零食，超市正在做促销活动。已知牛牛一共买了 T 组商品，请你帮他算一算，每组商品最终需要付多少钱。
# 优惠规则如下：
# 对于每一组商品，如果购买的总数量 n 是奇数，那么这组商品的总价可以减去 5 元（如果是偶数则无此优惠）。
# 经过第一步减免后的总价，如果大于等于 100 元，则打 8 折（乘以 0.8）；如果大于等于 50 元但不足 100 元，则打 9 折（乘以 0.9）；不足 50 元不打折。
# 最终支付金额如果出现小数，保留两位小数。
# 【输入描述】
# 第一行输入一个正整数（ 1≤T≤10)，表示有T 组数据。
# 接下来 T 行，每行输入两个数：第一个是购买数量 n（正整数），第二个是商品单价 price（可能带有小数）。
# 【输出描述】
# 对于每组数据，输出一行，表示最终需要支付的金额（保留两位小数）
def suan():
    T = int(input())
    for i in range(T):
        n,price = map(float,input().split())
        n = int(n)
        b = n*price
        if n%2 ==1:
            b -=5
        if b >= 100:
            b*=0.8

        elif 50<=b<100:
            b*=0.9
        print(f"{b:.2f}")          


    # suan ()
# 【题目描述】
# 牛牛是班级的课代表，老师让他统计一下某次考试的成绩。已知班上一共有  n 名同学，请你帮牛牛写一个程序，完成以下三项任务：
# 找出全班最高分。
# 找出全班最低分。
# 统计出及格人数（分数大于等于 60 分即为及格）。

# 【输入描述】
# 第一行输入一个正整数 n (1≤n≤100)，表示班级人数。
# 第二行输入 n 个正整数，表示这  n 个同学的成绩（用空格隔开，成绩在 0 到 100 之间）。

# 【输出描述】
# 输出三行，分别表示：
# 第一行：最高分: X
# 第二行：最低分: Y
# 第三行：及格人数: Z
def feng():
    n = int(input())
    c = list(map(float,input().split()))
    max_c = max(c)
    min_c = min(c)
    b = 0
    for s in range(n):        
        if c[s] >=60:
            b += 1
    print(f'最高分:{max_c}')
    print(f'最低分:{min_c}')
    print(f'及格人数:{b}')



# 题目：第一个重复出现的数字
# 【题目描述】
# 牛牛拿到了一串数字。他想知道，按顺序看过去，第一个重复出现的数字是哪一个？
# 比如序列是 5 2 7 2 5，第一个重复出现的数字是 2（因为 2 第二次出现比 5 第二次出现要早）。
# 如果所有数字都不重复，请输出 None。
# 【输入描述】
# 第一行输入一个正整数 
# n
# n（1≤n≤1000），表示数字的个数。
# 第二行输入 n个正整数，用空格隔开。
# 【输出描述】
# 输出第一个重复出现的数字。如果没有重复的数字，输出 None。
def chonfu ():
    n = int(input())
    c = list(map(int,input().split()))

    a = []
    found = False
    for i in c:
        if i in a:
            print(i)
            found = True
            break
        else:
            a.append(i)
    if not found:
        print(None)


# 题目：牛牛的密码强度验证
# 【题目描述】
# 牛牛在注册一个网站时，网站要求他设置一个密码。为了保证账号安全，密码必须满足以下所有条件：
# 密码长度至少为 8 位。
# 密码中必须包含至少一个大写字母（A-Z）。
# 密码中必须包含至少一个小写字母（a-z）。
# 密码中必须包含至少一个数字（0-9）。
# 请你写一个程序帮牛牛判断，他输入的密码是否合格。
# 如果合格，输出 Valid；如果不合格，输出 Invalid。
# 【输入描述】
# 一行，输入一个字符串（不带空格），表示牛牛设置的密码。
# 【输出描述】
# 输出 Valid 或 Invalid。

def nima():
    print("请输入：")
    password = input()
    if len(password)<8:
        print('Invalid')
    else:
        has_upper = False
        has_lower = False
        has_digit = False
        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
        if has_upper and has_lower and has_digit:
            print('Valid')
        else:
            print('Invalid')



# 【题目描述】
# 牛牛收到了一串神秘的混杂字符串，里面包含英文字母、标点符号和数字。牛牛需要把里面所有的连续数字提取出来，并计算它们的总和。
# 比如字符串 "a1b23c456" 中，数字有 1、23、456，它们的和是 1 + 23 + 456 = 480。

# 【输入描述】
# 一行字符串（可能包含字母、数字、符号，不含空格），长度不超过 1000。

# 【输出描述】
# 输出一个整数，表示字符串中所有数字的总和。



print('请输入')
n = map(input().split())
C = []
for i in n:
    if i.isdigit():
        C.append(i)
b = 0
if r in range(C):
    b += r
    print (b)
