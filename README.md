# レッド・スター

# ゲームの説明
このゲームはすばやい動きが求められる。<br>
ゲームを続けるには、赤い星をクリックしなければなならい。<br>
他の星をクリックするとやっかいなことになります。<br>

ゲームが始まると星が２つ現れて画面の下へと落ちていく。<br>
星が画面の一番下に着く前に、赤い星をクリックしなければならない。<br>
赤い星がクリックされれるたびに、レベルが上がる。<br>
レベルが上がると緑と青の星が増えていき、星が落ちるスピードも速くなる。<br>
赤以外の色の星をクリックか、星が画面の一番下に着いてしまうとゲームオーバー。<br>

# フローチャート
<img width="740" height="671" alt="Red・Star drawio" src="https://github.com/user-attachments/assets/f600496a-365e-4435-ba01-fb9bc374f348" />

## 事前準備

Pygame Zeroのインストール(Windows環境)<br>

1. コマンドプロンプトを開く<br>
2. パッケージマネージャーをインストールする<br>
```
python -m pip install -U pip
```
3. pygameのインストール<br>
   パッケージマネージャーをインストールしたら下記の<br>
   命令文を入力しENTERキーを押すこれでPygameがインストールされます。<br>
   ```
   pip install pygame
   ```
4. Pygame Zeroのインストール<br>
   最後に下記の命令文を入力しENTERキーを押す。<br>
   これでPygame Zeroがインストールされる。<br>
   ```
   pip install pgzero
   ```

# プログラミング

**1. 準備**<br>
IDLEを起動しFileメニューからNew Fileを選んで<br>
新しいファイルを作成する。<br>
<img width="204" height="308" alt="スクリーンショット 2025-09-07 072707" src="https://github.com/user-attachments/assets/a817ac8b-b29d-442b-a2c4-761a8657a1a6" />
<br>
**2. セーブする**<br>
フォルダーを新しく作成し、**Fileメニュー**内の**Save As**を選び**red.py**という名前で保存。<br>
<br>
**3. 画像用フォルダー**<br>
新しくimagesというフォルダを作成しRed-Starのフォルダの中に保存<br>
<br>
**4. 画像をセットする**<br>
Red Sta用画像を保存する。<br>
<br>
**5. モジュールの組み入れ**<br>
最初にしなければならないのは、**Python**の**random**のモジュールを組み入れること。<br>
モジュール全体を組み入れるには、**import**と書き、続けてモジュールの名前を書けばよい。<br>
今回は**random**モジュールの``choice()``関数と``shuffle()``関数を使用します。<br>

**ソースコード**
```
import random
```

> [!NOTE]
> これでrandomモジュールが組みいれらることができます。

**6. 定数の宣言**<br>
ふつう、定数はプログラムの最初の部分で定義します（「宣言する」とも言います）。<br>
定数と呼ばれる由来は、代入した値を変えずに使用するから。<br>

**ソースコード**
```
FONT_COLOUR = (255, 255, 255)
WIDTH = 800
HEIGHT = 800
CENTRE_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTRE = (CENTRE_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLOURS = ["green", "blue"]
```

**解説**
```
FONT_COLOUR = (255, 255, 255)
```
> [!NOTE]
> ゲームの終わりに表示されるメッセージの文字の色を決めている。

```
WIDTH = 800
HEIGHT = 600
```

> [!NOTE]
> この2つの定数にはゲームの画面サイズが代入されている。

```
FINAL_LEVEL = 6
```
> [!NOTE]
> ゲームのレベルをセット

```
START_SPEED = 10
```

> [!NOTE]
> 星が下に動くスピードを決めている定数。

```
COLOURS = ["green", "blue"]
```

> [!NOTE]
> クリックしてはいけない星の色はここで指定されている。

**7. グローバル変数を宣言する**<br>
定数と同じようにグローバル変数も、ふつうはプログラムの先頭で宣言（定義）しますが、定数と違って中の値は変えられます。<br>
このゲームではグローバル変数を利用してゲームの進行をコントロールしていきます。<br>

