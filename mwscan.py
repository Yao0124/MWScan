# Copyright (c) 2026 Yao0124
# SPDX-License-Identifier: MIT
import requests
from fake_useragent import UserAgent
import pyfiglet
import argparse

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'
logo = pyfiglet.figlet_format("MWSCAN", font="slant")
print(f"{RED}{logo}{RESET}")
print('by Yao0124')

ua = UserAgent()
parser = argparse.ArgumentParser(
    description='中间件查找工具'
)
parser.add_argument('-u','--url',help='目标url')

def main():
    args = parser.parse_args()
    url = args.url
    if url is not  None and not url.startswith("http"):
        url = 'http://' + args.url
    headers = {'User-Agent': ua.random}
    if args.url is None:
        parser.print_help()
        exit(0)
    response = request(url, headers)
    server(response)

def request(url,headers):
    try:
        response = requests.get(url, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        print(f'连接错误:{url}')
        return None

def server(response):
    try:
        server_version = response.headers.get("server")
        print('中间件：', server_version)
    except KeyError:
        print('网站隐藏了该信息')
    except Exception as e:
        print(f'其他错误:{e}')

if __name__ == '__main__':
    main()
