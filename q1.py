# Q1-1
# 理科は社会より何点高いかを「◯点」という形式で出力
scores = {"数学": 82, "国語": 74, "英語": 60, 
          "理科": 92, "社会": 70}
diff = scores["理科"] - scores["社会"]
print(f"{diff}点")

# Q1-2
# 五教科のテストの点数を辞書で表したとき平均点を〇点と出力
scores_values = list(scores.values())
avg_score = sum(scores_values) / len(scores_values)
print(f"{avg_score}点")

## 別解
avg_score = sum(scores.values()) / len(scores)
print(f"{avg_score}点")
