"""
1. Tuple: là 1 bộ giá trị, cấu trúc dữ liệu có thứ tự,
có thể chứa các phần tử, giá trị trùng lặp
bên trong Tuple và được tạo bởi cặp dấu ngoặc tròn ()
Tuple cũng tương tự với list nhưng có 1 điểm khác biệt đó là
Nó không thể thay đổi bản thân nó và các giá trị trong bản thân nó

2. Set: được tạo bởi dấu ngoặc nhọn {} và trong set không thể 
chứa các giá trị trùng lặp. Set không có thứ tự
"""

Tuple : #Hay dùng với database
tup1 =1, 2, 3
print(type(tup1))
tup2 = (1, 2, 3)
print(type(tup2))
tup3 = 1,
print(type(tup3))
tup4 = (4,)
print(tup1[1])
print(type(tup4))
tup1[0]=1000 #  Tuple không thể thay đổi giá trị bên trong nó 
tup1.append(2200) # Bản thân nó không thể thay đổi 
#Thêm 1 giá trị vào tup1
tup1 += (4,5,6,1,23,3,5,23,4)
print(tup1)

Set: #là cấu trúc dữ liệu dùng để lưu trữ nhiều giá trị 
#trong 1 cái biến duy nhất. Và set không thể chứa các giá trị trùng lặp
Set #không có thứ tự 

set1= set()
set1.add("Anh")
set1.add("Anh")
set1.add("Anh")
# Không thể có những phần tử trùng lặp
print(set1)
set1.update([1,2,3,4,5])
set1.remove(2)
set2=set1.copy()

print(set1 is set2 )
print(set1 == set2 )
set1.clear()
print(set1)
set1 ={1,2,3,4}
print(type(set1))
set1.add([1,2,3,4]) # Error : vì những giá trị có thể thay đổi
#   trực tiếp bằng cách phương thức trên nó như append,reversed...
set1.add("vinh") # Giá trị không thể thay đổi là chuỗi
print(type(set1))
print(set1)
print(set1[-1]) # Không thể truy cập các giá trị bằng chỉ số 
set1 = set({1,2,3,4,5,6,7,8,9,-10})
value = set1.pop()
print(value)
print(set1)