# Khởi tạo các giá trị
a = 10
b = 5

# Nhận tên biến từ người dùng
variable_name = input("Nhap ten bien: ")

# Kiểm tra xem biến có tồn tại hay không
if variable_name in locals():
    # Nhận phép tính từ người dùng
    operation = input("Nhap phep tinh (+, -, *, /): ")

    # Nhận giá trị thứ hai từ người dùng
    value = float(input("Nhap gia tri thu hai: "))

    # Thực hiện phép tính và in ra kết quả
    if operation == "+":
        result = locals()[variable_name] + value
        print(result)
    elif operation == "-":
        result = locals()[variable_name] - value
        print(result)
    elif operation == "*":
        result = locals()[variable_name] * value
        print(result)
    elif operation == "/":
        result = locals()[variable_name] / value
        print(result)
else:
    print("Tên biến không tồn tại")
