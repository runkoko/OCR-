# 以本示例中文件夹下图片为待预测图片。本教程为大家总共提供了5个具体场景下的ocr识别，分别是「身份证识别」、「火车票识别」、「快递单识别」、「广告信息识别」、「网络图片文字识别」。
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

# 待预测图片
test_img_path = ["./advertisement.jpg", "./pics.jpg", "./identity_card.jpg", "./express.jpg", "./railway_ticket.jpg"]

# 展示其中广告信息图片
img1 = mpimg.imread(test_img_path[0]) 
plt.figure(figsize=(10,10))
plt.imshow(img1) 
plt.axis('off') 
