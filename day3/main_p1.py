
if __name__ == '__main__':
    ans = 0
    f = open('data.in', 'r')

    data = f.read()
    #print(data)

    for i in range(0, len(data) - 2):
        t = data[i:i+3]
        if t == 'mul':
            j = i+3
            after = ''
            while j < len(data) and data[j] != ')':
                if not (data[j].isdigit() or data[j] == '(' or data[j] == ','):
                    after = ''
                    break

                after += data[j]
                j += 1

            if after == '' or after.count(',') != 1 or after.count('(') != 1:
                continue

            comma_pos = after.find(',')
            x = int(after[1:comma_pos])
            y = int(after[comma_pos+1:])
            
            ans += x * y
            
    print(ans)