import sys

def main(argv):

    with open('mapper3test.txt','r') as e:
        line = e.readline()

        while line:

            base_product = line.split(' ')[0]

            other_products = line.split(':')[-1]

            matches = other_products.split('!')[0].strip()

            non_matches = other_products.split('!')[-1].strip()

            if matches != '':
                print_matches(base_product, matches)

            if non_matches != '':
                print_non_matches(base_product, matches, non_matches)

            line = e.readline()

def print_matches(base_product,matches):
        matches = matches.split(' ')
        for match in matches:
            print(base_product + ' : ' + match)
            for other_match in matches:
                if match != other_match:
                    print(match + ' : ' + base_product + ' : ' + other_match)


def print_non_matches(base_product,matches,non_matches):
    non_matches = non_matches.split(' ')
    if matches != '':
        matches = matches.split(' ')

        for non_match in non_matches:
            for other_match in matches:
                print(non_match + ' ! ' + base_product + ' : ' + other_match)
    else:
        pass


if __name__ == '__main__':
    main(sys.argv)
