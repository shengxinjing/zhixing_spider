#coding:utf-8

from pyquery import PyQuery as pq
import requests
import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
loginUrl = 'http://zhixing.bjtu.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
pageUrl = 'http://zhixing.bjtu.edu.cn/thread-979315-1-1.html'
postObj = {
	"username":'woniuppp',
	"password":'92d7ddd2a010c59511dc2905b7e14f64',
	"quickforward":'yes',
	"handlekey":'ls'
}
# user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
#               "AppleWebKit/537.36 (KHTML, like Gecko) "
#               "Chrome/36.0.1985.143 Safari/537.36")

# post_headers = {"User-Agent": user_agent,
#                 "Referer": "http://zhixing.bjtu.edu.cn/portal.php"
#                 }
# 知行没有验证header UA 和rederer 我想多了

s = requests.Session()  # 可以在多次访问中保留cookie
s.post(loginUrl, postObj)  # POST帐号和密码，设置headers
# s.post(loginUrl, postObj, headers=post_headers)  # POST帐号和密码，设置headers
r = s.get(pageUrl)  # 已经是登录状态了

test = pq(r.text).find('.t_fsz td.t_f')
print test.html()
