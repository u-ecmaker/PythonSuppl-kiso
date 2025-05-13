# Q2
# Max Active Interval

"""
■ 問題文（SaaSログ分析ユースケース）
あなたはあるBtoB SaaSサービスの利用ログを分析しています。
ログは「あるユーザーが何時から何時までサービスを利用していたか」を示しています。
以下の形式のリストが与えられます：

■ 入力例
logs = [
    [1, 5],  # ユーザーAは時刻1〜5に利用
    [3, 6],  # ユーザーBは時刻3〜6に利用
    [4, 10]  # ユーザーCは時刻4〜10に利用
]
このとき、**サービス利用者が最も多かった1時間（連続する1単位区間）**に、
同時に何人利用していたかを求めてください。

■ 要件（仕様）
時刻は整数（0〜10^6）
各ログは [start, end] の形式で、start <= end
区間 [start, end] は、start時間からend時間まで使っていたとみなします（両端含む）

■ 入力
  ```
  def solution(logs: list[list[int]]) -> int:
      logs: List of [start, end] intervals
      return: 最大同時利用者数（整数）
  ```

■ 入力例
  ```
  logs = [
      [1, 5],
      [3, 6],
      [4, 10]
  ]
  ```

■ 出力
  3

■ 解説
時刻4〜5の間に3人利用している（1〜5, 3〜6, 4〜10 の全員が重なる）
これが最大なので、出力は 3

■ 制約
logs の長さは 1〜10^5
実行時間は O(N log N) が理想
同時最大数を求めるだけでよく、どの時刻かは不要
"""

def solution(logs: list[list[int]]) -> int:
  """
  logs: List of [start, end] intervals
  return: 最大同時利用者数（整数）
  """
  start = 0
  end = 0

  # 開始時刻でソート
  logs.sort(key=lambda x: x[0]) 

  max_users = 0 # 最大同時利用者数

  # スライディングウィンドウ
  # [start, start+1]で探索していく
  for i in range(len(logs)):
    window_start = logs[i][0]
    window_end = window_start + 1 

    # 利用者数カウント
    count = 0
    for j in range(i, len(logs)):
      start, end = logs[j]
      if start <= window_end and end >= window_start:
        count += 1

    max_users = max(max_users, count)

  return max_users
