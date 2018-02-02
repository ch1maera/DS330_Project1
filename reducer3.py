from itertools import chain, combinations

# def all_subsets(ss):
#   return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))
#
# stuff = '123456'
#
# for subset in all_subsets(stuff):
#     if len(subset) > 1 and subset[0] == '1':
#         output = ''
#         for i in subset:
#             output += str(i + ' ')
#         output += ': '
#         print(output)

product_dict = {}


with open('reducer3test.txt','r') as e:
    line = e.readline()
    current_key = line.split(':')[0].strip()

    while line:
        if len(line.split(':')) == 2 and '!' not in line:
            key = line.split(':')[0].strip()
            product = line.split(':')[0].strip()
            match = line.split(':')[-1].strip()

        if line.count(':') == 2:
            key = line.split(':')[0].strip()
            product = line.split(':')[1].strip()
            match = line.split(':')[-1].strip()

        if '!' in line:
            key = line.split('!')[0].strip()
            product = line.split('!')[-1].split(':')[0].strip()
            match = line.split('!')[-1].split(':')[-1].strip()

        if current_key != key:
            print(product_dict)
            product_dict = {}
            current_key = key

        if product in product_dict:
            matched = product_dict[product]
            matched.append(match)
            product_dict[product] = matched
        else:
            product_dict[product] = list(match)

        line = e.readline()


    print(product_dict)
