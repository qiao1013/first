""" 
字符串相关的处理工具
"""

def str_reverse(s):       #接收传入字符串，将字符串反转返回
    return s[::-1]
def substr(s,x,y):          #按照下标x和y，对字符串s进行切片
    return s[x:y:1]

