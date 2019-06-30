import requests
from lxml import etree
import re
import webbrowser


# 解析接口
q_url = 'http://www.qmaile.com/'
r = requests.get(q_url)

# 定义匹配规则
reg = re.compile('<option value="(.*?)" selected="">')
q2_url = re.findall(reg, r.text)


# 解析接口
q_url = 'http://www.qmaile.com/'
r = requests.get(q_url)

# 定义匹配规则
reg = re.compile('<option value="(.*?)" selected="">')
q2_url = re.findall(reg, r.text)

s = input("请输入：")
t_url = "https://v.qq.com/x/search/?q=%s" % s
r = requests.get(t_url)
r.encoding = r.apparent_encoding
tree = etree.HTML(r.text)
result_url = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/@href')[0]
result_name = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/h2/a/em/text()')[0]
print(result_name, result_url)
# print(r.text)
response = requests.get(result_url)
tree_2 = etree.HTML(response.text)
url_list = tree_2.xpath('/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/span/div/div/div/span/a/@href')
# print(url_list)
# print(response.text)
# print(len(url_list))
print(s + "共{}集".format(len(url_list)-2))
n = input("选集： ")
tx_url = url_list[int(n) - 1]
webbrowser.open(q2_url[0] + tx_url)