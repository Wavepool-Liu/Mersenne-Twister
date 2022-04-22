from tkinter import N
import re
import json


a = 0
b = 20

h = 20
N = 100000

#B:[5030. 4990. 5130. 5052. 5051. 4919. 4912. 4964. 4966. 5078. 4998. 4933. 5055. 5028. 4928. 4928. 4971. 5105. 5025. 4937]
#A:[4954. 5083. 4883. 4963. 4987. 5105. 4921. 5043. 4937. 5072. 5039. 5088. 5025. 4902. 4926. 4878. 4962. 5124. 5078. 5030]
numsA = "[4954. 5083. 4883. 4963. 4987. 5105. 4921. 5043. 4937. 5072. 5039. 5088. 5025. 4902. 4926. 4878. 4962. 5124. 5078. 5030]"
numsB = "[5030. 4990. 5130. 5052. 5051. 4919. 4912. 4964. 4966. 5078. 4998. 4933. 5055. 5028. 4928. 4928. 4971. 5105. 5025. 4937]"

def listnums(nums):
    strinfo = re . compile('. ')
    nums = json.loads(strinfo.sub(',',nums))
    return nums

def duli(nums):
    v = 0
    for i in range(0,h):
        v = v+ ((nums[i]-(N/h))*(nums[i]-(N/h)))
    return (h/N) *v

def xiangguan(a,b):
    a_avg = sum(a) / len(a)
    b_avg = sum(b) / len(b)
    cov_ab = sum([(x - a_avg) * (y - b_avg) for x, y in zip(a, b)])
    sq = (sum([(x - a_avg) ** 2 for x in a]) * sum([(x - b_avg) ** 2 for x in b])) ** 0.5
    corr_factor = cov_ab / sq
    return corr_factor

m1 = listnums(numsA)
m2 = listnums(numsB)
print(xiangguan(m1, m2))  
