# 練習
# 関数の練習
def is_leap_year(year):  
  if year%400 == 0:
    return True
  elif year%100 == 0:
    return False
  elif year%4 == 0:
    return True
  else:
    return False

year = (2020,2024,2025)
result = [is_leap_year(y) for y in year]
print(result)

# クラスの練習
class Student:
  def __init__(self, name, math, japanese,
               english, science, society):
    self.name = name
    self.math = math
    self.japanese = japanese
    self.english = english
    self.science = science
    self.society = society

  def average_score(self):
    avg = (self.math + self.japanese + self.english +
           self.science + self.society) / 5
    return avg

student_1 = Student("山田太郎", 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(f"{student_1.name}さんの平均点は{s1_avg}点です")

# Q3-1
# アパレルネット通販アプリの商品クラス
class Item:
  def __init__(self, id, name, price, purchase_price):
    self.id = id
    self.name = name
    self.price = price
    self.purchase_price = purchase_price

  def cost_rate(self):
    return (self.purchase_price / self.price) * 100

item_1 = Item("A001", "Tシャツ", 5000, 2250)
print(f"{item_1.name}の原価率は{item_1.cost_rate()}%です")

item_1.price = 6000
print(f"{item_1.name}の原価率は{item_1.cost_rate()}%です")