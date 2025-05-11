# 【模擬問題】TechPartner Matching
"""
■ 問題文（想定: BtoBマッチングSaaSのユースケース）
ある企業間マッチングプラットフォームでは、技術キーワードによって「発注企業」と「受注企業」がマッチングされます。

各企業は、複数の技術タグ（文字列）を持っており、
ある企業 A に最も多く共通タグを持つ他社 B を、「最もマッチした技術パートナー」として推薦したいと考えています。

■ 要件
与えられた企業群（IDとタグ一覧）から、ある対象企業 target_id に対して、最も共通タグ数が多い他社の企業ID を返してください。
共通タグが同じなら、IDが小さい方を優先とします。target_id 自体は、候補から除外してください。
共通タグを1個以上持つ企業が存在しない場合、-1 を返してください。

■ 入力
  ```
  def solution(companies: list[dict], target_id: int) -> int:
      companies: List of company dicts. Each dict has:
          - 'id': int
          - 'tags': list[str]
      target_id: int

      return: int, id of the best matching partner
  ```

■ 出力
  ```
  2
  ```

■ 解説
target_id=1 のタグは ["AI", "IoT", "DX"]

他の企業と比較: 
ID=2 → ["IoT", "DX", "Cloud"]: 共通2個
ID=3 → ["AI", "DX"]: 共通2個 → IDは2の方が小さい
ID=4 → ["Blockchain", "AI", "IoT"]: 共通2個

よって、最も小さいIDで共通タグ2個を持つID=2を返す。

■ 制約
companies の長さは 2〜10^4
各 tags は最大20個、重複なし
tags はASCII文字列、英大文字小文字混在あり
実行時間: 1秒以内を目安に（set操作を活用せよ）
"""

def solution(companies: list[dict], target_id: int) -> int:
  """""
  companies = [
      {"id": 1, "tags": ["AI", "IoT", "DX"]},
      {"id": 2, "tags": ["IoT", "DX", "Cloud"]},
      {"id": 3, "tags": ["AI", "DX"]},
      {"id": 4, "tags": ["Blockchain", "AI", "IoT"]}
  ]
  target_id = 1

  return: int, id of the best matching partner
  """

  # 対象企業のタグを取得
  target_tags = set()
  for company in companies:
    if company["id"] == target_id:
      target_tags = set(company["tags"])
      break

  # 共通のタグの数を比べる
  max_common_tag = 0
  best_id = float("inf") # 最も小さいIDを探索するため

  for company in companies:
    if company["id"] == target_id:
      continue

    common_tags = target_tags & set(company["tags"]) # 共通タグ、積集合
    common_count = len(common_tags)

    if common_count > max_common_tag:
      max_common_tag = common_count
      best_id = company["id"]
    elif common_count == max_common_tag:
      best_id = min(best_id, company["id"])

  return best_id if max_common_tag > 0 else -1

# test
companies1 = [
    {"id": 1, "tags": ["AI", "IoT", "DX"]},
    {"id": 2, "tags": ["IoT", "DX", "Cloud"]},    # 共通2
    {"id": 3, "tags": ["AI", "DX"]},              # 共通2
    {"id": 4, "tags": ["Blockchain", "AI", "IoT"]}# 共通2
]
print(solution(companies1, 1))

companies2 = [
    {"id": 1, "tags": ["AI", "IoT", "DX"]},
    {"id": 2, "tags": ["IoT", "DX", "Cloud"]},    # 共通2
    {"id": 3, "tags": ["AI", "DX"]},              # 共通2
    {"id": 4, "tags": ["Blockchain", "AI", "IoT"]},# 共通2
    {"id": 5, "tags": ["Blockchain", "AI", "IoT", "DX"]}# 共通3
]
print(solution(companies2, 1))

companies3 = [
    {"id": 1, "tags": ["AI", "IoT", "DX"]},
    {"id": 2, "tags": ["IoT1", "DX1", "Cloud1"]},
    {"id": 4, "tags": ["Blockchain1"]}
]
print(solution(companies3, 1))