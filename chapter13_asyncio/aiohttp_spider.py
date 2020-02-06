# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-13 10:20:33
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-14 12:02:17
 * @Description: None
'''
# ASYNCIO 爬虫，去重，入库

import asyncio
import re


import aiohttp
import aiomysql
from pyquery import PyQuery


start_url = "https://www.baidu.com/"
waitting_urls = []  # 待解析URL 
seen_urls = set()   # 已完成URL
stopping = False

# downloader
async def fetch(start_url, session):
    print("fetch")
    try:
        async with session.get(start_url) as resp:
            if resp.status in [200, 201]:
                print(resp.status)
                data = await resp.text()
                return data
    except Exception as e:
        print(e)

# 解析HTML中的url
def extract_urls(html):
    print("extract_html", html)
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    print(waitting_urls)
    return urls

async def article_handler(url, session, pool):
    print("article_handler")
    # 获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()

    async with pool.acquire() as conn:
         async with conn.execute() as cur:
             await cur.execute("SELECT 42;")
             insert_sql = "insert into article_test(title) value('{}')".format(title)
             await cur.execute(insert_sql)



async def consumer(pool):
    print("consumer")
    print(waitting_urls)
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            
            url = waitting_urls.pop()
            print("start get url: {}".format(url))

            if re.match(r"https://\w+.baidu.com", url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
                    await asyncio.sleep(30)
                # else:
                #     if url not in seen_urls:
                #         asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    #等待Mysql连接建立好
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
                                        user="root", password="password",
                                        db="aiomysql_test", loop=loop, 
                                        charset="utf8", autocommit=True)
 
    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)

    asyncio.ensure_future(consumer(pool))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()