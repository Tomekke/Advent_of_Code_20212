

def main():
    # inputfile = 'test_import.txt'
    inputfile = 'puzzle_input.txt'
    with open(inputfile, 'r') as fd:
        final_array = []
        tmp_array = []
        for line in fd.readlines():
            if line.strip():
                tmp_array.append(int(line))
            else:
                final_array.append(tmp_array)
                tmp_array = []
        final_array.append(tmp_array)

    for i in range(0, len(final_array)):
        sum = 0
        for number in final_array[i]:
            sum += number
        final_array[i] = sum

    final_result = 0
    for number in sorted(final_array, reverse=True)[:3]:
        final_result += number
    print(final_result)


if __name__ == '__main__':
    main()
