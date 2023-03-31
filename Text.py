# '''
# phrase = "DH SPKT TP HCM"
# print(phrase.lower().islower())
# print(len(phrase))
# print(phrase[4])
# print(phrase.index("TP"))
# print(phrase.replace("TP","QV"))
# print(-2.43353/2314)
# print(0%3)
# chuoi_so = 5
# print(str(chuoi_so)+ " quang vinh")
# tri_tuyet_doi = -5
# print(abs(tri_tuyet_doi))
# print(pow(5,2)) # phep toan luy thua
# print  (max(4,6))
# print(round(3.6))
# from math import *
# print(sqrt(16))
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + " ! You are " + age )

# Building a Basic Calculator

# num2 = input("Enter another number: ")
# result = num1 + num2
# Nếu chỉ cộng như này thì sẽ hiểu là 2 chuỗi và kết quả sẽ là 1 chuỗi
# result = int(num1)+ int(num2) # kiểu số nguyên
# print(result)

# Mad Libs Game :  nhập các từ ngẫu nhiên

# truong = input("Cai truong ma ban dang hoc : ")
# nganh =  input("Cai nganh ma ban dang hoc : ")
# su_yeu_thich = input("Ban co yeu thich no ?  : ")

# print("Ngoi truong than yeu toi dang hoc la " + truong)
# print("Cai nganh quai quy toi dang theo hoc la " + nganh)
# print("Toi " + su_yeu_thich + " yeu nganh nay" )

# ############### Chuyen nhieu dong thanh commet Ctrl +/  ######################

# List
# friends = ["Peter","Kevin", "Crba","Tom", "Com"]
# print(friends[-3])
# print(friends[1:3])
# friends[1] = "Vinh"
# print(friends[1])

# List Functions
# number = [0,1,4,8,1,6,7,3,9]
# name = ["Aen1","Ben2","Cen3","Den4","Een5","Aen1","Aen1","Aen1"]
# name.extend(number) # Kiểu gộp chuỗi
# name.append("Vinh") # Nối chuỗi
# name.insert(1,"Huy") #Chèn vào vị trí
# name.remove("Ten5") # xóa
# name.clear() #clear all
# name.pop() #xóa phần tử cuối cùng của chuỗi
# print(name)
# print(name.index("Ten2")) # Vị trí của phần tử
# print(name.count("Ten1")) # số lần xuất hiện của pt trong chuỗi
# name.sort() # sắp xếp theo abc... giá trị 1,2,3.. tăng dần
# print(name)
# number.reverse() # đảo thứ tự
# print(number)
# name2=name.copy() # copy
# print(name2)

# Tuples : 1 loại của cấu trúc dữ liệu ( về cơ bản là 1 nơi có thể lưu trữ cấu trúc dữ liệu) . Tuples  Bất biến không thể thay đổi đc
# toado =(4,5)
# print(toado[0])

# Function
# def sayhi():
#     print("Hello User")
# print("thutu1")
# sayhi()
# print("thutu2")
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age) )
# say_hi("Huy", 23)
# say_hi("Vinh", 24)

# Return Statement:  Lenh return
# def cube(num):
#     return num*num*num
# ketqua = cube(5)
# print(ketqua)

# If Statements

# is_male = False
# is_male = True
# if is_male:
#     print("You are a male")
# else:
#     print("You are not a male")

# is_male = False
# is_tall = True
# #if is_male or is_tall:
# if is_male and is_tall:
#     print("You are a male or tall or both")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You either male nor tall or both")

# If Statements & Comparisons : lenh if va toán tử so sánh
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(399979,400,5))

# Buiding a Better Calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1/num2)
# else:
#     print("Invalid operator")

# # Dictionaries
# monthConversions ={
#     "Jan":"January",
#     "Feb":"February",
#     "Mar":"March",
#     "Apr":"April",
#     "May":"May",
#     "Jun":"June",
#     "Jul":"July",
#     "Aug":"August",
#     "Sep":"September",
#     "Oct":"October",
#     "Nov":"November",
#     "Dec":"December",
#      "1" : "thang111"
# }
# #print(monthConversions["Dec"])
# print(monthConversions.get("May","Not a valid Key"))
# print(monthConversions["1"])

# While loop
# i = 1
# while i <=10:
#     print(i)
#     i +=1
# print("Done with loop")

# Building a Guessing Game
# secret_word = "Key Word"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False # Kieu bien tam xem da du 3 lan hay chua

# while guess!= secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print(" Out of Guesses, You Lose! ")
# else:
#     print("You win! ")

# For Loop
# friends = ["Dang", "Quang", "Vinh"]
# for name in friends:
#     print(name)
# for index in range(1,100):
#     print(index)
# for index in range (6):
#     if index ==0:
#         print(" Lan dau tien")
#     else:
#         print("Deo phai")

# Exponent Funciton : hàm số mũ
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(5,4))
#  tạo hàm. cho biến result =1 chạy vl for theo biến lũy thừa. gán hàm result bằng result nhân với cơ số.
# Sau đó return trở lại để bắt đầu theo biến result bằng 1 mới. In kết quả của hàm với cơ số và số mũ

# 2D Lists & Nested Loops : ds 2 chieu & vong lap long
# number_grid =[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]
# # print(number_grid[2][1]) # hang 2 cot 1 : so 10
# for row in number_grid:
#     for col in row:
#         print(col)

# Build a Translator : xay dung chuong trinh dich
# def translate(phrase):
#     translation = " "
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else :
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))


#  #Cach commmet khac
# '''
# day
# la
# commmet
# kieu
# thu
# 2
# '''
#  print(" day la comment")

# Try/Except
# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# # except:
# #     print("Loi roi thang ngu ")
#     # Những vấn đề không thể xử lí được sẽ in qua except và print ( kiểu chấp nhận 1 lỗi cụ thể )
#     # Lỗi cụ thể
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

# Reading files

#   r: doc file w: ghi, thay doi thong tin file a: cơ bản là cây bút: nối thêm thông tin ở cuối tệp  r+ :đọc và viết
# doc_file = open("docfile.txt","r")
# # doc thong tin trong file
# # print(doc_file.readlines()[1])
# for ten in doc_file.readlines():
#     print(ten)

# doc_file.close()

# Writing Files
# doc_file = open("docfile.txt", "a")

# doc_file.write("\nQuang Vinh ")

# doc_file.close()

# # w: ghi đè lên mọi thứ
# doc_file = open("docfile.txt", "w")

# doc_file.write("\nQuang Vinh ")

# doc_file.close()

# doc_file = open("docfile2.txt", "w")
#
# doc_file.write("\nQuang Vinh ")
#
# doc_file.close()

# import cv2

# # Playing video from file:
# # cap = cv2.VideoCapture('vtest.avi')
# # Capturing video from webcam:
# cap = cv2.VideoCapture(0) # 0 is default webcam

# currentFrame = 0
# while (True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Handles the mirroring of the current frame
#     frame = cv2.flip(frame, 1)

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Saves image of the current frame in jpg file
#     # name = 'frame' + str(currentFrame) + '.jpg'
#     # cv2.imwrite(name, frame)

#     # Display the resulting frame
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     # To stop duplicate images
#     currentFrame += 1

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
