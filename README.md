# About

Sutton 本(http://incompleteideas.net/book/the-book.html) の第5章演習問題5.12の実装です。

<details>
<summary>問題文の引用(英語)</summary>
 http://incompleteideas.net/book/RLbook2020.pdf p133 より引用
<pre>
<!-- <code> -->

> Exercise 5.12: Racetrack (programming)

> Consider driving a race car around a turn like those shown in Figure 5.5.
>You want to go as fast as possible, but not so fast as to run o↵ the track. In our simplified racetrack, the car is at one of a discrete set of grid positions, the cells in the diagram. 
>The velocity is also discrete, a number of grid cells moved horizontally and vertically per time step. 
>The actions are increments to the velocity components. Each may be changed by +1, 1, or 0 in each step, for a total of nine (3 x 3) actions. 
>Both velocity components are restricted to be nonnegative and less than 5, and they cannot both be zero except at the starting line.
>Each episode begins in one of the randomly selected start states with both velocity components zero and ends when the car crosses the finish line.
>The rewards are 1 for each step until the car crosses the finish line. 
>If the car hits the track boundary, it is moved back to a random position on the starting line, both velocity components are reduced to zero, and the episode continues. 
>Before updating the car’s location at each time step, check to see if the projected path of the car intersects the track boundary. 
>If it intersects the finish line, the episode ends; if it intersects anywhere else, the car is considered to have hit the track boundary and is sent back to the starting line. 
>To make the task more challenging, with probability 0.1 at each time step the velocity increments are both zero, independently of the intended increments. 
>Apply a Monte Carlo control method to this task to compute the optimal policy from each starting state. 
>Exhibit several trajectories following the optimal policy (but turn the noise o↵ for these trajectories).

<!-- </code> -->
</pre>
</details>

# DEMO

![demo](https://i.imgur.com/CxGc9Fp.gif)
 

# Features
 
 - 学習過程のビジュアル化

 - csv によるコースの作成
 
# Usage
 
 ```
python main.py [start_drawing_episode] [path_to_csv.csv]
 ```

 **上記を実行すると、別ウィンドウが立ち上がるので、Enterを入力すると学習が始まります。**

start_drawing_episode は 描画を開始するエピソードです。指定しない場合は0となり、最初のエピソードからアニメーションが開始されます。

path_to_csv.csv は csv ファイルによって、学習するコースを指定します。

指定されない場合は、デフォルトで作成してあるコースが選ばれます。詳細はmain.pyを確認してください。

## csv でのコースの作成について

![csv](https://i.imgur.com/sBUNXfJ.png)

適当な表計算ソフトで上のようなシートを作りcsvでダウンロードすれば、そのcsvファイルからコースを作成できます。

s: スタートセル

o: コース

x: コース外

e: エンドセル（ゴール）

に対応しています。

# Note

- 移動の補完について

  問題の性質上、エージェントは飛び飛びの場所を動くので、ゴールラインを超えたかどうかやコースアウトの判定には、エージェントの移動がなめらかになるように軌跡を補完してあげる必要があります。

  その際に、先にまっすぐ右に移動してその後まっすぐ下に降りるという方針で二点を繋げています。
  
- 初期ポリシーについて

  初期化時にすべての state に対して、greedy action としてランダムなアクションを設定しています。

  そのために、学習の初期にはいくつかの cell で停滞する現象が見られます。


