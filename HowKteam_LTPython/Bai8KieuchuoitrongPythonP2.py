#chuỗi trần không quan tâm đến esecape sequence cú pháp : r
	#print(r'Haizz,\neu mot ngay nao do')
# toán tử cộng trong chuỗi
	#strA = "HowKteam.com\n"
	#strB = "Free education"
#strC = strA +"\n"+ 	strB
	#strC = strA*5
	#print (strC) 
#in khi sử dụng toán tử này chỉ nhận được 1 trong 2 đáp án là true hoặc false( kiểm tra xem 1 chuỗi có nằm trong 1 chuỗi khác hay không )
	#strA = "HowKteam"
#cắt chuỗi
#strB = strA[1:None]
#Bước nhảy
	#strB=strA[None:None:2]
# K IN HOA thì sẽ phát hiện nên true còn k thường thì sẽ ra false
#strB = "K"
#truy cập đến phần tử cuối cùng của chuỗi dùng hàm len/none
#strB = strA[len(strA)-1]
	#strC = strB in strA
#print(strC)
	#print(strB)
 #Ép Kiểu chuỗi thành số
	#strA = int('69') 
	#print(strA)
#Số thành chuỗi
	#strB = str(69) + "5"
	#print(strB)
#thay đổi giá trị trong chuỗi 
strA = "HowKteam.com"
strA = strA[None:1] + "0" + strA[3:None]
print(strA)