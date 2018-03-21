import requests
import sys
import asyncio

async def send_request(num):
    r = requests.get('https://requestb.in/1angnzb1')
    if r.status_code == 200:
        print('ok request' + str(num))


def http_sync_call(num):
    for x in range(1, num + 1):
        r = requests.get('https://requestb.in/1angnzb1')
        if r.status_code == 200:
            print('ok request' + str(x))


def http_async_call(number):
    loop = asyncio.get_event_loop()
    # generate method list
    task = asyncio.gather(*[send_request(num) for num in range(1, number + 1)])
    loop.run_until_complete(task)
    loop.close()


if sys.argv[1] == 'async':
    print('Asynchronous:')
    http_async_call(int(sys.argv[2]))

if sys.argv[1] == 'sync':
    print('Synchronous:')
    http_sync_call(int(sys.argv[2]))
'''
print('Asynchronous:')
http_async_call(3)

print('Synchronous:')
http_sync_call(3)
'''

'''
    Output:
    ton9ericdeMacBook-Air:CMPE273 ton9eric$ python3 273Lab2.py sync 3
    Synchronous:
    ok request1
    ok request2
    ok request3
    ton9ericdeMacBook-Air:CMPE273 ton9eric$ python3 273Lab2.py async 3
    Asynchronous:
    ok request1
    ok request3
    ok request2
'''



