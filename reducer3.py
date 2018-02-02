from itertools import chain, combinations

def all_subsets(ss):
  return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1)))



product_dict = {}
current_key = None


with open('intersorted.txt','r') as e:
    line = e.readline()

    while line:
        if len(line.split(':')) == 2 and '!' not in line:
            key = line.split(':')[0].strip()
            product = line.split(':')[0].strip()
            match = line.split(':')[-1].strip()

            if not current_key:
                current_key = key

        if line.count(':') == 2:
            key = line.split(':')[0].strip()
            product = line.split(':')[1].strip()
            match = line.split(':')[-1].strip()

            if not current_key:
                current_key = key

        if '!' in line:
            key = line.split('!')[0].strip()
            product = line.split('!')[-1].split(':')[0].strip()
            match = line.split('!')[-1].split(':')[-1].strip()

            if not current_key:
                current_key = key

        if current_key != key:
            output = ''
            list_of_keys = []
            list_of_keys = list(product_dict.keys())
            list_of_keys.sort()
            for prod in list_of_keys:
                if current_key <= prod:
                    output += prod


            for subset in all_subsets(output):
                keys_to_search = []
                items_to_append = []
                if len(subset) > 1 and subset[0] == current_key:
                    output = ''
                    for i in subset:
                        output += str(i + ' ')
                        if i != current_key:
                            keys_to_search.append(i)
                    output += ': '
                    for matching_product in product_dict[current_key]:
                        should_append = False

                        for other_product in keys_to_search:
                            if matching_product not in product_dict[other_product]:
                                break
                            else:
                                should_append = True

                        if should_append == True:
                            if matching_product not in items_to_append:
                                if matching_product not in output:
                                    items_to_append.append(matching_product)

                    for item in items_to_append:
                        output += item + ' '

                    print(output.strip())

            product_dict = {}
            current_key = key

        if product in product_dict:
            matched = product_dict[product]
            matched.append(match)
            product_dict[product] = matched
        else:
            product_dict[product] = list(match)

        line = e.readline()
