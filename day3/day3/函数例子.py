s='1.1'
s1='-0.1'
#1、必须只有一个小数点
#2、小数点的左边必须是整数，小数点的右边必须是正整数
def is_float1(s):
    s = str(s) #.1
    if s.count('.')==1:
        left,right = s.split('.') #['-','1']
        if left.isdigit() and right.isdigit():#正小数
            return True
        elif left.startswith('-') and left.count('-')==1 and right.isdigit():
            #先判断负号开头，只有一个负号，小数点右边是整数
            lleft = left.split('-')[1] #如果有负号的话，按照负号分隔，取负号后面的数字
            if lleft.isdigit():#
                return True
    return False


# def is_float(s):
#     s = str(s)
#     if s.count('.') == 1:  # 判断小数点个数
#         left,right = s.split('.')  # 按照小数点进行分割
#         if left.startswith('-') and left.count('-') == 1 and right.isdigit():
#             lleft = left.split('-')[1]  # 按照-分割，然后取负号后面的数字
#             if lleft.isdigit():
#                 return True
#         elif left.isdigit() and right.isdigit():
#             # 判断是否为正小数
#             return True
#     return False
#
# print(is_float('-.1'))

