def transform_to_matrix(matrix_string: str) -> list:
    # use \n as separator for the split() method
    # but ignore the first one to avoid empty list
    # since there is a \n as a first element in the string
    return [list(string) for string in matrix_string[1:].split('\n')]

def select_chars(matrix: list) -> str:
    tmp_message = str()
    for j in range(3):
        for i in range(len(matrix)):
            if matrix[i][j].isalpha():
                tmp_message += matrix[i][j]
    return tmp_message

def substitute_for_space(matrix:list) -> None:

    for i in range(len(matrix)):
        for j in range(3):
            if not matrix[i][j].isalpha():
                matrix[i][j] = " "

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''         

matrix = transform_to_matrix(MATRIX_STR)
print(matrix)

tmp_message = select_chars(matrix)
print(tmp_message)




