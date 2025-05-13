"""
問題: 文字の頻度ソート
問題文
英大文字・英小文字のみからなる文字列 S が与えられます。
各文字の出現回数を数え、出現回数が多い文字から順に並べ替えた新しい文字列を返してください。
同じ文字はまとめて連続して並べます。
出現回数が同じ文字同士は、任意の順序（元の順序でも、辞書順でも可）で構いません。

■ 関数の定義
  ```
  def solution(S: str) -> str:
  ```

■ 引数
S: 長さ N の文字列（1 ≤ N ≤ 100,000）、英大文字・英小文字のみ

■ 戻り値
各文字を出現頻度の降順で並べ替えた文字列

■ 例
  ```
  # 例1
  S = "tree"
  # 'e' が2回、't','r' が1回ずつ → "eetr" や "eert" がOK
  print(solution("tree"))  # => "eetr" or "eert"

  # 例2
  S = "cccaaa"
  # 'c','a' がそれぞれ3回 → "aaaccc" も "cccaaa" もOK
  print(solution("cccaaa"))  # => "aaaccc" or "cccaaa"

  # 例3
  S = "Aabb"
  # 'b'が2回、'A','a' が1回ずつ → "bbAa" などがOK （大文字小文字を区別）
  print(solution("Aabb"))  # => "bbAa" or "bbaA"
  ```

■ 制約
N は最大100,000

実行時間は O(N log N) 以下を想定（sorted+キー指定、またはヒープ/バケットソートなど）
"""

from collections import Counter

def solution(S: str) -> str:
# ✅ ステップ0: 前提知識「cnt.get(char)」とは？
# dict.get(key) は指定したキーが存在すればその値を返し、なければ None または指定したデフォルト値を返します。
  """ 
  cnt = {'a': 3, 'b': 2}
  cnt.get('a')  # => 3
  cnt.get('c', 0)  # => 0（存在しないキーに対してデフォルト値を返す）
  """
  cnt = {}

  # 出現回数を手動でカウント
  # 例: S = "tree" の場合、s は順に 't', 'r', 'e', 'e'.
  for s in S:
    # cnt という辞書の中に s（今回の文字）が すでにあればその回数を返す or なければ 0 を返す
    cnt[s] = cnt.get(s, 0) + 1  # ← +1 はcount up.

  # 出現回数の多い順にソート（setで重複排除）
  sorted_chars = sorted(set(S), key=lambda x: -cnt.get(x))

  # 出現回数分繰り返して連結
  result = ''
  for ch in sorted_chars:
      result += ch * cnt.get(ch)  # 例: 'e'*2 = 'ee'
  
  return result
