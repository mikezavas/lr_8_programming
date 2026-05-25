def frog_routes(n):
    """
    задача про лягушку:
    количество маршрутов от камня 1 до камня n при шагах на 1, 2 или 3 камня
    :param n: конечный камень
    :return: количество маршрутов
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def min_path_sum(matrix):
    """
    задача про матрицу:
    минимальная сумма пути в матрице m на n (вправо или вниз двигаемся)
    :param matrix: двумерный массив
    :return: минимальная сумма пути
    """
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


def min_coins(coins, s):
    """
    задача про монеты:
    минимальное количество монет для суммы s
    :param coins: список номиналов монет
    :param s: сумма
    :return: min кол-во монет
    """
    if s == 0:
        return 0
    if not coins or s < 0:
        return -1

    dp = [float('inf')] * (s + 1)
    dp[0] = 0

    for i in range(1, s + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[s] if dp[s] != float('inf') else -1


def longest_increasing_subsequence(arr):
    """
    задача про массив:
    длина наибольшей строго возрастающей подпоследовательности
    :param arr: массив целых чисел
    :return: длина
    """
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def knapsack(w, weights, values):
    """
    задача про рюкзак:
    максимальная ценность рюкзака вместимости w, каждый предмет берется один раз
    :param w: вместимость
    :param weights: список весов предметов
    :param values: список ценностей предметов
    :return: max ценность
    """
    n = len(weights)
    dp = [0] * (w + 1)

    for i in range(n):
        weight, value = weights[i], values[i]
        for j in range(w, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[w]


# тесты
if __name__ == "__main__":
    print("задача про лягушку (n=5)")
    print(f"результат: {frog_routes(5)}\n")

    print("задача про матрицы")
    mat = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(f"результат: {min_path_sum(mat)}\n")

    print("задача про монеты (сумма 11, номиналы [1, 2, 5])")
    print(f"результат: {min_coins([1, 2, 5], 11)}\n")

    print("задача про возрастающую подпоследовательность")
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"результат: {longest_increasing_subsequence(arr)}\n")

    print("задача про рюкзак (вместимость 5)")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    print(f"результат: {knapsack(5, weights, values)}")
