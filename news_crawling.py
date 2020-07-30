# 从淘宝网站获取商品评论数据

# 导入模块
import requests
import re
import time
import pandas as pd

# 耳圈网址
# https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.4e143c6dzJBB7e&id=533016464039&skuId=3178935135714&areaId=230100&user_id=1712484042&cat_id=2&is_b=1&rn=a3c51963c6c7fe9f47f7bb626953cacd

# Requests Headers
headers = {
    # 从哪个页面发出的数据申请
    'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.4e143c6dzJBB7e&id=533016464039&skuId=3178935135714&areaId=230100&user_id=1712484042&cat_id=2&is_b=1&rn=a3c51963c6c7fe9f47f7bb626953cacd',
    # 用的哪个浏览器
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    # 哪个游客想要看数据
    'cookie': 'lid=cookie%E5%87%A1; enc=TaPAdTDNOIxBfRpvr7cVJPK4PmvSUoKPLXgvde7GtXYScbmtcTXE1lV1f6i60qLgI1zMmlxlq46CxVwTpIuYow%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; tfstk=ckdVB7coe1xSOXMod65NfvQrZXsAZ8dH6u71npmIoUnIytBci2ZOrZH5U9sKZtf..; OZ_1U_2061=vid=veea06d9e18a26.0&ctime=1592395499&ltime=1592395491; dnk=cookie%5Cu51E1; tracknick=cookie%5Cu51E1; lgc=cookie%5Cu51E1; cookie2=10d156b184b3812864793f5a465f7ecd; t=e5c55da930ee01cc806724ad1d01e449; cna=vkacFwTIdTgCASplQBxd3qaT; sm4=230102; _l_g_=Ug%3D%3D; unb=124942875; cookie1=VWp0TqBorD4YRUxIc6lrieI1DVIyUMBr3AALm52E7eI%3D; login=true; cookie17=UoM%2F32AGuhPK; _nk_=cookie%5Cu51E1; sg=%E5%87%A158; _tb_token_=3e8744363e7eb; uc1=cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&existShop=false&pas=0&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie14=UoTV6eqZ7Mah2g%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; uc3=id2=UoM%2F32AGuhPK&nk2=AHXKcP1P74k%3D&lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dBxGyicvN1Ut4pHNM%3D; uc4=nk4=0%40Ahsn0YxODOLpffnw6jq7iYpbrA%3D%3D&id4=0%40UOu7qW%2BGAXI9uOr0vFsCCsS1YZ4%3D; sgcookie=ExkK%2BaRdisCTq4MSeaa8P; csg=2d3bb025; x5sec=7b22726174656d616e616765723b32223a223565326538323434326133633838663335636566653863343339643038353632434d364e39766746455033697a2b7a506f72474232674561437a45794e446b304d6a67334e547378227d; _m_h5_tk=c995d52a15b66b9469c443ef3ee7140b_1595780077404; _m_h5_tk_enc=82ec62055a8921efcd204ad3057f1cf6; isg=BEJCNHv9qQCivbeqKOBJo5Kak06kE0YtQqjGGYxb27V53-BZdaLyP-RZj9ujj77F; l=eBMp5Esqq7Z8_DoFKO5Zourza77twIRbzsPzaNbMiInca1lFwLHdRNQqdTbkkdtjgtfXUeKyZPH3jRHM-5z_8E_ceTwhKXIpBxv9O'
}

# 获取更多页评论
texts = []
for n in range(1, 401):

    # 设定爬虫网址
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=533016464039&spuId=609856080&sellerId=1712484042&order=3&currentPage='+str(n)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvTQvpvB%2BvUpCkvvvvvjiPnL5wzjiRPsFyAjljPmPU6jnCPsMp1jlnP2LwQjtUPT6CvCh9mvvmkIIvTR6idAI3pQeHA46CvvyvCPmCHCpvsnvtvpvhvvvvvUhCvvsNq1%2BGKDsNzYYO5aQPvpvhvvvvvvhCvvOvCvvvphmivpvUvvmvKwKIzduEvpvVmvvC9c3bKphv8vvvvvCvpvvvvvmmZhCv2nvvvUEpphvWh9vv9DCvpvQovvmmZhCv2CUEvpCW2UikvvwTD7z9a40AVADlafmxdByaUneYiXhpVVQEfwBlYC978BLhQWswVCO0747B9Wma%2BoHoDO2UsC6tExjxAfev%2Bull8PLUYPoJ%2BFyCvvpvvvvviQhvCvvv9U8jvpvhvvpvv86Cvvyv2vwmw5UvabTCvpvWz%2FaIcml4zYMN%2BcjwRphvCvvvvvv%3D&needFold=0&_ksTS=1595771450701_2430&callback=jsonp2431'
    # 增加延时控制速度，避免反爬
    time.sleep(3)

    # 直接发起拿数据请求拿数据
    data = requests.get(url, headers=headers).text

    # 通过正则提取评论
    # 匹配规则："rateContent": "想要的评论内容","fromMall"
    rate = re.compile('"rateContent":"(.*?)","fromMall"')
    rate = rate.findall(data)

    texts.extend(rate)
    print('finish' + str(n) + 'page')

# 保存数据
df = pd.DataFrame()
df['comment'] = texts

print(df)

df.to_csv('comments.csv')
