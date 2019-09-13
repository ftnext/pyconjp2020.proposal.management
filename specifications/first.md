# 最小構成 (PyCon JP 2019 Sprint用)

タイムテーブルを自由に作れるサイトをDjangoで作る

※これはnikkieの案であり、開発の方向性を示すために用意しています。より良くする案があったら、そちらを提案していただいてかまいません

## タイムテーブル作成機能

- 採択済みのプロポーザルが与えられている
- コンテンツチームメンバーは、タイムテーブルの枠を作ることができる（[例：2019](https://pycon.jp/2019/schedule)）
    - 行＝時間帯を決められる（例：11:25〜12:10）
    - 列＝部屋の種類を決められる（例：小展示ホール）
- コンテンツチームメンバーは、採択済みのプロポーザルを並べたタイムテーブルを作ることができる
    - タイムテーブルの各枠をプルダウンから選べるフォームを想定
- 後で付ける要件
    - 同じ時間帯でタグが重複しないようにプルダウンの選択肢を絞り込む
    - 英語トークが各時間帯に1件以上あるようにバリデーション

実装後、2019の採択済みトークを取り込み、タイムテーブルが自由に作れることを期待している

### ほしい画面

- タイムテーブルの大枠を作る画面
- タイムテーブルの1つ1つを埋める画面
    - タイムテーブルのマスごとにプルダウンから選ぶフォーム
    - プルダウンには、発表言語とタグとタイトルと発表者名を表示したい
    - あると嬉しい：トークのタグにより候補が減る機能（同じ時間帯でタグを重複させない）
    - オプション：（可能ならワーニング）「この時間帯には英語がありません」

## 設計

- TimeTable
- TimeTableRow
- TimeTableColumn
- TimeTableItem
- Talk

コンテンツチームメンバーは`createsuperuser`で作る想定  
スピーカーに該当するユーザーは後回しとする

## Models

### TimeTable

- id
- title（タイムテーブルのタイトル。例「1日目」）
- is_published（trueのとき、コンテンツチームメンバー以外にも見られる）
- 低優先度：slug（タイムテーブルを公開したときのURLの一部）

### TimeTableRow

- id
- table_id（1つのTimeTableはNのTimeTableRowをもつ）
- start_at（開始時間）
- duration（セッションの時間。start_at+duration分の時間枠とする）

### TimeTableColumn

- id
- table_id（1つのTimeTableはNのTimeTableColumnをもつ）
- name（例「小展示ホール」）

### TimeTableItem

あるTimeTableRowとあるTimeTableColumnが与えられたときに、1つのTimeTableItemを設定したい

- id
- row_id
- column_id
- talk_id
- 低優先度：is_empty（トークを当てはめないと決めたときに使う）

### Talk

- id
- speaker_name（MVPができたら、発表者のユーザー情報を別途定義したい）
- title（トークのタイトル）
- status（例「Accepted」）
- tag（PyCon JPで用意したタグ。例「data science and machine learning」）（MVPができたら、別のモデルに切り出したい）
- talk_language（発表言語。日／英）
- slide_language（スライドの言語。日／英／両方）
- target_audience（想定する対象者。beginnerなど）（MVPができたら、別のモデルに切り出したい）
