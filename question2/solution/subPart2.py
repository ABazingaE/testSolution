import math



from solution.utils.baseUtil import getGroundLine, getLightLine, getThirdLine, getCrossPoint, getDistance,  draw

"""
射灯照射光束以锥形散开，能够照射出以射线为轴线且具有一定角度的光带，
光带的覆盖宽度 𝑊 随射灯开角θ和天花板高度𝐷 的变化而变化。若两个射灯
射线相互平行且地面水平平坦，则相邻光带之间的重叠率定义为 η = 1 −
𝑑/𝑊
中 𝑑 为相邻两条射线的间距，𝑊 为光带的覆盖宽度

若η < 0,则表示照射覆盖范围存在未照射的暗部。为保证室内光照的均匀性，
相邻光带之间应有 10%-20% 的重叠率。如果重叠率过大，则会造成光源的增多，
资源的浪费，影响射灯的使用效率
实际地面一般不会绝对的水平，假如地面与水平面构成的夹角为α，称α为坡度。请建立该种情况下射灯的覆盖宽度及相邻光带之间重叠率
的数学模型

思路：
以射灯原点建立平面直角坐标系，根据地面的倾斜角α表示出地面倾斜的直线，这是第一条直线，
再表示第二条直线，第二条直线过原点，倾斜角为90° - θ/2。
再表示出第三条直线，斜率为第二条直线的斜率的相反数，然后获得第一条直线与另外两条直线的交点，两个交点的距离为W


结论：
从运行结果来看，最后两组情况没有发生重叠，且覆盖宽度小于200（灯源间距离）
从这个现象我怀疑，在地面倾斜的情况下，覆盖率的数学模型仍与第一问中的公式有关系，即η = 1 − d/ W
经过验证，地面倾斜时，覆盖率数学模型应修正为η = 1 − d/ （W1+W2）/2；即原公式中的W要换成相邻两个光源的平均覆盖宽度
"""

## 角度转换为弧度
alpha = math.radians(1.5)
theta = math.radians(120)


# 全局变量用于存储交点
# 每个元素的格式：(灯源编号, (交点1坐标), (交点2坐标))
cross_points = []
"""
传入灯源编号
"""
def getW(light_id):
    global cross_points
    k1, b1 = getGroundLine(alpha, 70)
    k2, b2 = getLightLine(theta)
    k3, b3 = getThirdLine(k2)
    """
    根据lightId判断这组灯源的位置，涉及到平移直线，
    计算id-4，若为负则向左平移，若为正则向右平移，平移距离为绝对值乘以200,更新截距
    """
    b2 = b2 - (light_id[0] - 4) * 200 * k2
    b3 = b3 - (light_id[0] - 4) * 200 * k3
    x1, y1 = getCrossPoint(k1, b1, k2, b2)
    x2, y2 = getCrossPoint(k1, b1, k3, b3)
    # 保存交点信息，并附上灯源编号
    cross_points.append((light_id, (x1, y1), (x2, y2)))
    W = getDistance(x1, y1, x2, y2)
    return W

"""
射灯距地面高度即地面直线（第一条直线）对应位置的纵坐标的绝对值
因为图形为直线，观察到表格中所求位置为均匀间隔200，不用一个个点算，
只需算出横坐标变化200时纵坐标的变化，结合原点处的纵坐标，即可得到一个等差数列
"""

def get_spotlight_height_above_ground():
    D = 70  # 射灯到地面的距离
    k1, b1 = getGroundLine(alpha, D)  # 获取地面直线的斜率和截距

    # 等差数列的公差
    d = k1 * 200

    # 原点处的纵坐标（射灯高度）
    height_at_origin = -D

    # 计算等差数列
    heights = [height_at_origin + i * d for i in range(-4, 5)]
    print(heights)
    return heights



def calculate_overlap_rate():
    global cross_points

    overlap_rates = []
    for i in range(1, len(cross_points)):
        # 获取相邻灯源的交点信息
        _, (x1_left, y1_left), (x1_right, y1_right) = cross_points[i - 1]
        _, (x2_left, y2_left), (x2_right, y2_right) = cross_points[i]

        # 判断是否重叠并计算重叠长度
        overlap_length = 0
        if x1_right >= x2_left and x2_right >= x1_left:
            # 两个交点中更靠左和更靠右的点
            overlap_x_left = max(x1_left, x2_left)
            overlap_y_left = k1 * overlap_x_left + b1
            overlap_x_right = min(x1_right, x2_right)
            overlap_y_right = k1 * overlap_x_right + b1

            # 计算两个交点之间的距离
            overlap_length = ((overlap_x_right - overlap_x_left) ** 2 +
                              (overlap_y_right - overlap_y_left) ** 2) ** 0.5

        # 计算覆盖宽度
        coverage_width = ((x1_right - x1_left) ** 2 +
                          (y1_right - y1_left) ** 2) ** 0.5

        # 计算重叠率
        overlap_rate = overlap_length / coverage_width if coverage_width > 0 else 0
        overlap_rates.append(overlap_rate)

    return overlap_rates

if __name__ == "__main__":
    k1, b1 = getGroundLine(alpha, 70)
    k2, b2 = getLightLine(theta)
    k3, b3 = getThirdLine(k2)
    #draw()
    draw(k1,b1,k2,b2,k3,b3,200)
    print("射灯距地面高度")
    heights = get_spotlight_height_above_ground()
    print("覆盖宽度")
    ## 遍历height，调用getW
    coverages = []
    for light_id in enumerate(heights):
        coverage = getW(light_id)
        coverages.append(coverage)

    # 打印结果
    for i, coverage in enumerate(coverages):
        print(f"Point {i - 4}: Coverage Width = {coverage} meters")

    ## 计算相邻的重叠率
    print("重叠率")
    overlap_rates = calculate_overlap_rate()
    for rate in overlap_rates:
        print(f"Overlap rate: {rate:.2f}")







