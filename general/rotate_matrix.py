# v1

def rotate_matrix(m: list[list[int]]) -> None:
    transpose_cols(m)
    reverse_rows(m)

def transpose_cols(m: list[list[int]]) -> None:
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]

def reverse_rows(m: list[list[int]]) -> None:
    for i in range(len(m)):
        m[i].reverse()


# v2

def rotate_matrix(m: list[list[int]]) -> None:
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    for i in range(len(m)):
        m[i].reverse() 