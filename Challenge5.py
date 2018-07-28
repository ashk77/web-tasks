import json

with open('chall5.json', encoding='utf-8') as root:
    root = json.loads(root.read())
workWith = root['body']['Recommendations']


def printName(childrene, arrow):
    print("-"*arrow, ">", childrene['name'])
    if childrene['selected'] == 1:
        for childs in childrene['children']:
            printName(childs, arrow+2)


for restaurants in workWith:
    print(restaurants['RestaurantName'])
    menus = restaurants['menu']
    for menu in menus:
        if menu['type'] == 'sectionheader':
            for children in menu['children']:
                if children['type'] == 'item':
                    printName(children, 2)






