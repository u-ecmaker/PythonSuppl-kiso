# https://zenn.dev/tko_kasai/articles/2495d5b28766e5
# 問題11:アナグラム判定
# 問題: 2つの文字列がアナグラム（文字の並び替えで一致）かどうかを判定する関数を作成してください。

"""
🧩 問題: アナグラムの検出
■ 問題文
2つの文字列 s1 と s2 が与えられます。これらの文字列がアナグラムであるかを判定する関数を作成してください。

アナグラムとは、文字の順序は異なるが、同じ文字とその回数で構成されている文字列のことを指します。

■ 関数の定義
```
  def solution(s1: str, s2: str) -> bool:
```

■ 入力
s1: 英小文字のみからなる文字列（長さは1以上100,000以下）
s2: 英小文字のみからなる文字列（長さは1以上100,000以下）

■ 出力
True: s1 と s2 がアナグラムである場合
False: それ以外の場合

■ 例
solution("listen", "silent")  # 出力: True
solution("triangle", "integral")  # 出力: True
solution("apple", "pale")  # 出力: False

■ 制約
入力文字列の長さは最大で100,000文字です。
効率的なアルゴリズム（O(N) または O(N log N)）を実装してください。
"""

# 💡 解法のヒント
# Pythonの collections.Counter クラスを使用すると、文字列中の各文字の出現回数を簡単にカウントできます。
# 2つの文字列の Counter オブジェクトが等しい場合、それらの文字列はアナグラムであると判断できます。

from collections import Counter

def solution(s1: str, s2: str) -> bool:
  # Counter(s1) = {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
  # Counter(s2) = {'s':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1}

  return Counter(s1) == Counter(s2)
  