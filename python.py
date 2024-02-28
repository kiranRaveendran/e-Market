
# def winning_pos(list_data):
#     total_bet=sum(list_data)
#     print(f'total bet amount {total_bet}',)
#     item=[]
#     for amount in list_data:
#         owner_profit=amount*9*10/100
#         item.append(owner_profit)
#     pos=item.index(max(item))
#     print(f'The winning postion is {pos}')

# val = [1000, 600, 500, 2000, 300, 200, 800, 1500, 100, 250]
# winning_pos(val)


# def find_combinations(data):
#     result = {}
#     for name,phone in data:
#         last_4_digit=phone[-4:]
#         if last_4_digit in result:
#             result[last_4_digit].append(name)
#         else:
#             result[last_4_digit]=[name]
#     return result


# contacts = [('Alice', '1234567890'), ('Bob', '98765432110'), ('Charlie', '5551237890'), ('David', '5551233456'),
#             ('Eve','9876543210')]
# print(find_combinations(contacts))


# from datetime import date
# import datetime as DT
# today = DT.date.today()
# week_ago = today - DT.timedelta(days=7)

# print(week_ago)
# # today =date.today-7()
# # print(today)

# today = DT.date.today()
# print(today)
# week_ago = today - DT.timedelta(days=7)

# print(week_ago)

# /////////////////////////////////////////list of seven days leading up to today

# import datetime as DT
# today = DT.date.today()
# print(today)
# date_list = [today - DT.timedelta(days=x) for x in range(7)]

# for date in date_list:
#     # print(date)
#     pass

# p = [3, 2, 1]
# n = [i for i in enumerate(p)]
# print(n)

class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedlist:
    def __init__(self, value):
        new_node = node(value)
        self.head = new_node
        self.tile = new_node
        self.length = 1


# l = linkedlist(1)
# print(l.tile.next)
l = [1, 2, 3, 4, 5, 6]
if 2 in l[2:]:
    print('hhhh')
