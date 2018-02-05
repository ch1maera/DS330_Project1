from itertools import chain, combinations


def main():

    product_dict = {}

    with open('intersorted.txt', 'r') as e:
        current_line = e.readline()

        current_key = get_key(current_line)

        while current_line:
            #Reads in a line and parses it for relevant information
            line_key = get_key(current_line)

            line_type = get_line_type(current_line)

            current_product, current_match = parse_line(current_line, line_type)

            # If the line key is the same as the current key inserts product into our dictionary
            if line_key == current_key:
                product_dict = insert_into_product_dict(current_product, current_match, product_dict)

            # If the line key is different than the current key, we need to dump all our recommendations before moving forward
            elif line_key != current_key:
                list_of_products = get_list_of_products(product_dict, current_key)

                #Get list of all products in our dictionary, and creates all possible combinations
                for subset in all_subsets(list_of_products):

                    #If the current subset of products starts with our current key, builds the cart and recommendations
                    if subset[0] == current_key:

                        current_cart = build_cart_products(subset)

                        products_to_recommend = recommend_products(current_cart, current_key, product_dict)

                        print(format_output(current_cart, products_to_recommend))

                #Clears our product dictionary and sets our current key to the line key
                product_dict = {}
                product_dict = insert_into_product_dict(current_product, current_match, product_dict)
                current_key = line_key

            current_line = e.readline()


def all_subsets(ss):
    #Returns all possible combinations of products that could be found in someone's cart
    return chain(*map(lambda x: combinations(ss, x), range(2, len(ss)+1)))


def get_key(line):
    #Returns the key of the current line
    key = int(line.split(' ')[0].strip())
    return key


def get_line_type(line):
    #Returns the current line type
    if '!' in line:
        return 'non-match'
    if line.count(':') == 2:
        return 'other-match'
    if len(line.split(':')) == 2 and '!' not in line:
        return 'match'


def parse_line(line, line_type):
    #Reads in a line and line type and returns the product and recommended product match
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
    #Inserts the product and match into a dictionary
    if product in product_dict:
        matched_products = product_dict[product]
        matched_products.append(match)
        product_dict[product] = matched_products
    else:
        product_dict[product] = [match]
    return product_dict


def get_list_of_products(product_dict, current_key):
    #Returns list of products to build our combinations upon
    list_of_keys = list(product_dict.keys())
    list_of_keys.sort()
    for product in list_of_keys:
        if current_key > product:
            list_of_keys.remove(product)
    return list_of_keys


def build_cart_products(subset_of_products):
    #Returns a list of products found in a cart
    cart = []
    for product in subset_of_products:
        cart.append(product)
    return cart.sort()


def recommend_products(items_in_cart, current_key, product_dict):
    #returns a list of recommended products
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
    return products_to_recommend.sort()


def append_item(matching_product, items_in_cart, list_of_items_to_append):
    #Returns a modified list of recommended products if that product isn't in the cart or the list already
    if matching_product not in list_of_items_to_append:
        if matching_product not in items_in_cart:
            return list_of_items_to_append.append(matching_product)


def format_output(cart, recommended_products):
    #Formats the printed line as specified by the assignment
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
