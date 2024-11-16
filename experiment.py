import asyncio
import time
import threading
import random

group_size = 10
# task_list = [3, 4, 2, 3,1, 5, 6,3, 5,2,1,3,4,2,6]
task_list = []
for i in range(1000):
    task_list.append(random.randint(1,10))

total_time = 0
for t in task_list:
    total_time += t
print(f"total time:{total_time}")

async def task(n):
    await asyncio.sleep(n)

async def thread_task(new_task_list, name):
    tasks = []
    for task_time in new_task_list:
        tasks.append(task(task_time))
    await asyncio.gather(*tasks)
    print(f"thread {name} complete!")

def run_async_tasks(new_task_list, name):
    asyncio.run(thread_task(new_task_list, name))

start_time = time.time()

group_num = len(task_list) // group_size

print(group_num)

threads = []
for i in range(group_num):
    thread = threading.Thread(target=run_async_tasks, args=(task_list[i*group_size:(i+1)*group_size], i))
    threads.append(thread)
    thread.start()



for thread in threads:
    thread.join()

print("All threads have finished")
end_time = time.time()
print(f"execution time:{end_time- start_time}")


start_time = time.time()
async def only_async():
    tasks = [task(task_time) for task_time in task_list]
    await asyncio.gather(*tasks)
asyncio.run(only_async())
end_time = time.time()
print(f"execution time:{end_time- start_time}")
