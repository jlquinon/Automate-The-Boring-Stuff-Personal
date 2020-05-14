import pyinputplus as pyip

breadPrices = {
    "wheat" : 1.25,
    "white" : 1.50,
    "sourdough" : 2.00
    }

breadMenu = ['wheat', 'white', 'sourdough']
breadPrompt = 'What type of bread would you like?\n * {}\n * {}\n * {}\n'
breadResponse = pyip.inputMenu(breadMenu,
                               prompt=breadPrompt.format(breadMenu[0], breadMenu[1], breadMenu[2]),
                               numbered=True,
                               allowRegexes = ['^(wheat|white|sourdough)$'])


proteinPrices = {
    "chicken" : 1.50,
    "turkey"  : 1.50,
    "ham"     : 1.75,
    "tofu"    : 1.00
    }

proteinMenu = ['chicken', 'turkey', 'ham', 'tofu']
proteinPrompt = 'What type of protein would you like?\n * {}\n * {}\n * {}\n * {}\n'
proteinResponse = pyip.inputMenu(proteinMenu,
                                 prompt=proteinPrompt.format(proteinMenu[0], proteinMenu[1], proteinMenu[2], proteinMenu[3]),
                                 numbered=True,
                                 allowRegexes = ['^(chicken|turkey|ham|tofu)$'])


cheeseInquiryPrompt = 'Would you like cheese?\n'
wantCheese = pyip.inputYesNo(cheeseInquiryPrompt)
if wantCheese == 'yes':
    cheesePrices = {
        "cheddar"       : 1.00,
        "mozzarella"    : 1.50,
        "swiss"         : 1.75
        }
    cheeseMenu = ['cheddar', 'mozzarella', 'swiss']
    cheesePrompt = 'What type of cheese would you like?\n * {}\n * {}\n * {}\n'
    cheeseResponse = pyip.inputMenu(cheeseMenu,
                                    prompt=cheesePrompt.format(cheeseMenu[0], cheeseMenu[1], cheeseMenu[2]),
                                    allowRegexes = ['^(chicken|turkey|ham|tofu)$'])

countPrompt = 'How many sandwiches would you like?\n'
countResponse = pyip.inputNum(countPrompt, min=1)

pricePerSandwich = breadPrices[breadResponse] + proteinPrices[proteinResponse] + (cheesePrices[cheeseResponse] if wantCheese == 'yes' else 0)
total = pricePerSandwich * countResponse

print('The price per sandwich is %s' % pricePerSandwich)
print('Your total is %s' % total)
