from itertools import chain, combinations

def all_subsets(ss):
  return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

stuff = '123456'

for subset in all_subsets(stuff):
    if len(subset) > 1 and subset[0] == '1':
        output = ''
        for i in subset:
            output += str(i + ' ')
        output += ': '
        print(output)
