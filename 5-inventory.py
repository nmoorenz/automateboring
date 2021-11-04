# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:27:45 2019

@author: MooreN
"""

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        # assume we always get a dictionary item
        item_total += v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)


def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems: 
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)