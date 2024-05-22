import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
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
    "Be open to feedback.",
    "Teamwork makes the dream work.",
    "Attention to detail leads to success.",
    "Continuous improvement is key.",
    "Embrace challenges as opportunities.",
    "Stay focused on your goals.",
    "Creativity fuels innovation."
]

# フォントリスト
font_names = [
    "arial.ttf",  # 英語対応フォント
    "arialbd.ttf",  # 英語対応フォント（太字）
    "ariali.ttf",  # 英語対応フォント（イタリック）
    "times.ttf",  # 英語対応フォント
    "verdana.ttf",  # 英語対応フォント
    "calibri.ttf"  # 英語対応フォント
]

# グラフの種類
graph_types = ['line', 'bar', 'scatter']

# グラフの種類
def plot_graph(draw, x_values, y_values, bar_width, bottom_pos):
    graph_type = random.choice(graph_types)
    if graph_type == 'line':
        for i in range(len(x_values) - 1):
            if (bottom_pos <= 300):
                draw.line([(x_values[i], y_values[i] + bottom_pos), (x_values[i+1], y_values[i+1] + bottom_pos)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=random.randint(1, 5))
            else:
                draw.line([(x_values[i], bottom_pos - y_values[i]), (x_values[i+1], bottom_pos - y_values[i+1])], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=random.randint(1, 5))
    elif graph_type == 'bar':
        for x, y in zip(x_values, y_values):
            if (bottom_pos <= 300):
                draw.rectangle([(x - bar_width / 2, bottom_pos), (x + bar_width / 2, bottom_pos + y)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            else:
                draw.rectangle([(x - bar_width / 2, bottom_pos - y), (x + bar_width / 2, bottom_pos)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    elif graph_type == 'scatter':
        for x, y in zip(x_values, y_values):
            if (bottom_pos <= 300):
                draw.ellipse([(x - 5, y - 5 + bottom_pos), (x + 5, y + 5 + bottom_pos)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            else:
                draw.ellipse([(x - 5, bottom_pos - y - 5), (x + 5, bottom_pos - y + 5)], fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def generate_slide():
    # 画像サイズ
    width = 800
    height = 600
    
    # 画像の背景色（ランダム）
    bg_color1 = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    bg_color2 = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    
    # 描画オブジェクトの生成
    slide = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(slide)
    
    # 直線の傾きをランダムに設定
    angle = random.randint(0, 180)
    angle_radians = np.radians(angle)
    slope = np.tan(angle_radians)
    
    # 直線の切片をランダムに設定
    intercept_x = random.randint(0, width)
    intercept_y = random.randint(0, height)
    intercept = intercept_y - slope * intercept_x
    
    # グラデーションを適用
    for x in range(width):
        for y in range(height):
            t = (x * slope + intercept) / (width + height)
            t = max(0, min(1, t))
            color = (bg_color1 * (1 - t) + bg_color2 * t).astype(int)
            slide.putpixel((x, y), tuple(color))
    
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
        
        bottom_pos = random.randint(0, 600)
        
        # 長方形でグラフを囲む
        if (bottom_pos <= 300):
            draw.rectangle([(position - bar_width, bottom_pos), (position + width + bar_width, height + bottom_pos)], fill="grey", width=2)
        else:
            draw.rectangle([(position - bar_width, bottom_pos - height), (position + width + bar_width, bottom_pos)], fill="grey", width=2)
        
        plot_graph(draw, x_values, y_values, bar_width, bottom_pos)
        
        # 長方形でグラフを囲む
        if (bottom_pos <= 300):
            draw.rectangle([(position - bar_width, bottom_pos), (position + width + bar_width, height + bottom_pos)], outline="black", width=2)
        else:
            draw.rectangle([(position - bar_width, bottom_pos - height), (position + width + bar_width, bottom_pos)], outline="black", width=2)
    
    # ランダムなフォントと位置、傾きの設定
    y_position = 50
    for _ in range(15):  # 15回文章を表示する
        # ランダムな文章の選択
        sentence = random.choice(sentences)
        
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

# 保存
fileName = f"generateImages/Ver41/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver41.png"
slide.save(fileName, quality=95)

# 生成したスライドを表示
slide.show()
