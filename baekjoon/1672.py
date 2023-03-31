# DNA 해독

n = int(input())
dna = list(input())

dic = {
  'AA': 'A',
  'AG': 'C',
  'AC': 'A',
  'AT': 'G',
  'GA': 'C',
  'GG': 'G',
  'GC': 'T',
  'GT': 'A',
  'CA': 'A',
  'CG': 'T',
  'CC': 'C',
  'CT': 'G',
  'TA': 'G',
  'TG': 'A',
  'TC': 'G',
  'TT': 'T'
}

while True:
  if len(dna) == 1:
    break
  s = dna[-2] + dna[-1]
  dna.pop()
  dna.pop()
  dna.append(dic[s])

print(''.join(dna))