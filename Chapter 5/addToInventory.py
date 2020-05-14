# addToInventory.py
from inventory import displayInventory

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

if __name__ == '__main__':
    inventory = {
        'rope' : 1,
        'torch' : 6,
        'gold coin' : 42,
        'dagger' : 1,
        'arrow' : 12 
    }

    dragonLoot = [
        'gold coin',
        'dagger',
        'gold coin',
        'gold coin',
        'ruby'
    ]
    print('Before adding items')
    displayInventory(inventory)

    print()

    addToInventory(inventory, dragonLoot)

    print('After adding items')
    displayInventory(inventory) 