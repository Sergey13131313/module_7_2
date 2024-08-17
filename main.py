def custom_write(file_name, strings):
    with open(file_name, 'w') as f:
        for x in strings:
            f.write(x + '\n')
    with open(file_name, 'r') as f:

        x = None
        dict = {}
        counter = 0

        while True:
            x = f.readline()
            if x == '':
                return dict
            else:
                dict[(counter, f.tell())] = x
                counter += 1


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for iteam in result.items():
        print(iteam)
