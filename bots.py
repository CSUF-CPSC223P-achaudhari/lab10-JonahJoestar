# Claire Swiatek
# CPSC 223P Lab 10
# 11/15/2023

import threading
from time import sleep
import json

def bot_fetcher(items, cart, lock):
    new_dict = {}
    with open('inventory.dat', 'r') as f: # You open the inventory renamining it as f
        new_dict = json.load(f)
    for key in items:
        value = new_dict[key]
        duration = value[1]
        item = value[0]
        sleep(duration)
        lock.acquire()
        cart.append([key, item])
        lock.release()


def bot_clerk(items):
    bot0 = []
    bot1 = []
    bot2 = []
    cart = []
    lock = threading.Lock()
    for n, key in enumerate(items):
        bot_num = n % 3
        if bot_num == 0:
            bot0.append(key)
        elif bot_num == 1:
            bot1.append(key)
        elif bot_num == 2:
            bot2.append(key)
    
    # print(bot0)
    # print(bot1)
    # print(bot2)

    threads = []
    if len(bot0) > 0:
        t = threading.Thread(target=bot_fetcher, args=(bot0, cart, lock))
        t.start()
        threads.append(t)

    # Same for bot 1 and 2
    if len(bot1) > 0:
        t = threading.Thread(target= bot_fetcher, args= (bot1, cart, lock))
        t.start()
        threads.append(t)

    if len(bot2) > 0:
        t = threading.Thread(target= bot_fetcher, args= (bot2, cart, lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        
    return cart
    
        
# Above is the bot clerk function


# Prior Attempt
# cart_list = 0
# thread_lock = threading.Lock()

# #Temp list?
# y = []

# def shared_var():
#     for _ in range(10000):
#         with lock:
#             shared_var += 1

# print(f'item {x} goes to robot fetcher list{y}')