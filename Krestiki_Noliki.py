class game:
    table = [[' ', '1', ' ', '2', ' ', '3'],['A',' ','|',' ','|',' '],[' ','_','_','_','_','_'],['B',' ','|',' ','|',' '],[' ','_','_','_','_','_'],
             ['C',' ','|',' ','|',' '],[' ','_','_','_','_','_']]

    dict_table = {'A':1, 'B':3, 'C': 5, '1':1, '2':3, '3':5}

    def input_x(dict_table, table):
        x = input('Turn X. Input coordinates: ').upper()
        x1 = dict_table[x[0]]
        x2 = dict_table[x[1]]
        table[x1][x2] = 'X'
        return table

    def input_o(dict_table, table):
        o = input('Turn O. Input coordinates: ').upper()
        o1 = dict_table[o[0]]
        o2 = dict_table[o[1]]
        table[o1][o2] = 'O'
        return table

    def check(table):
        flag = True
        for i in range(len(table)):
            print(*table[i])
        for i in range(1, len(table), 2):
            if table[i][1] == table[i][3] == table[i][5] != ' ':
                flag = False
                print(f'Winner: {table[i][1]}')
                break
            elif table[1][i] == table[3][i] == table[5][i] != ' ':
                flag = False
                print(f'Winner: {table[1][i]}')
                break
            elif table[1][1] == table[3][3] == table[5][5] != ' ':
                flag = False
                print(f'Winner: {table[1][1]}')
                break
            elif table[1][5] == table[3][3] == table[5][1] != ' ':
                flag = False
                print(f'Winner: {table[1][5]}')
                break
            elif ' ' not in table[1]:
                if ' ' not in table[3]:
                    if ' ' not in table[5]:
                        print('NICHYA')
                        break
        return flag

    for i in range(len(table)):
        print(*table[i])

    flag = True
    while flag:
        input_x(dict_table, table)
        flag = check(table)
        if flag == False:
            break
        input_o(dict_table, table)
        flag = check(table)
        if flag == False:
            break