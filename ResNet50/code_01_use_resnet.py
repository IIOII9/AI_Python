import base64
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
tf.compat.v1.disable_v2_behavior

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
    
