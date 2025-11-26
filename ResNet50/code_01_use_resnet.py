import base64
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# -----------------------------
# 加载模型
# -----------------------------
model = ResNet50(weights='imagenet')

# -----------------------------
# 加载图片并转成 base64 示例
# -----------------------------
img_path = "D:/code/AI_Python/ResNet50/test_image.jpg"
with open(img_path, "rb") as f:
    encoded_string = base64.b64encode(f.read())

# -----------------------------
# base64 → Image → numpy
# -----------------------------
img_bytes = base64.b64decode(encoded_string)
#默认为最近邻法
#img = Image.open(BytesIO(img_bytes)).resize((224, 224))

# 算法	描述
# Image.NEAREST	最邻近插值，最快，但粗糙
# Image.BILINEAR	双线性插值，平滑，速度较快
# Image.BICUBIC	三次卷积插值，更平滑，速度稍慢
# Image.LANCZOS	Lanczos 插值，高质量，速度最慢

#双线性插值，平滑，速度较快
img = Image.open(BytesIO(img_bytes)).resize((224, 224), resample=Image.BILINEAR)

x = np.expand_dims(np.array(img), axis=0)
x = preprocess_input(x)  # Keras 预处理

# -----------------------------
# 模型预测
# -----------------------------
logits = model(x, training=False)  # Eager 模式
pred_class = np.argmax(logits, axis=1)[0]

top3 = decode_predictions(logits.numpy(), top=3)[0]
print("Predicted class ID:", pred_class)
print("Top-3 predictions:")
for _, label, prob in top3:
    print(f"{label}: {prob*100:.2f}%")

# -----------------------------
# 可视化
# -----------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(img)
ax1.axis('off')

ax2.bar(range(3), [i[2] for i in top3], color=['g','b','r'])
ax2.set_ylim([0, 1])
ax2.set_xticks(range(3))
ax2.set_xticklabels([i[1][:10] for i in top3], rotation=45)
plt.show()
