"""
1. List trong list
2. Copy list
3. List Slicing
"""

# # Sử dụng thư viện pprint để pprint ra list quá dài sẽ tự xuống hàng
# from pprint import pprint
# list = ["aaaaaaaaaaaaaaaaaaaa",
#         "bbbbbbbbbbbbbbbbbbbbb",
#         "ccccccccccccccccccccc",
#         "ddddddddddddddddddddđ"]
# pprint(list)

#       #1. List in list
#             0              1           2
# friends = [["Dang",17],["Quang",18],["Vinh"],19]
# print(type(friends))a
# # In ra phần tử 0 của vị trí 0
# print(friends[0][0])
# print(friends[1][1])

#       #2. Copy List
# lst1= [1,3,5]
# # lst2 = lst1       #1
# # Toán tử is: kiểm tra cái id (vị trí bộ nhớ của cái list đó) xem id có bằng nhau không
# #Copy
# lst2 = lst1.copy()  #s
# print(lst1 is lst2)     #1 True #2 False(vì đã copy nên không phải bản gốc ~~)
# print(lst1 == lst2)
print("toi bi dien")
# Khi nao moi het ngao