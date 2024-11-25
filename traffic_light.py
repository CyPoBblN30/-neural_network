from threading import Thread
import asyncio
from time import sleep



#  синхронный
def traffic_light(all_colors):
    for color in all_colors:
        yield color


colors = ['Red', 'Yellow', 'Green']
b = traffic_light(colors)


print(next(b))
print(next(b))
print(next(b))



# асинхронный


async def traffic_light1():
    print('Red')


async def traffic_light2():
    sleep(10)
    print('Yellow')


async def traffic_light3():
    sleep(3)
    print('Green')


async def main():
    t1 = asyncio.create_task(traffic_light1())
    t2 = asyncio.create_task(traffic_light2())
    t3 = asyncio.create_task(traffic_light3())
    await t1, t2, t3


asyncio.run(main())



#  многопоточный


def traffic_light4():
    print('Red')


def traffic_light5():
    print('Yellow')


def traffic_light6():
    print('Green')


t4 = Thread(target=traffic_light4())
t5 = Thread(target=traffic_light5())
t6 = Thread(target=traffic_light6())


t4.start()
t5.start()
t6.start()



