grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(6): # https://ru.stackoverflow.com/questions/1185961/%d0%a1%d0%b5%d1%82%d0%ba%d0%b0-%d1%81%d0%b8%d0%bc%d0%b2%d0%be%d0%bb%d0%be%d0%b2-%d0%b8%d0%b7-%d1%81%d0%bf%d0%b8%d1%81%d0%ba%d0%b0-%d1%81%d0%bf%d0%b8%d1%81%d0%ba%d0%be%d0%b2-%d0%b2-python-%d0%b7%d0%b0%d0%b4%d0%b0%d1%87%d0%b0-%d1%81%d0%bf%d0%b8%d1%81%d0%ba%d0%be%d0%b2-%d0%b8%d0%b7-%d0%ba%d0%bd%d0%b8%d0%b3%d0%b8-al-sweigart/1185974#1185974
    for j in range(9):
        print(grid[j][i], end="")
    print()