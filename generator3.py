import random
from PIL import Image, ImageDraw, ImageFont
import datetime ### 自力で追加

# 意味の通る文章のリスト
sentences = [
    "プロジェクトの目標を明確にしましょう。",
    "チームメンバーとのコミュニケーションを大切にしましょう。",
    "スケジュールを適切に管理しましょう。",
    "タスクを適切に分担しましょう。",
    "効果的なプレゼンテーションを行いましょう。",
    "問題解決には論理的思考が必要です。",
    "柔軟なアプローチを心がけましょう。",
    "失敗から学ぶことが大切です。",
    "成果を共有しましょう。",
    "フィードバックを受け入れる姿勢を持ちましょう。"
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
    
    # フォントの設定
    font_size = random.randint(20, 40)
    font = ImageFont.truetype("arial.ttf", font_size)
    
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
fileName = f"generateImages/Ver3/" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '-').replace('.', '-') + "_ver3.png"
slide.save(fileName, quality=95)
### 自力

# 生成したスライドを表示
slide.show()