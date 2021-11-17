def is_unique(input_str):
  d = dict()

  for i in input_str:
      if i in d:
          return False
      else:
          d[i] = 1
  return True


str1 = "nonunique"
str2 = "abcdef"

print(is_unique(str1))
print(is_unique(str2))
