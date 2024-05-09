import random
from PIL import Image, ImageDraw

def generate_slide():
    # 画像サイズ
    width = 800
    height = 600
    
    # 画像の背景色（ランダム）
    bg_color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    bg_color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 描画オブジェクトの生成
    slide = Image.new("RGB", (width, height), bg_color1)
    draw = ImageDraw.Draw(slide)
    
    # 直線の始点をランダムに設定
    start_x = random.randint(0, width)
    start_y = random.randint(0, height)
    
    # 直線の傾きをランダムに設定
    angle = random.uniform(0, 2 * 3.141592653589793)
    
    # 直線の終点を計算
    end_x = start_x + int(2000 * (width / 800) * (random.uniform(0.1, 0.9) * 0.5 * (2 * width * 0.5 * (1 - abs(start_y - height * 0.5) / (height * 0.5))) ** 0.5) * width * (random.choice([-1, 1]) / (width / 800)) * (random.choice([-1, 1]) / (height / 600)))
    end_y = start_y + int((end_x - start_x) * (random.uniform(0.1, 0.9) * 0.5 * (2 * width * 0.5 * (1 - abs(start_y - height * 0.5) / (height * 0.5))) ** 0.5) * (random.choice([-1, 1]) / (width / 800)) * (random.choice([-1, 1]) / (height / 600)))
    
    # 直線の描画
    draw.line([(start_x, start_y), (end_x, end_y)], fill=(0, 0, 0), width=3)
    
    # 生成したスライドを表示
    slide.show()

# スライド生成
generate_slide()
