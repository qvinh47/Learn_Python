"""
1. List trong list
2. Copy list
3. List Slicing
"""

# Sử dụng thư viện pprint để pprint ra list quá dài sẽ tự xuống hàng
from pprint import pprint
list = ["aaaaaaaaaaaaaaaaaaaa",
        "bbbbbbbbbbbbbbbbbbbbb",
        "ccccccccccccccccccccc",
        "ddddddddddddddddddddđ"]
pprint(list)

# 1. List in list
#           0              1           2
friends = [["Dang", 17], ["Quang", 18], ["Vinh"], 19]
print(type(friends))
# In ra phần tử 0 của vị trí 0
print(friends[0][0])
print(friends[1][1])

# 2. Copy List
lst1 = [1, 3, 5]
# lst2 = lst1       #1
# Toán tử is: kiểm tra cái id (vị trí bộ nhớ của cái list đó) xem id có bằng nhau không
# Copy
lst2 = lst1.copy()  # s
print(lst1 is lst2)  # 1 True #2 False(vì đã copy nên không phải bản gốc ~~)
print(lst1 == lst2)

#    3. List slicing : lấy ra 1 phần từ cái list ban đầu
#    0  1   2    3    4
#   -5 -4  -3   -2   -1
a = [1, 3, 101, 111, 23]
new_lst = a[0:2:1]  # Lấy khoảng [0:2) bước nhảy là 1
new_lst = a[:2]    # hoặc viết như thế này
print(new_lst is a)
new_lst = a[1:]  # lấy từ 1 đến hết
new_lst = a[1:-1]
new_lst = a[-1:-4]  # Sao chép ra toàn bộ phần  tử của list
print(new_lst)
# Muốn lật lại list thì [::-1]
new_lst = a[::-1]
print(new_lst)
# Rev thì nó sẽ thực thi trên cái list cũ, còn ::-1 thì sẽ in ra list mới
print(a[1:-1])
print(a[0:])
