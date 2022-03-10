import collections
import re


def word_cal():
    with open('C:/Users/Dero/Desktop/record.txt', 'r') as fp:
        content = re.split('\n', fp.read())
    b = collections.Counter(content)
    # flag = 1
    with open('C:/Users/Dero/Desktop/result_han.txt', 'w') as result_file:
        for key, value in b.items():
            result_file.write( key + ':' + str(value) + '\n')
            # flag = flag + 1

def main():
    word_cal()


if __name__ == '__main__':
    main()
