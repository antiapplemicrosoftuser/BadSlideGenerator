import random
import string
from PIL import Image, ImageDraw, ImageFont
import datetime ### 自力で追加

def generate_slide():
    # 画像サイズ
    width = 800
    height = 600
    
    # 画像の背景色（ランダム）
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 描画オブジェクトの生成
    slide = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(slide)
    
    # フォントの設定
    font_size = random.randint(20, 40)
    font = ImageFont.truetype("arial.ttf", font_size)
    
    # ランダムな文字列の生成
    text_length = random.randint(50, 200)
    text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=text_length))
    
    # テキストの配置（ランダム）
    text_position = (random.randint(50, width-150), random.randint(50, height-100))
    draw.multiline_text(text_position, text, fill=(255, 255, 255), font=font)
    
    # 矢印の描画（ランダム）
    num_arrows = random.randint(1, 5)
    for _ in range(num_arrows):
        arrow_start = (random.randint(50, width-50), random.randint(50, height-50))
        arrow_end = (random.randint(50, width-50), random.randint(50, height-50))
        draw.line([arrow_start, arrow_end], fill=(255, 255, 255), width=3)
    
    return slide

# スライド生成
slide = generate_slide()

### 自力
fileName = f"generateImages/Ver2/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver2.png"
slide.save(fileName, quality=95)
### 自力

# 生成したスライドを表示
slide.show()