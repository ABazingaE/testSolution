import math

def calculate_overlap_rate(d, theta, D):
    # 将角度转换为弧度
    theta_radians = math.radians(theta)

    # 计算光带的覆盖宽度 W
    W = 2 * D * math.tan(theta_radians / 2)

    # 计算并返回重叠率 eta
    eta = 1 - d / W
    return eta
