# 範例 3：continue 與巢狀迴圈
# continue：跳過本圈剩下的程式，直接進入下一圈
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 巢狀迴圈：外層每跑一圈，內層完整跑一輪
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
