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