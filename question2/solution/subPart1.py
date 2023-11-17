import pandas as pd

from solution.utils.calculator import calculate_overlap_rate

# 定义固定的D值和变化的d和theta值
D = 120
distances = [100, 150, 200, 250]
angles = [80, 90, 100, 120]


def main():
    data = []
    for d in distances:
        row = []
        for theta in angles:
            eta = calculate_overlap_rate(d, theta, D)
            row.append(eta)
        data.append(row)

    # 使用pandas创建DataFrame
    df = pd.DataFrame(data, index=[f"θ={angle}°" for angle in angles],
                      columns=[f"d={distance}" for distance in distances])

    # 输出表格
    print("覆盖率")
    print(df)



if __name__ == "__main__":
    main()