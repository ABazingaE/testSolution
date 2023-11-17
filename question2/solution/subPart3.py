from solution.subPart2 import getW
import numpy as np


def calculate_optimal_layout(length, width, D, alpha, theta):
    # 计算射灯的覆盖宽度
    W = getW(alpha, theta, D)

    # 计算最优间距，满足重叠率在10%到20%之间
    min_overlap = W * 0.1
    max_overlap = W * 0.2
    optimal_spacing = W - (min_overlap + max_overlap) / 2

    # 计算南北方向和东西方向所需的射灯数量
    num_lights_north_south = int(length / optimal_spacing) + 1
    num_lights_east_west = int(width / optimal_spacing) + 1

    # 计算总共所需的射灯数量
    total_lights = num_lights_north_south * num_lights_east_west

    return total_lights, optimal_spacing

# 场地参数
length = 3700  # 南北长
width = 7400  # 东西宽
D = 110  # 射灯高度
alpha = 1.5 * np.pi / 180  # 地面倾斜角度
theta = 120 * np.pi / 180  # 射灯开角


if __name__ == "__main__":
    # 计算布局方案
    total_lights, spacing = calculate_optimal_layout(length, width, D, alpha, theta)
    print(f"Total lights needed: {total_lights}")
    print(f"Optimal spacing: {spacing} meters")
