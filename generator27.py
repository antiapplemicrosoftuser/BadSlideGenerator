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

### グラフの種類
graph_types = ['line', 'bar', 'scatter']

# グラフの種類
def plot_graph(draw, x_values, y_values, bar_width):
    graph_type = random.choice(graph_types)
    if graph_type == 'line':
        for i in range(len(x_values) - 1):
            draw.line([(x_values[i], y_values[i]), (x_values[i+1], y_values[i+1])], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=random.randint(1, 5))
    elif graph_type == 'bar':
        y_bar = random.randint(0, 600)
        for x, y in zip(x_values, y_values):
            if (y_bar <= 300):
                draw.rectangle([(x - bar_width / 2, y_bar), (x + bar_width / 2, y_bar + y)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            else:
                draw.rectangle([(x - bar_width / 2, y_bar - y), (x + bar_width / 2, y_bar)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # Add tick marks
            draw.line([(x, y_bar), (x, y_bar + 5)], fill="black", width=2)
        # Add vertical tick marks
        for y_tick in range(0, 600, 100):
            draw.line([(x_values[0], y_tick), (x_values[-1], y_tick)], fill="black", width=2)
        # Connect tick marks with lines
        draw.line([(x_values[0], 0), (x_values[0], 600)], fill="black", width=2)
        draw.line([(x_values[-1], 0), (x_values[-1], 600)], fill="black", width=2)
        for i in range(len(x_values) - 1):
            draw.line([(x_values[i], y_values[i]), (x_values[i+1], y_values[i+1])], fill="black", width=2)
    elif graph_type == 'scatter':
        for x, y in zip(x_values, y_values):
            draw.ellipse([(x - 5, y - 5), (x + 5, y + 5)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def generate_slide():
    # 画像サイズ
    width = 800
    height = 600
    
    # 画像の背景色（ランダム）
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 描画オブジェクトの生成
    slide = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(slide)
    
    # ランダムなグラフの個数と大きさを設定
    num_graphs = random.randint(1, 5)
    graph_widths = [random.randint(50, 150) for _ in range(num_graphs)]
    graph_heights = [random.randint(50, height - 100) for _ in range(num_graphs)]
    graph_positions = random.sample(range(50, width - 50), num_graphs)  # ランダムな位置に修正
    
    # グラフの描画
    for width, height, position in zip(graph_widths, graph_heights, graph_positions):
        x_values = np.linspace(position, position + width, 10)
        y_values = np.random.randint(0, height, 10)
        
        # バーの幅をランダムに決定
        bar_width = random.randint(5, 20)
        
        plot_graph(draw, x_values, y_values, bar_width)
    
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
    
    return slide

# スライド生成
slide = generate_slide()

### 自力
fileName = f"generateImages/Ver27/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver27.png"
slide.save(fileName, quality=95)
### 自力

# 生成したスライドを表示
slide.show()
