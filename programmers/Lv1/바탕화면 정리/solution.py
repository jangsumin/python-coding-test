def solution(wallpaper):
    answer = []
    rows, columns = list(), list()
    for row in range(len(wallpaper)):
        for column in range(len(wallpaper[row])):
            if wallpaper[row][column] == '#':
                rows.append(row)
                columns.append(column)
    answer.append(min(rows))
    answer.append(min(columns))
    answer.append(max(rows) + 1)
    answer.append(max(columns) + 1)
    return answer