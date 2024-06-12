# BadSlideGenerator
WE ALWAYS WANT BAD SLIDES (These are written based on GPT-3.5 statements)

コードの保存部分のナンバリングは手動で変えています。
## What is bad slide?
以下のような方針でbad slideを作成させるようにした。
- 統一されてない書式
- 過剰な情報量
  - 過剰な文章量
  - 過剰なグラフ
  - 意味のない色付け
    - グラフの色付け
    - うるさい背景色
- 見にくさ
  - 目盛りのないグラフ
  - 重なるグラフ
  - 大量の矢印
  - 長すぎて画面外に出る文字列
## Ver1
最初に生成してくれたコード。いくつか自力で追記。

## Ver2
### 要求
- 文字列もっと長くして
- 文字列ずっと同じのままは嫌なのでランダムで変えて
### 結果
そういうことじゃねぇよ。

## Ver3
### 要求
- 意味の通る文章に
- 複数の文章を用意し、その中からランダムで指定
- 文章の内容については指定せず
### 結果
- 矢印を入れるのを忘れてる
- フォントが日本語対応してなかったため表示されず
- 文章が整列されている。なんでやねん。

## Ver4
### 要求
- 日本語と英語の文章を用意
- 複数のフォントを用意してランダムに選択(日本語対応してるフォントが含まれるように)
### 結果
- 日本語と英語混在させろって
- その他は概ねﾖｼ

## Ver5
### 要求
- 文字列をランダムな位置・回転で置いて
- 文章ごとにフォントを変えて
### 結果
**エラー出た💢💢💢💢💢💢**

## Ver6
### 要求
- エラー直せや
### 結果
- 過去あったけど廃止されたメソッドを使用していた。
- GPTはこの事実に気付けなかったため、自力で調べてGPTに教えた。
- randrangeの第2引数が第1引数よりも小さくなる場合があった。

## Ver7
### 要求
- 第2引数が第1引数より大きくなるように改善
### 結果
- なかなかいい!!!
- 傾きが適用されてないけどこれでもよい気がする。
- 用意した文章全部使ってる。別にこれでもいいかも。
- 順番はシャッフルしてもいいかも

## Ver8
### 要求
- ひとまず文字の改善はここまでにする
- 余白に適当なグラフ入れさせる
### 結果
- 折れ線グラフにしてきた(自分は棒グラフを想定)
- 全然余白ではない。

## Ver9
### 要求
- グラフの種類をランダムに。
- グラフの上に文字を描画する。
### 結果
- 定義されていない謎のdraw_graph関数を持ってきた。なんで???

## Ver10
### 要求
- エラーの改善を要求
### 結果
- draw_graphを定義しましたってGPTは言ってたけど全然定義してない。しかも別の箇所でエラーが出る。
- グラフは折れ線・棒・散布図の3種類。
- 散布図持ってくるんかい
- 棒グラフの時のみエラー

## Ver11
### 要求
- とりあえずエラーの内容を渡して改善するか確認
### 結果
- 流石に厳しかった。エラーの原因の確認は手動で行う必要がありそう。

## Ver12
### 要求
- y1の値がy0より小さくならないように
### 結果
- どうしても一つ前のコードから修正してきやがる。うぜぇ。
- もう手動で修正した方が早い。

## Ver10-1
- 手動でVer10から修正。

## Ver13
### 要求
- Ver10-1のプログラムを与え、そこから折れ線をカラフルにさせる。
### 結果
- `matplotlib.pyplot`をインポートし忘れていたので手動で追加
- エラーが出る
- 色の選択方法が悪さしてそう
- コードを与えたけどその与えたコードに則った形式になっていない。

## Ver14
### 要求
- バグの原因を指摘し改善を求める。
### 結果
- バグはうまく消えた
- グラフが文字より上に描画されてるのは改善されず。

## メモ
- 要求のあいまいな点を聞き返してこないのが人間との違い

## Ver15
### 要求
- グラフの個数をランダム
- グラフの大きさもランダム
- グラフの種類を個別に決めるように
### 結果
- また`randint`の範囲設定ミスしてる。いい加減にしてくれ。

