import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)

def cyclic123_array(n): 
    """2. Генерирует numpy массив длины 3n, заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n+1, 2)

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    arr = np.zeros((n, n))
    arr[[0, -1], :] = 1  # Primera y última fila
    arr[:, [0, -1]] = 1  # Primera y última columna
    return arr

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    board = np.zeros((n, n))
    board[::2, ::2] = 1  # Casillas pares en filas pares
    board[1::2, 1::2] = 1  # Casillas impares en filas impares
    return board

def matrix_with_sum_index(n):
    """6. Создаёт n × n матрицу с (i,j)-элементами равными i+j."""
    rows = np.arange(n).reshape(-1, 1)
    cols = np.arange(n).reshape(1, -1)
    return rows + cols

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите cos(x) и sin(x) на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    x = np.arange(a, b, dx)
    cos_x = np.cos(x)
    sin_x = np.sin(x)
    return np.vstack([cos_x, sin_x])

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    mean = np.mean(A)
    row_sums = np.sum(A, axis=1)
    column_sums = np.sum(A, axis=0)
    return mean, column_sums, row_sums

def sort_array_by_column(A, j):
    """9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[np.argsort(A[:, j])]

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:  
    method == 'rectangular' - методом прямоугольника   
    method == 'trapezoidal' - методом трапеций   
    method == 'simpson' - методом Симпсона  
    """
    n_intervals = int((b - a) / dx)
    x = np.linspace(a, b, n_intervals + 1)
    
    if method == 'rectangular':
        x_mid = x[:-1]  # Левая точка прямоугольника
        return np.sum(f(x_mid)) * dx

    elif method == 'trapezoidal':
        y = f(x)
        return (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) * dx / 2

    elif method == 'simpson':
        if n_intervals % 2 == 1:  # нужно чётное число отрезков → нечётное число точек
            x = np.linspace(a, b, n_intervals + 2)
            dx = (b - a) / (n_intervals + 1)
        
        y = f(x)
        return dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

    else:
        raise ValueError("Unknown method. Use 'rectangular', 'trapezoidal' or 'simpson'.")