**ソースコード**
```
game_over = False
game_complete = False
current_level = 1
stars =[]
animations = []
```

**解説**

```
game_over = False
game_complete = False
```

>[!NOTE]
>これらの変数で、ゲームオーバーかどうかを判断します。

```
current_level = 1
```

>[!NOTE]
>現在のプレイヤーのレベルを記録し続けます。

```
stars =[]
animations = []
```

>[!NOTE]
>この2つのリストで画面上の星をコントロールし続けます。

> [!TIP]
> **定数**<br>
> プログラミングの定数は、最初に代入した値を変えてはいけない変数と考えることができます。<br>
> プログラマーは定数の値を変えないよう、わざと大文字で名前をつけ、分かりやすくしています。<br>
> このルールを「命名規則」と呼びます。<br>
> このルールを守ってプログラミングしているから、ソースコードは見た目が似ていて理解しやすい。<br>

**8. 星を描く**<br>
関数を定義していきます。<br>
draw()関数を使って星を描き、画面にメッセージを表示させます。<br>

**ソースコード**

```
def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    if geme_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "well done.")
    else:
        for star in stars:
            star.draw()
```

**解説**

```
    global stars, current_level, game_over, game_complete
```
>[!NOTE]
>この関数で使用するグローバル変数。

```
    screen.blit("space", (0, 0))
```
>[!NOTE]
>この行でゲーム画面の背景画像をセットしています。

```
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "well done.")
```

>[!NOTE]
>ゲームオーバーになるかゲームがコンプリートされたときは、
>この部分で画面にメッセージを表示させます。

```
    else:
        for star in stars:
            star.draw()
```

>[!NOTE]
>このブロックが画面に星を描きます。

**9. update()関数を定義する**<br>
定義した``draw()``関数は星をあらかじめ作成しておかないと何も描かないです。<br>
そこで**stars**リストに星が入っているかチェックし、入っていなければ<br>
作ろうとする``update()``関数を定義します。<br>
星が無いときは、``make_stars()``関数を呼び出すようになっています。<br>

**ソースコード**
```
def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)
```

**解説**
```
    if len(stars) == 0:
```

>[!NOTE]
>すでに星が作られてるかをここでチェックします。

```
        stars = make_stars(current_level)
```
>[!NOTE]
>リスト**stars**に何も入ってないなら``make_stars()``の関数を呼び出す。

**10. 星を作る**<br>
``make_stars()``関数を作成していく。
この関数は他の関数をいくつか呼び出すようになっています。

**ソースコード**
```
def make_stars(number_of_extra_stars):
    colours_to_create = get_colours_to_create(number_of_extra_stars)
    new_stars = create_stars(colours_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars
```

**解説**
```
    colours_to_create = get_colours_to_create(unmber_of_extra_stars)
```
>[!NOTe]
>星を描くために必要な、星の色のリストが戻り値になっている。

```
    new_stars = create_stars(colours_to_create)
```
>[!NOTE]
>色のリストを引数にして、星ごとにアクターをを作成するための関数。

```
    layout_stars(new_stars)
```
>[!NOTE]
>星を画面の決められた位置に置いていく関数。

```
    animate_stars(new_stars)
```
>[!NOTE]
>星を画面下に向けて動かす関数。

**11. 関数のための場所取り**<br>
ソースコードをテストする前に、必要なすべての関数を作成。<br>
今のところは、``get_colours_to_create()``関数と``create_stars()``関数は<br>
**returm[]**で空っぽのリストを戻り値にしておきます。<br>
``layout_stars()``関数と``animate_stars()``関数はキーワードの**pass**を使って場所取りの設定を行っておく。

**ソースコード**
```
def get_colours_to_create(number_of_extra_stars):
    return []

def create_stars(colours_to_create):
    return []

def layout_stars(stars_to_layout):
    pass

def animate_stars(stars_to_animate):
    pass
```

