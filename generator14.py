import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import datetime

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
    # カラーマップからランダムに色を選択
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(len(x_values))]
    
    graph_type = random.choice(['line', 'bar', 'scatter'])
    if graph_type == 'line':
        for i in range(len(x_values) - 1):
            draw.line([(x_values[i], y_values[i]), (x_values[i+1], y_values[i+1])], fill=colors[i], width=random.randint(1, 5))
    elif graph_type == 'bar':
        bar_width = random.randint(5, 20)
        for x, y, color in zip(x_values, y_values, colors):
            draw.rectangle([(x - bar_width // 2, 0), (x + bar_width // 2, y)], fill=color)
    elif graph_type == 'scatter':
        for x, y, color in zip(x_values, y_values, colors):
            draw.ellipse([(x - 3, y - 3), (x + 3, y + 3)], fill=color)

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
    plot_random_graph(np.linspace(50, width - 50, 10), np.random.randint(50, height - 50, 10), draw)
    
    return slide

# スライド生成
slide = generate_slide()

### 自力
fileName = f"generateImages/Ver14/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver14.png"
slide.save(fileName, quality=95)
### 自力

# 生成したスライドを表示
slide.show()