# Q3
# 【模擬問題】Most Frequent Within Time Limit

"""
■ 問題文（顧客アクティビティ分析）
あるサービスでは、ユーザーが一定の時間範囲内で何回アクションを起こしたかを記録しています。
各アクションログは、ユーザーIDとアクション発生時刻（整数）で構成されています。
あなたは「指定された時間範囲（start_time〜end_time）内に、最も多くアクションを起こしたユーザーのID」を特定する必要があります。

■ 要件
同率で最多だった場合はIDの小さい方を返してください
指定時間範囲に該当するアクションが1件もなければ -1 を返してください

■ 入力
def solution(logs: list[tuple[int, int]], start_time: int, end_time: int) -> int:
    ```
    logs: List of tuples (user_id, time)
    start_time, end_time: 範囲（両端含む）
    return: 最も多くアクションしたユーザーのID（同率は最小ID優先、なければ -1）
    ```

■ 入力例
logs = [
    (1, 10),  # user 1 at time 10
    (2, 11),
    (1, 15),
    (3, 12),
    (1, 19),
    (2, 18),
    (3, 25)
]
start_time = 10
end_time = 20

■ 出力
1

■ 解説
時間10〜20の範囲で抽出すると：
user 1 → 10, 15, 19 → 3回
user 2 → 11, 18 → 2回
user 3 → 12 → 1回
最多は user 1（3回）

■ 制約
logs の長さは最大10^5
user_id と time は 1〜10^9 の整数
O(N) or O(N log N) で解けること
"""

def solution(logs: list[tuple[int, int]], start_time: int, end_time: int) -> int:
  """
  logs: List of tuples (user_id, time)
  start_time, end_time: 範囲（両端含む）
  return: 最も多くアクションしたユーザーのID（同率は最小ID優先、なければ -1）
  """
  print(logs, start_time, end_time)

  # 変数定義
  count_map = {} # アクション数のカウント

  # 時間内かを判定
  for user_id, time in logs:
    print(user_id, time)

    if start_time <= time <= end_time:
      if user_id not in count_map:
        count_map[user_id] = 1
      else:
        count_map[user_id] += 1
    
    print(count_map)

  # 一致ログなし
  if not count_map:
    return -1
  
  max_user = max(count_map.items(), key=lambda x: (x[1], -x[0]))[0]
  