**12. ソースコードをテスト**<br>
コマンドプロンプト（またはターミナル(PowerShell)）ウィンドウのコマンドラインから実行。<br>
現段階では、まだ星は1つも画面に表示されない状態。<br>
ここで書いたコードにバグがあるかチェックを行う。<br>

```
pgzrun
```

>[!NOTE]
>``red.py``のファイルをドラッグして実行する。

**13. 色リストに色をセットする**<br>
このゲームは、赤、青、緑いろの星を使用します。<br>
まず文字列の「red」(赤)を1つ入れたリストを作成し、変数**colours_to_create**に代入します。<br>
このリストは赤から始まることになる。<br>
画面には赤い星を必ず1個だけ表示する。<br>
赤以外に緑と青の星を加えるため、**number_of_extra_stars**を引数にしてループを動かします。<br>
追加する星の色を緑にするか青にするかはランダムに決める設定。<br>
書いた**def get_colours_to_create(number_of_extra_stars)** のあとの**return []** のソースコードを書き換えていく。<br>

**ソースコード**

```
    colours_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_colour = random.choice(COLOURS)
        colours_to_create.append(random_colour)
    return colours_to_create
```
**解説**

```
    colours_to_create = ["red"]
```

>[!NOTE]
>リストの最初の星を赤色に指定しています。<br>

```
    for i in range(0, number_of_extra_stars):
```
>[!NOTE]
>ループが実行されるとiに１が加えられて、iの値がrangeの範囲内のうちはループが繰り返されます。<br>

```
        random_colour = random.choice(COLOURS)
```
>[!NOTE]
>星を加えるごとに色を1つランダムに決めます。

```
        colours_to_create.append(random_colour)
```

>[!NOTE]
>リストに決められた色を追加します。

**14. 星を作る**<br>
画面に星を描かならないため、``new_stars``と言う空っぽのリストを作成することがら始めます。<br>
そして``colours_to_create``というリストのアイテムをループで取り出しながら、指定されている色で新しい星のアクターを作成します。<br>
作成した星をリスト``new_stars``に入れていく。<br>
``def create_stars(colours_to_create)``の後の``return[]``を書き換えていく。<br>

**ソースコード**
```
    new_stars = []
    for colour in colours_to_create:
        star = Actor(colour + "-star")
        new_stars.append(star)
    return new_stars
```

**解説**

```
    new_stars = []
```

>[!NOTE]
>新しく作成した星を入れる為のリスト<br>

```
    for colour in colours_to_create:
```

>[!NOTE]
>``colours_to_create``のアイテムを取り出しながらループをっ実行します。<br>

```
        star = Actor(colour + "-star")
```

>[!NOTE]
>2つの文字列をつないています。<br>

```
    return new_stars
```
>[!NOTE]
>更新した``new_stars``リストを返しています。<br>

**15. 試してみる**<br>
ソースコードにバグが入りこんでいないかチェック。<br>
ソースコードのファイルをSAVEして、コマンドラインから実行します。<br>

**16. 星を置く**<br>
``layout_stars()``関数を使ってすべての星を画面に配置します。<br>
まず星と星の間の、何もない隙間を何か所作るか決めなければならい。<br>
隙間の幅は、画面の幅を隙間の合計数で割って計算します。<br>
そして赤い星がいつも決まった位置に置かないよう、星のリストを**shuffle(シャッフル)** しておかないといけない。<br>
``def layout_stars(stars_to_layout)``のあとの**pass**を書き換えていきます。<br>

**ソースコード**
```
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
```

**解説**

```
    number_of_gaps = len(stars_to_layout) + 1
```

>[!NOTE]
>画面上に作る隙間の数を計算しています。<br>

```
    gap_size = WIDTH / number_of_gaps
```

>[!NOTE]
>画面の幅を隙間の数で割っています。<br>

```
    random.shuffle(stars_to_layout)
```

>[!NOTE]
>星のリストをシャッフルして、水平(左右)方向の位置（X座標）がランダムになるように設定しています。<br>

