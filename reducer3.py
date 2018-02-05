from itertools import chain, combinations


def main():

    product_dict = {}

    with open('intersorted.txt', 'r') as e:
        current_line = e.readline()

        current_key = get_key(current_line)

        while current_line:
            line_key = get_key(current_line)

            line_type = get_line_type(current_line)

            current_product, current_match = parse_line(current_line, line_type)

            if line_key == current_key:
                product_dict = insert_into_product_dict(current_product, current_match, product_dict)

            elif line_key != current_key:
                list_of_products = get_list_of_products(product_dict, current_key)

                for subset in all_subsets(list_of_products):

                    if subset[0] == current_key:

                        current_cart = build_cart_products(subset)

                        products_to_recommend = recommend_products(current_cart, current_key, product_dict)

                        print(format_output(current_cart, products_to_recommend))

                product_dict = insert_into_product_dict(current_product, current_match, product_dict)
                current_key = line_key

            current_line = e.readline()


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1)))


def get_key(line):
    key = int(line.split(' ')[0].strip())
    return key


def get_line_type(line):
    if '!' in line:
        return 'non-match'
    if line.count(':') == 2:
        return 'other-match'
    if len(line.split(':')) == 2 and '!' not in line:
        return 'match'


def parse_line(line, line_type):
    if line_type == 'match':
        product = int(line.split(':')[0].strip())
        match = int(line.split(':')[-1].strip())
    if line_type == 'other-match':
        product = int(line.split(':')[1].strip())
        match = int(line.split(':')[-1].strip())
    if line_type == 'non-match':
        product = int(line.split('!')[-1].split(':')[0].strip())
        match = int(line.split('!')[-1].split(':')[-1].strip())
    return product, match


def insert_into_product_dict(product, match, product_dict):
    if product in product_dict:
        matched_products = product_dict[product]
        matched_products.append(match)
        product_dict[product] = matched_products
    else:
        product_dict[product] = [match]
    return product_dict


def get_list_of_products(product_dict, current_key):
    list_of_keys = list(product_dict.keys())
    list_of_keys.sort()
    for product in list_of_keys:
        if current_key > product:
            list_of_keys.remove(product)
    return list_of_keys


def build_cart_products(subset_of_products):
    cart = []
    for product in subset_of_products:
        cart.append(product)
    return cart


def recommend_products(items_in_cart, current_key, product_dict):
    products_to_recommend = []
    for product in product_dict[current_key]:
        should_append = False
        for other_product in items_in_cart:
            if product in product_dict[other_product]:
                should_append = True
            else:
                should_append = False
                break
        if should_append is True:
            append_item(product, items_in_cart, products_to_recommend)
    return products_to_recommend


def append_item(matching_product, items_in_cart, list_of_items_to_append):
    if matching_product not in list_of_items_to_append:
        if matching_product not in items_in_cart:
            return list_of_items_to_append.append(matching_product)


def format_output(cart, recommended_products):
    output = ''
    for item in cart:
        output += str(item) + ' '
    output += ': '
    recommended_products.sort()
    for product in recommended_products:
        output += str(product) + ' '
    return output


if __name__ == '__main__':
    main()