## Ver16
### 要求
- バグの原因を通知し、修正する
### 結果
- 修正漏れしてる。行数を教えても漏れててカス。
- 修正してないのに修正したとか言ってくる。舐めとんちゃうぞ。
- 変えなくていいところを変える
- バグ修正は苦手そう。使い方が悪いかも。
- 埒が明かないため手動で修正。

## Ver17
### 要求
修正後のコードを渡してから要求
- 棒グラフは棒の間隔をあける
- 棒グラフの棒の太さもランダムにする
- グラフの上から文字が描画されるようにする
### 結果
- また廃止されたメソッド使ってる
- 修正後のコードを渡しても何にも反映されない。
- 埒が明かないので新しいチャットにコードを投げる
- **`randint`の引数は第1引数と第2引数が同じでもだめっぽい**(自力で修正)
- なぜか何も修正されなかった。話聞いてた?

## メモ
- コードが長くなってから修正の精度が落ちてる。

## Ver18
### 要求
- 17と同じ要求
### 結果
- 3つ目以外改善されず。

## Ver19
### 要求
- bar_width をランダムで決定し、それを基にして棒グラフの間隔を決めるよう指示。
### 結果
- なぜか棒グラフだけを生成するようになった。あほ。
- 太さはランダムになったが感覚は狭い。これは別に見逃してもええか…

## Ver20
### 要求
- 棒グラフが上向きになるように
- 棒グラフの位置もランダムに
### 結果
- チャット変える前と同じ間違いをやってる。
- 具体的な修正を提案して直してもらった。
- 要求は何も改善していない。

## メモ
- デバッグをやらせるのはマジでキツイ

## Ver21
### 要求
- 棒グラフの上下を逆に
### 結果
- さっきと同じミスをもう一回やった。ほんまにお前さぁ。

## Ver22
### 要求
- y=600でグラフを揃えて
### 結果
- やってくれたけど今自分の思い描いてるものを作ろうとするともはやAIの方が遅い。

## Ver23
### 改善点
- グラフの底のy座標をランダムに
- グラフの底のy座標によってグラフの向きを変える
- 他のグラフを混ぜる
- グラフの値の決め方を変更
- 散布図の点を少し大きく

## Ver24
### 要求
- グラフに目盛りを追加して
- 文字をランダムなx座標にして
### 結果
- 棒グラフだけ横方向だけの変なメモリができた
- 2つ目は改善なし

## Ver25
### 要求
- 縦の目盛りを追加して
- 文字をランダムなx座標にして
### 結果
- 棒グラフだけにはできた。
- 2つ目は改善なし

## Ver26
### 要求
- 目盛りを直線で繋いで
### 結果
- なんか変なとこを繋ぐ折れ線になってた

## Ver27
### 要求
- 横の目盛り、縦の目盛りそれぞれ一つの直線で結んで
### 結果
- これはこれでいい。

## Ver28
### 要求
- 目盛りを消す
- グラフを囲う
### 結果
- 棒グラフ以外は行けた

## Ver29
手作業です
### 改善点
- 囲いの長方形の位置調整
- グラフ背景の変更
- y軸方向のランダム性を追加
- その他バグ修正

## Ver30
### 要求
- 表示する文章の種類を増やす
- 文章をランダムで表示
### 結果
- 文の集まりをいくつか作ってそこから1つ選択して表示させたいと思ってたけど、文を16個用意してそこから15回文章の選択を行うようになった。まぁいいんじゃね
- その他は良好

## Ver31
### 要求
- 文字のスタイルをランダムに
- イタリックになる確率1/2、太字になる確率1/2(独立)
  - 色々上手くいかなかったので英語のフォントを追加させた
### 結果
- スタイルの指定が難しいことが分かったので断念。
- 代わりにフォントの種類を増やしてと頼んだらスタイル違いのフォント増やしてきた。できるなら最初からやれ。
- ↑で出てきたフォント、なかった…
- 英語のフォントは正常に追加できた。
- グラフの枠を前に出した(手動)

