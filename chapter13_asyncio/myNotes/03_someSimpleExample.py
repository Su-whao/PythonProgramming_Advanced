import time
import urllib.request
import asyncio
import aiohttp

URL = "https://api.github.com/events"
MAX_CLIENTS = 3

async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as reponse:
            return reponse

async def fetch_async(pid):
    print("Fetch async process {} started".format(pid))
    start = time.time()
    response = await aiohttp_get(URL)
    datetime = response.headers.get("Date")

    print("Process {}: {}, took: {:.2f} seconds".format(
        pid, datetime, time.time()-start
    ))

    response.close()
    return datetime

async def main1():
    '''
        Example 1:等待所有任务完成后进行处理
    '''
    start = time.time()
    tasks = [asyncio.create_task(fetch_async(i)) for i in range(1,MAX_CLIENTS+1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time()-start))

async def main2():
    '''
        Example 2:当前任务完成后立即处理当前任务的结果
    '''
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print('{} {}'.format(">>" * (i + 1), result))

    print("Process took: {:.2f} seconds".format(time.time() - start))

# asyncio.run(main2())


'''
    Example 3:
    Let’s get to another example, imagine you’re trying to get your IP address. 
    There are similar services you can use to retrieve it but you’re not sure 
    if they will be accessible at runtime. You don’t want to check each one 
    sequentially, ew. You would send concurrent requests to each service and pick 
    the first one that responds, right? Right!

    要获取IP地址，有多个服务器可以满足功能，但是不确定每个都能用，又不想每个都去测试一下，
    因此可以给每个服务器都发一个请求，然后使用第一个返回的结果，可以使用 wait() 方法，
    wait 方法有一个参数 return_when 可以满足条件。
'''

from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple("service", ("name", "url", "ip_addr"))
SERVICES = (
    Service("ipify", "https://api.ipify.org?format=json", "ip"),
    Service("ip-api", "http://ip-api2.com/json", "query")
)

async def aiohttp_get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_ip(service):
    start = time.time()
    print("Fetching IP from {}".format(service.name))

    json_response = await aiohttp_get_json(service.url)
    ip = json_response[service.ip_addr]

    return "{} finished with result: {}, took: {:.2f} seconds".format(
        service.name, ip, time.time()-start
    )


async def main():
    start = time.time()
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(futures, return_when=FIRST_COMPLETED)
    # 需要将未完成的任务取消
    [pend.cancel() for pend in pending]
    print(done.pop().result())
    print(f"Total time: {time.time()-start}")

# 这种方式不用取消pending的任务也不会报错
# asyncio.run(main())

# 使用这种方式要取消pending的任务，否则会报错
# ioloop = asyncio.get_event_loop()
# ioloop.run_until_complete(main())
# ioloop.close()


## timeout

import time
import random
import asyncio
import aiohttp
import argparse
from collections import namedtuple
from concurrent.futures import FIRST_COMPLETED

Service = namedtuple("Service",  ("name", "url", "ip_addr"))

SERVICES = (
    Service("ipify", "https://api.ipify.org?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query")
)

DEFAULT_TIMEOUT = 0.01

async def aiohttp_get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_ip(service):
    start = time.time()
    print("Fetching IP from {}".format(service.name))

    await asyncio.sleep(random.randint(1,3) * 0.1)
    try:
        json_response = await aiohttp_get_json(service.url)
    except:
        return "{} is unresponsive".format(service.name)


    ip = json_response[service.ip_addr]

    print("{} finished with result: {}, took: {:.2f} seconds".format(
        service.name, ip, time.time()-start
    ))

    return ip

async def main(timeout):
    response = {
        "message": "Result from asynchronous",
        "ip": "not available"
    }

    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, timeout=timeout, return_when=FIRST_COMPLETED
    )

    # for future in pending:
    #     future.cancel()
    
    for future in done:
        response["ip"] = future.result()

    print(response)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--timeout",
    help="Timeout to use, defaults to {}".format(DEFAULT_TIMEOUT),
    default=DEFAULT_TIMEOUT, type=float
)

args = parser.parse_args()

print("Using a {} timeout".format(args.timeout))
asyncio.run(main(args.timeout))
