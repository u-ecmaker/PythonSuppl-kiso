# 練習
# モジュールの練習
from my_module import Student

student_1 = Student("山田太郎", 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(f"{student_1.name}さんの平均点は{s1_avg}点です")

from datetime import datetime

t = datetime.today()
print(t)

# matpolotlib
import matplotlib.pyplot as plt # type: ignore

label = ["A", "B", "C", "D", "E"]
score = [82, 74, 60, 92, 72]

plt.bar(label, score)
plt.show()


