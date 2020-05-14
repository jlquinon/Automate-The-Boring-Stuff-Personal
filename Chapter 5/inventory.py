# inventory.py

def displayInventory(inventory):
    print('Inventory')

    totalAmount = 0

    for item, amount in inventory.items():
        print('%s %s' % (amount, item))

        totalAmount += amount

    print('Total number of items: %s' % (totalAmount))

    
inventory = {
    'rope' : 1,
    'torch' : 6,
    'gold coin' : 42,
    'dagger' : 1,
    'arrow' : 12 
}

displayInventory(inventory)