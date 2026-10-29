"""自訂模組：溫度轉換。"""


def c_to_f(c):
    """攝氏轉華氏"""
    return c * 9 / 5 + 32


def f_to_c(f):
    """華氏轉攝氏"""
    return (f - 32) * 5 / 9
