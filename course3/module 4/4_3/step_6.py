import sys, json

data = json.loads(sys.stdin.read())

for line in data:
    if type(data[line]) == list:

        s = str(line) + ': '
        ss = ''
        for word in data[line]:
            ss += str(word) + ', '
        ans = s + ss
        print(ans[:-2])

    else:
        print(line, ': ', data[line], sep='')