## Ver32
### 要求
- 背景に2色以上の色を用いること
### 結果
- 背景の要素の変数を1つ追加しただけで表示できていない。

## Ver33
### 要求
- 背景を分割してその境界で背景色が変わるように
### 結果
- `bottom_pos`の求め方をなぜか変えていてエラーが出る。
- 問い詰めたら間違いを認めて修正元のコードを提示してきた。
  - 本当に間違いを認識しているのか?文句を言われたから元に戻しただけの可能性も
- 上下で背景が2分割されるようになった。

## Ver34
### 要求
- 背景をランダムに分割し、その境界で背景を分割する(間違えた日本語で提出)
  - 「背景をランダムに分割し、その境界で背景色を変える」と言いたかった。
### 結果
- 間違えた日本語でもランダムに分割して色が変わるようにしてくれた
- ただし分割線は縦線のみ

## Ver35
### 要求
- ランダムな位置・傾きの直線で分割するように
### 結果
- 直線が途中で途切れるようになってしまう
- 傾きが一切反映されない

## Ver36
### 要求
- 傾きをランダムに
- 直線が途中で途切れることのないように
### 結果
- 直線がどの直線を指すのかを分からずに折れ線グラフの部分を編集
  - 多分命令した側が悪い

## Ver37
### 要求
- 直線が背景色を分割する直線であることを明示
### 結果
- グラフの描画部分が元に戻されないまま。

## Ver38
### 要求
- グラフの描画部分を元に戻す
- Ver36で行った要求を再度明示
### 結果
- 全然関係ないコード出てきた

## メモ
- 2つ以上前のコードの指定がうまくいかないことが多い。

## Ver39
### 要求
- コードを示して再度要求
### 結果
- なんか思ったのと違う
- 切片の位置が左端で固定っぽい?

## メモ
- 「なんか思ったのと違う」の原因究明は自力で行う必要アリ。

## Ver40
### 要求
- 切片のx軸方向の位置をランダムで決める
### 結果
- 画像内で通る点をランダムで決めるようになった
  - 要求は達成してる。
- カッコよくなってる気もする(あんまりよくない)。

## ここからの方針
- グラデーション
- 余白を小さめに
- 矢印を入れる

## Ver41
### 要求
- 背景をグラデーションに。
- Ver40で求めた直線のもとにグラデーションの方向を決めて。
### 結果
- 直線は求められてる
- グラデーションもできてる
- グラデーションがなぜか横方向のみ
- 1ピクセルずつ処理してるので時間がかかります。

## Ver42
### 要求
- 現状では横方向のみでしか直線が変化していないことを伝える
- グラデーションの方向は直線の傾きのみに依存するように
- 「大丈夫です。あなたならできます。」という文言を追加
### 結果
- 概ねうまくいっている
- グラデーションはこれでOKかも
- 「大丈夫です。あなたならできます。」の効果は不明 (この文言に反応したようなメッセージではなかった)

## Ver43
### 要求
- 文字やグラフを繋ぐ矢印を追加
### 結果
- 矢印の色が白色
  - 見にくいのはいい (クソ度合いが高い) んだけど矢印は矢印として伝わってほしい
- 矢印同士が繋がってる (カオスには見えるけど繋がってる必要はそんなにない)
  - 矢印はオブジェクトをランダムにつないでほしい

## Ver44
### 要求
- 矢印の色を黒色に
- ランダムなオブジェクトを繋ぐように
### 結果
- 要求通りよくできてます。

## Ver45
### 要求
- 矢印の太さをランダムに
### 結果
- 矢印の太さは変わったけど先端の大きさはそのまま。

## Ver46
### 要求
- 矢印の太さに応じて先端の大きさも変える。
### 結果
- 変えてはいるが太い矢印の先端を大きくするのではなく、細い矢印の先端を小さくしているっぽい。

## Ver47
### 要求
- 矢印の先端を大きくする
### 結果
- うまくいってる
