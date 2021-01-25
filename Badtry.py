# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

for i in range(1):
    url = f'https://www.yelp.com/search?find_desc=Vegan%20Cafe&find_loc=San%20Francisco%2C%20CA&ns=1&start={i}0'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    for item in soup.select('[class*=container]'):
        try:

            # print(item)
            if item.find('h4'):
                name = item.find('h4').get_text()

                for j in range(51):
                    name = name.strip(f'{j+1}.')
                    name = name.lstrip()
                print(name)
                name = name.replace("&", "and")
                print(name.lower())

                cafe_url = name.lower().replace(" ", "-")
                cafe_url = cafe_url.replace(',-', '-')
                print(cafe_url)
                detail_cafe_urls = f'https://www.yelp.com/biz/{cafe_url}-san-francisco?osq=Vegan+Cafe'
                print(detail_cafe_urls)
                # for action in
                detail_response = requests.get(detail_cafe_urls)
                #
                # print(detail_response.json()["linkText"])
                detail_soup = BeautifulSoup(detail_response.content, 'lxml')

                # content_response = detail_response.content
                print(detail_soup.find('a', {'class_': 'link'}))
                # website = detail_soup.find('a', {'class_': 'link'})
                # # print(detail_soup.select("//span[contains(@class,'biz-website')]/a/@href"))
                # print(website)
                # print(soup.select('[aria-label*=rating]')[0]['aria-label'])
                # print(soup.select('[class*=secondaryAttributes]')[0].get_text())
                # print(soup.select('[class*=priceRange]')[0].get_text())
                # print(soup.select('[class*=priceCategory]')[0].get_text())

                print('------------------')
        except Exception as e:
            raise e
            print('Error')




#
# <a class=" link__373c0__1G70M link-color--blue-dark__373c0__85-Nu link-size--inherit__373c0__1VFlE" href="/biz_redir?url=http%3A%2F%2Fwww.belovedsf.com&amp;website_link_type=website&amp;src_bizid=U2lbKxfjKbqGPsvsYPAyLA&amp;cachebuster=1611507159&amp;s=76a8743743f383cd820c0f93d5f5dc49e4ef12d843919d2588b63a234dbfcfb8" target="_blank" name="" rel="noopener nofollow" role="link">belovedsf.com</a>
#
#

