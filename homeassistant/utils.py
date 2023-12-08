import cv2
import numpy as np

def get_image_points(img_name:str)-> list:
    #图片尽量不要有大面积的黑色块，以免和黑点混淆
    """
        top: (y/600) %
        left:(x/800) %
        return: [(x,y),...]
    """
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # 形态学操作（膨胀）增加黑点的大小
    kernel = np.ones((9, 9), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=1)

    # 使用findContours函数查找图像中的轮廓
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    points = []

    for contour in contours:
        area = cv2.contourArea(contour)

        # 如果面积小于50，则认为这是一个黑点
        if area < 50:
            x, y, w, h = cv2.boundingRect(contour)
            points.append((x, y))
    return (points)
    
    

import cv2
import numpy as np

def embed_image(small_image_path, big_image_path, scale_ratio, position):
    # 读取小图片和大图片
    small_image = cv2.imread(small_image_path, cv2.IMREAD_UNCHANGED)
    big_image = cv2.imread(big_image_path)

    # 获取小图片的尺寸
    small_height, small_width, _ = small_image.shape

    # 根据缩放比例计算新的尺寸
    new_height = int(small_height * scale_ratio)
    new_width = int(small_width * scale_ratio)

    # 缩放小图片
    small_image_resized = cv2.resize(small_image, (new_width, new_height))

    # 获取小图片在大图片中的位置
    x, y = position
    
    # 创建小图片的透明度掩码
    alpha_mask = small_image_resized[:, :, 3] / 255.0  # 将透明度值归一化到0-1范围

    # 将小图片嵌入到大图片中
    for c in range(3):
        big_image[y:y+new_height, x:x+new_width, c] = \
            small_image_resized[:, :, c] * alpha_mask + \
            big_image[y:y+new_height, x:x+new_width, c] * (1 - alpha_mask)

    # 返回嵌入后的大图片
    return big_image
    
    
def embed_image_fixed(small_image_path, big_image_path, scale_ratio, position):
    # 读取小图片和大图片
    small_image = cv2.imread(small_image_path, cv2.IMREAD_UNCHANGED)
    big_image = cv2.imread(big_image_path)

    # 获取小图片的尺寸
    small_height, small_width, _ = small_image.shape

    # 根据缩放比例计算新的尺寸
    new_height = int(small_height * scale_ratio)
    new_width = int(small_width * scale_ratio)

    # 缩放小图片
    small_image_resized = cv2.resize(small_image, (new_width, new_height))

    # 获取小图片在大图片中的位置
    x, y = position
    x -= int(new_width/2)
    y -= int(new_height/2)
    # 创建小图片的透明度掩码
    alpha_mask = small_image_resized[:, :, 3] / 255.0  # 将透明度值归一化到0-1范围

    # 将小图片嵌入到大图片中
    for c in range(3):
        big_image[y:y+new_height, x:x+new_width, c] = \
            small_image_resized[:, :, c] * alpha_mask + \
            big_image[y:y+new_height, x:x+new_width, c] * (1 - alpha_mask)

    # 返回嵌入后的大图片
    return big_image



def write_image()
    
#png透明背景   


small_image_path = 'telephone.png'

big_image_path = 'a.png'
scale_ratio = 0.2
position = get_image_points(big_image_path)[0] 

result_image = embed_image(small_image_path, big_image_path, scale_ratio, position)

# 保存结果图片
cv2.imwrite('result_image.jpg', result_image)



    
    
