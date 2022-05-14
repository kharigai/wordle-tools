# wordle-tools

## 概要

wordle サポートツール


## インストール

```
# 単語リストをダウンロード
$ wget -O word.list https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt

# 権限付与
$ chmod +x five-letter-word.py
```


## 使い方

```
# 5文字の英単語を出力
$ ./five-letter-word.py
about
other
..

# ランダムな1文字を出力
$ ./five-letter-word.py -r
could
```


## 資料

- [first20hours/google-10000-english](https://github.com/first20hours/google-10000-english)
  - 英単語リスト
