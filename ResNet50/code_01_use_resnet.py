import base64

import matplotlib.pyplot as plt
import tensorflow as tf
from keras.applications.resnet50 import (
    ResNet50,
    decode_predictions,
    preprocess_input,
)

tf.compat.v1.disable_v2_behavior()  #以静态图的形式处理

# 输入类型为string
input_imgs = tf.compat.v1.placeholder(shape=None, dtype=tf.string)

#把Base64字符串图解码成jpeg格式

decoded = tf.image.decode_jpeg(tf.compat.v1.decode_base64(input_imgs), channels=3)

#用邻近法调整图像大小到[224,224],因为ResNet50需要入图像的大小是[224, 224]
decoded = tf.compat.v1.image.resize_images(decoded, [224, 224], tf.image.ResizeMethod.NEAREST_NEIGHBOR)

#在0位置增加一个值是1的维度，使其成为一个图像
tensorimg = tf.expand_dims(tf.cast(decoded, dtype=tf.float32), 0)

tensorimg = preprocess_input(tensorimg) #图像预处理

with tf.compat.v1.Session() as sess:    #构建一个新会话
    sess.run(tf.compat.v1.global_variables_initializer())
    #加载ResNet50模型
    Reslayer = ResNet50(weights='resnet50_weights-tf_dim_ordering_tf_kernels.h5')
    logits = Reslayer(tensorimg) #获取模型的输出节点

    #得到图片中的每个类别的概率值
    prediction = tf.squeeze(tf.cast(tf.argmax(logits, 1), dtype=tf.int32), [0])

    img_path = './dog.jpg'
    
    with open(img_path, "rb") as image_file:
        #把图像编码成base64字符串格式
        encoded_string = str(base64.urlsafe_b64encode(image_file.read()), "utf-8")
    
    img, logitsv, Pred = sess.run([decoded, logits, prediction], feed_dict={input_imgs: encoded_string})

    print("Pred label ID, ", Pred) #预测标签ID
        # 从预测结果中取出前三名
    Pred = decoded_predictions(logitsv, top=3)[0]
    print('Predicted:', Pred, len(logitsv[0]))

    #可视化处理，创建一个1行2列的子图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 8))
    fig.sca(ax1)    #设置第一轴是ax1, plt.sca(ax1) 写成 fig.sca 也可以，但 mpl 不推荐
    ax1.imshow(img) #第一个子图要显示的图片

    #设置第二个子图为预测结果，按概率取前三
    barlist = ax2.bar(range(3), [i[2] for i in Pred])
    barlist[0].set_color('g')    #设置颜色为绿色

    #预测结果中前三名的柱状图
    plt.sca(ax2)
    plt.ylim([0, 1.1])

    #竖直显示前三名的标签
    plt.xticks(range(3), [i[1][:5] for i in Pred], rotation='vertical')
    fig.subplots_adjust(bottom=0.2)     #调整第二个子图的位置
    plt.show()  #显示图片

