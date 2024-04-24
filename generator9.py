import random
import string
import numpy as np
import matplotlib.pyplot as plt
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

# グラフの種類
def plot_random_graph(x_values, y_values, draw):
    graph_type = random.choice(['line', 'bar', 'scatter'])
    if graph_type == 'line':
        draw.line(list(zip(x_values, y_values)), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=random.randint(1, 5))
    elif graph_type == 'bar':
        for x, y in zip(x_values, y_values):
            draw.rectangle([(x - 5, y), (x + 5, 0)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    elif graph_type == 'scatter':
        for x, y in zip(x_values, y_values):
            draw.ellipse([(x - 3, y - 3), (x + 3, y + 3)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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
        
        # テキストのbboxを取得
        text_bbox = draw.textbbox((0, 0), sentence, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # ランダムな位置と傾きの設定
        max_x_position = width - text_width - 50
        if max_x_position <= 50:  # 最小の横幅より小さい場合、50にする
            max_x_position = 50
        x_position = random.randint(50, max_x_position)
        
        angle = random.randint(-15, 15)
        
        # 文字列の描画
        draw.text((x_position, y_position), sentence, fill=(255, 255, 255), font=font, align="center", spacing=10)
        
        # 次の文章のために y_position を更新
        y_position += text_height + random.randint(10, 30)
    
    # 余白にグラフを描画
    draw_graph(draw, width, height)
    
    return slide

# スライド生成
slide = generate_slide()

# 生成したスライドを表示
slide.show()
