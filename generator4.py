import random
import string
from PIL import Image, ImageDraw, ImageFont
import datetime ### 自力で追加

# 日本語と英語の文章のリスト
sentences = [
    "Let's clarify the project goals.",
    "Communication with team members is important.",
    "Manage the schedule properly.",
    "Divide tasks properly.",
    "Make effective presentations.",
    "Logical thinking is necessary for problem solving.",
    "Strive for a flexible approach.",
    "Learning from failure is important.",
    "Share your achievements.",
    "Be open to feedback."
]

# 日本語対応のフォントリスト
font_names = [
    "arial.ttf",  # 英語対応フォント
    "msmincho.ttc",  # 日本語対応フォント（MS 明朝）
    "meiryo.ttc"  # 日本語対応フォント（Meiryo）
]

def generate_slide():
    # 画像サイズ
    width = 800
    height = 600
    
    # 画像の背景色（ランダム）
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 描画オブジェクトの生成
    slide = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(slide)
    
    # ランダムなフォントの選択
    font_name = random.choice(font_names)
    
    # フォントの設定
    font_size = random.randint(20, 40)
    font = ImageFont.truetype(font_name, font_size)
    
    # ランダムな文の数
    num_sentences = random.randint(2, 4)
    
    # ランダムな文章の選択と配置
    y_position = 50
    for _ in range(num_sentences):
        sentence = random.choice(sentences)
        draw.text((50, y_position), sentence, fill=(255, 255, 255), font=font)
        y_position += font_size + 10  # 文と文の間隔を空ける
    
    return slide

# スライド生成
slide = generate_slide()

### 自力
fileName = f"generateImages/Ver4/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver4.png"
slide.save(fileName, quality=95)
### 自力

# 生成したスライドを表示
slide.show()
