# 元组  ()  不能改变
url_tuple=('http://www.hnxmxit.com','80')
print(url_tuple[0])

#试图修改,我们希望改成  http//www.xmx.com
url_tuple[0]='http//www.xmx.com'
print(url_tuple)
