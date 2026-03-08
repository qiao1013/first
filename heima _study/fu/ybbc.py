#111111协程函数
#一个线程在遇到IO等待的时间的时候，不会傻傻的去等待，而是利用空闲时间去完成其它任务


"""import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


#3.5版本写法
 tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

#3.7
async def main():
    await asyncio.gather(func1(),func2())

asyncio.run(main()) """

#2222222事件响应 理解为死循环

#有一个任务列表，把可执行的或者可完成的任务去执行或完成


#33333333快速上手

#搭配事件响应，任务列表变成asyncio的协程函数
#事件响应进行死循环

# asyncio def 函数名   由函数名创建了一个对象，它并不会执行。

#导包
""" import asyncio """
#协程函数完成异步编程
""" async def func1():
    print("快来吃我吧") """
#创建协程对象
""" result = func1() """

#进行事件响应也就是死循环  python3.7以后的版本都是用下面的写法

""" asyncio.run(result) """

#定义协程函数一定要和事件循环搭配起来



#4444444await关键字

""" import asyncio

async def func():
    print('快来玩呀1')
    await asyncio.sleep(2)
    print('end1')

async def func2():
    print('快来玩呀2')
    await asyncio.sleep(2)
    print('end2')

async def func3():
    print('快来玩呀3')
    await asyncio.sleep(2)
    print('end3')

async def main():
    await asyncio.gather(func(),func2())
    print('end4')
    # asyncio.run(func3())  #asyncio不能在已经执行的循环事件中重复调用
    await func3()



asyncio.run(main())
 """
#   await意义就是等 等协程对象执行完全结束以后，才继续执行这个协程函数下面的。  但是等待的时间可以执行其他函数里的任务


#555555555555555555 Task关键字

#Task对象是，立即把对象放在事件循环里面

""" import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
async def func2():
    print(3)
    
async def main():
    print("开始啦")
    task_list = [

        #创建task对象，将 当前执行func函数立即添加到事件循环里面
        asyncio.create_task(func(),name = 'n1'),
        asyncio.create_task(func2(),name='n2')

    ]
    #此时print(2)没有被执行，main()函数就已经关闭了
    #如果要让print(2)执行加
    # await 后面只能加协程对象和await对象
    # 所以await asyncio.wait(task_list)会返回两个值
    done,pending = await asyncio.wait(task_list,timeout=1)

    #done 是已经完成的集合，pending是还未完成的集合
    print(done)
    print(pending)

asyncio.run(main()) """  #因为asyncio .run (协程对象) = 
                                                #   loop = asyncio.get_event_loop()
                                                # loop.run_until_complete(asyncio.wait(tasks))
#事件循环已经创建了

#task对象帮助咱们立即把某个任务放到事件循环里面

# task[任务1，任务2，任务3......]


#66666666future对象
# 更偏向底层，一般不会直接用
# 它是task类的基类，task继承了future