```
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
```

>[!NOTE]
>このブロックは現在処理している星を、画面左端から（リスト内での順番+1）＊（隙間の幅）だけ右に離して置いています。<br>
>リスト内の順番は0から始まります。<br>

**17. テストのし直し**<br>
再度プログラムを実行して画面がどのように変わるか確認します。

<img width="802" height="632" alt="タイトルなし" src="https://github.com/user-attachments/assets/4262aa63-d4c3-4ca6-b4fe-46ba51e53da5" />

**18. 星を動かす**<br>
星を動かしていきます。<br>
ゲームらしくしていきため、それぞれの星を画面の下に向けて動かしていきます。<br>
星を動かすときに1つの画面(アニメーションでは「フレーム」と呼びます)をどれだけの時間を表示しておくかを決めておき、レベルが上がったら星のスピードを上げられるようにしておきます。<br>
フレームの表示時間が短いと早く動いているように見えます。<br>
また「アンカー」は星の底に設定しておき、画面下に星が着いたとたん動くのをやめるようにしておきます。<br>
ソースコード``def animate_stars(stars_to_animate)``のあとの**pass**を書き換えていきます。<br>

> [!TIP]
> **アンカー**<br>
> PCのグラフィックでは図形のある1点を「アンカー」と呼んでいます。<br>
> 画面上での図形の位置を決めるときに使う特別な点です。<br>
> 例えば四角形のアンカー左下の頂点だとしておきます。<br>
> この四角形を座標(0，0)になるように置くということです。<br>
![名称未設定 1](https://github.com/user-attachments/assets/d6f84550-97f9-41a2-8fa9-e4cd2ab4b125)

**ソースコード**
```
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)
```

**解説**

```
    duration = START_SPEED - current_level
```
>[!NOTE]
>最初にセットされているスピードから現在のレベルを引いた値を、フレームが表示される時間にしています。<br>
>値が小さければ星は早く動く<br>

```
    star.anchor = ("center", "bottom")
```
>[!NOTE]
>星のアンカーを画像の一番下にしています。<br>

```
    animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
```
>[!NOTE]
>アニメーションの処理が終わったときに``handle_game_over()``関数を呼び出すよう指示ｓています。

**19. ゲームオーバー**<br>
次にしなければならないのは、``handle_game_over()``関数の定義です。<br>
この関数はプレイヤーがミスをしたときにゲームを終わらせるための設定です。<br>

**ソースコード**
```
def handle_game_over():
    global game_over
    game_over = True
```

> [!TIP]
> **animate()関数**<br>
> **Pygame Zero**のライブラリにに入っているanimate()関数はとても便利で。<br>
> この関数を使えば、画面上でアクターを簡単に動かせます。<br>
> 使うにはいくつかの引数が必要になります。<br>
>
> - 最初の引数で動かしたいアクターを必ず指定する。
> - **tween**= オプションの引数で、アニメーションのふるまいを変化させるのに使えます。
> - **duration**= アニメーションのフレームを何ミリ秒表示するかを指定します。
> - **no_finished**= オプションの引数で、アニメーションの処理が終わったあとに呼び出したい関数を指定しておける。<br>
>   このゲームでは星が画面下に着いたとき、ゲームを終わらせる関数を呼び出しています。
> - 最後の部分には、アクターをどのような感じで動かすかを決める引数をいくつか書き込む。<br>
>   この部分には2つ以上の引数をセットしてもいいです。
>
> 例えば座標(0, 0)にいるアクターを(100, 0)まで動かすということは、アクターを100ピクセル右に動かすことになる。
> フレームは**duration**で指定した時間だけつぎつぎに表示されていく。
> 同じ枚数のフレームを長く表示(**duration**の値が大きい)すれば、アクターはゆっくり動きます。
![名称未設定 1](https://github.com/user-attachments/assets/7ca9ee8c-87eb-4385-a827-70eaa2d64c45)

