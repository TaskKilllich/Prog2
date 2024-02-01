import itertools

randomNumber = [
  [3, 4, 5, 6, 7, 8, 9, 1, 2]
]

def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return itertools.zip_longest(*args, fillvalue=fillvalue)

for matrix in randomNumber:
  for chunk in grouper(matrix, 3):
    print(" ".join(map(str, chunk)))
  print()

print("El valor mas alto es: %s"% max(randomNumber[0]))
print("El valor mas bajo es: %s"% min(randomNumber[0]))