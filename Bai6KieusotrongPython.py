#gán cho biến a giá trị là 4. Với 4 là kiểu số nguyên (Intergers)
a = 1.12345678910112131415

#print(a) 

# kiểu dữ liệu của a: type lấy kiểu dữ liệu của giá trị hoặc của 1 biến nào đó,
#trong python kiểu dữ liệu số nguyên là vô hạn
# số thực là tập hợp số nguyên và stp 1 2.4 ...
# số thực trong python có giá trị chính xác xấp xỉ 15 số phần tp( số sau dấu .)


print(type(a)) 

#lấy toàn bộ nội dung của thư viện decimal
# từ thư viên decimal -> import mọi thứ (*) vào
from decimal import*
#lấy tối đa 30 chữ số phần nguyên và phần tp decimal
getcontext().prec =30
f=10/3
#print(Decimal(10)/Decimal(3))
print(f)
print(type(f))
# chỉ cần 1 giá trị là Decimal thì nó sẽ hiểu cả biểu thức là Decimal 
d=Decimal(10)/Decimal(3)
print(d)
print(type(d))
