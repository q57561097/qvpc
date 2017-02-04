#coding:utf-8
from scrapy.spider import Spider
from scrapy.http import Request,FormRequest
import urllib
class QvSpider(Spider):
    name = 'qvna'
    start_urls=['http://user.qunar.com/message/list']
    #cook={"QN1":"eIQiPliPB70oCYpTd1t8Ag==",}

    headers = {
       "Host":"user.qunar.com",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept":"*/*",
        "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding":"gzip, deflate",
        #"Referer":"http://order.qunar.com/",
        "Connection":"keep-alive",
        "Referer": "https://www.qunar.com/"
        #"Cache-Control":"max-age=0",
        #"Cookie":"QN99=6034; QN1=eIQiPliPB70oCYpTd1t8Ag==; csrfToken=gDgYXwguGupdAiwWEfrgGtBJhfaNEdsg; QunarGlobal=192.168.31.100_-1048beaf_159eeb146a7_-6e27|1485768639979; _i=RBTjeLzySXRVuFyRsaAS-S0jdAUx; QN269=C4B7CC50E6CE11E6994FFA163EBE0F8B; Hm_lvt_75154a8409c0f82ecd97d538ff0ab3f3=1485767830; QN48=tc_82cd2e89e5d52b0a_159eeb6532f_e478; QN25=5893ef66-f2c6-4d09-ba74-56ee1f574002-9f992f90; _vi=EcSxtJPFT8h2KdOK8XDO5OO5B5tbrNf-ypyexHQvx4jHYU8va3LSlsqWXRak4lkH8TQi408vSregFxDP4lidTto22nq0uxnwQnePXJWsqe7awIEk1myoJU-hfKJzr9s--2qZjCOU4znZ2AEUabFLmY3bvETV76jb2587neF7B1t3; QN271=a7331ab9-3bc5-417c-8508-acc7b22149be; QN43=2; QN42=txgh4095; _q=U.tozcxxt2928; _t=24873312; _s=s_L5HEYMLU7LK6NOJNOXBHXCHGJU; _v=8zCcRkbfkWz4QNwkSeL0Z1RyOrsejKLzovYsn9bSlI9_bqdlI6EMjLlOgXD9UyTlEL8kC9iow7dwzEIL6_ECp9AKcGxr6qdmfboZOwsrZimyOBsPQJPHWgWpdqgZQ4GIaZiJyHTyKx7EmWQsrPd8r-88fnZaUJKXQzKOTi7At9t3; JSESSIONID=839A9D31B1C27A8C1F4542BD53A3C937; QN44=tozcxxt2928; PHPSESSID=palcf8pob5a2od0c658vkrekm1; QN268=|1485832403329_31eb0c007a6bd698"

    }

    def start_requests(self):
        return [Request('https://user.qunar.com/passport/login.jsp',meta={'cookiejar': 1},headers=self.headers,callback=self.post_login)]
    def post_login(self,response):
        catca=response.xpath('//img[@id="vcodeImgMobile"]/@src').extract()
        filename="/home/zyh/catca.png"
        urllib.urlretrieve(catca[0],filename=filename)
        catca_value=raw_input()
        data={"username":"13052586986",
              "password":"57561097l",
              "vcode":catca_value,
              "remember":"1",
              }
        print catca_value
        yield FormRequest.from_response(response,
                                          # "http://www.zhihu.com/login",
                                          #meta={'cookiejar': 1},
                                          headers=self.headers,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          #cookies=self.cook,
                                          formdata=data,

                                          callback=self.after_login,

                                         )
        #req.meta['cookiejar']=response.mate['cookiejar']
        #yield req
    def after_login(self, response):


        for url in self.start_urls:
          yield   Request(url,headers=self.headers,meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse)
            #r.meta.update(cookiejar=response.meta['cookiejar'])

    def parse (self, response):
            with open('/home/zyh/body.txt','a') as f:
                f.write(response.body)
