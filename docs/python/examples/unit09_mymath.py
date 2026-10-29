"""自訂模組：簡單的數學工具。"""
PI = 3.14159


def circle_area(r):
    """回傳半徑為 r 的圓面積"""
    return PI * r ** 2


def is_even(n):
    """n 為偶數回傳 True"""
    return n % 2 == 0


if __name__ == "__main__":
    # 只有直接執行本檔案時才會跑到這裡，被 import 時不會執行
    print("測試 circle_area(2)：", round(circle_area(2), 2))
