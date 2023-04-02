# # OpenCV - Open Computer Vision
# import cv2
# # 1.Doc anh tu file : dua duong dan vao (neu khong se bi loi) ,       cv2.IMREAD_GRAYSCALE: anh den trang...v.v...
# image = cv2.imread("D:\Workspace\Python\Image_Processing\Vinh.jpg", cv2.IMREAD_GRAYSCALE)
# # Show anh
# cv2.imshow("Frame", image)
# # Dung man hinh : neu go ban phim moi tat con khong thi: thoi gian tuy chinh ms
# cv2.waitKey()
# # Dong cac cua so
# cv2.destroyAllWindows()

# --------------------------------------------------------------------------------------------------------------------#

# # 2. Doc anh tu camera
# import cv2
# # cac camera trong he thong se duoc danh so tu 0 tro di
# # camera_id = 0
# # Neu muon doc video thi them duong dan vao
# camera_id = 'D:\Workspace\Python\Image_Processing\Test.mp4'
# # Mo camera
# cap =cv2.VideoCapture(camera_id)
# # Doc anh tu camera
# while(True):
#     # Doc anh
#     ret, frame = cap.read()
#     # Hien anh
#     cv2.imshow("Cam",frame)
#     # Kiem tra neu bam x thi thoat
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break
# # Giai phong camera
# cap.release()
# cv2.destroyAllWindows

# --------------------------------------------------------------------------------------------------------------------#

# # Luu anh
# import cv2
# # Doc anh xam vao bien image
# image = cv2.imread(
#     "D:\Workspace\Python\Image_Processing\Vinh.jpg", cv2.IMREAD_GRAYSCALE)
# # Luu anh den trang
# cv2.imwrite("D:\Workspace\Python\Image_Processing\Vinh_gray.jpg", image)

# --------------------------------------------------------------------------------------------------------------------#

# Chuyen doi mau anh
import cv2
# Doc anh mau
image = cv2.imread("D:\Workspace\Python\Image_Processing\Vinh.jpg")
cv2.imshow("Anh mau", image)
cv2.waitKey()
# CVT qua anh mau mong muon
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Anh xam", image_gray)
cv2.waitKey()
cv2.destroyAllWindows()
