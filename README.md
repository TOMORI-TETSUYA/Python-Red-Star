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
HEIGHT = 800
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
