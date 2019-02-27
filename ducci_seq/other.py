sequence = [0, 653, 1854, 4063]
seen = []
count = 1
while sum(sequence) != 0 and tuple(sequence) not in seen:
  seen.append(tuple(sequence))
  print(sequence)
  count += 1
  first = sequence[0]
  for n in range(len(sequence)-1):
    sequence[n] = abs(sequence[n+1]- sequence[n])
  sequence[-1] = abs(first -sequence[-1])
print(count)
