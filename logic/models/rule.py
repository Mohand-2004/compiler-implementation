class Rule:
  def __init__(self, left, right,) -> None:
    self.left = left
    self.right = right

  @classmethod
  def fromString(cls, string: str):
    string = string.strip()
    string = string.replace(' ', '')
    left, right = string.split('->')
    return Rule(left=left, right=right)
  
  def __str__(self) -> str:
    return f"{self.left} -> {self.right}"