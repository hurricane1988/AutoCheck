#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def mytest():
    print("Hello ...")
    #await asyncio.sleep(1)
    print('... World')

asyncio.run(mytest())