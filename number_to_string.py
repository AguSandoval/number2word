units = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

decimals = {0: '', 1: 'teen', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
            9: 'ninety'}

diff_decimals = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen',
                 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}

bigger = {0: '', 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}

hundred = {0: '', 1: 'hundred'}

numbers = {1: units, 2: decimals, 3: hundred, 9: diff_decimals}


def check_triples(number):
    number_str = str(number)
    length = len(number_str)
    while length % 3 != 0:
        number_str = '0' + number_str
        length = len(number_str)
    return number_str


def split_number(number):
    chunks = [number[i:i + 3] for i in range(0, len(number), 3)]
    return chunks


def name_number(number_str):
    number_len = len(number_str)
    number_literal = ''
    for i in range(number_len):
        position = number_len - i
        if position % 3 == 0:
            if number_str[i] == '0':
                # number_literal += numbers.get(3).get(0) + ' '
                pass
            else:
                number_literal += numbers.get(1).get(int(number_str[i])) + ' ' + numbers.get(3).get(1) + ' '
        elif position % 2 == 0:
            if number_str[i] == '1' and number_str[i + 1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                number_literal += numbers.get(9).get(int(number_str[i + 1]))
                break
            elif number_str[i + 1] == '0':
                number_literal += numbers.get(2).get(int(number_str[i]))
            elif number_str[i] == '0':
                number_literal += ''
            else:
                number_literal += numbers.get(2).get(int(number_str[i])) + '-'
        else:
            number_literal += numbers.get(1).get(int(number_str[i]))
    return number_literal


number = 0
while True:
    number = int(input('Enter a number: '))
    number_str = check_triples(number)
    array_numbers = split_number(number_str)
    final_number = ''
    len_array = len(array_numbers) - 1
    for i in array_numbers:
        try:
            if int(i) != 0:
                final_number += name_number(i) + ' ' + bigger.get(len_array) + ' '
            else:
                final_number += bigger.get(0)
            len_array -= 1
        except:
            final_number = 'Number too big'
    print(final_number)
