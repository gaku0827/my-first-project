# Temperature Converter
# 摂氏を華氏に変換するプログラム

print("=== Temperature Converter ===")

# 温度を入力
celsius = float(input("摂氏温度を入力してください: "))

# 華氏に変換
fahrenheit = celsius * 9 / 5 + 32

# 結果を表示
print("=== 計算結果 ===")
print(f"摂氏: {celsius} ℃")
print(f"華氏: {fahrenheit:.1f} °F")
