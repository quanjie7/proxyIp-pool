#!/usr/bin/env python
# coding=utf-8

import asyncio

import aiohttp

# from .config import HEADERS, REQUEST_TIMEOUT, REQUEST_DELAY


async def _get_page(url, sleep):
    """
    获取并返回网页内容
    """
    async with aiohttp.ClientSession() as session:
        try:
            HEADERS = {
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
            }
            # 请求超时时间（秒）
            REQUEST_TIMEOUT = 15
            # 请求延迟时间（秒）
            REQUEST_DELAY = 0
            await asyncio.sleep(sleep)
            async with session.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT) as resp:
                return await resp.text()
        except:
            return ""


def requests(url, sleep=0):
    """
    请求方法，用于获取网页内容

    :param url: 请求链接
    :param sleep: 延迟时间（秒）
    """
    loop = asyncio.get_event_loop()
    html = loop.run_until_complete(asyncio.gather(_get_page(url,sleep)))
    if html:
        return "".join(html)
