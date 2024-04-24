import random
import string
from PIL import Image, ImageDraw, ImageFont

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
    
    # ランダムなフォントと位置、傾きの設定
    y_position = 50
    for sentence in sentences:
        # ランダムなフォントの選択
        font_name = random.choice(font_names)
        
        # フォントの設定
        font_size = random.randint(20, 40)
        font = ImageFont.truetype(font_name, font_size)
        
        # 文字列の幅と高さを取得
        text_width, text_height = draw.textsize(sentence, font=font)
        
        # ランダムな位置と傾きの設定
        x_position = random.randint(50, width - text_width - 50)
        angle = random.randint(-15, 15)
        
        # 文字列の描画
        draw.text((x_position, y_position), sentence, fill=(255, 255, 255), font=font, align="center", spacing=10)
        
        # 次の文章のために y_position を更新
        y_position += text_height + random.randint(10, 30)
    
    return slide

# スライド生成
slide = generate_slide()

# 生成したスライドを表示
slide.show()
