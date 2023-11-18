import cplex
import math
def solve():


    # 场地尺寸和射灯光斑半径
    length = 3700  # 南北长度
    width = 7400  # 东西宽度
    R = 190.53  # 光斑半径

    # 计算网格尺寸（假设10%重叠）
    grid_size = 306.90
    rows = math.ceil(length / grid_size)
    cols = math.ceil(width / grid_size)

    # 创建CPLEX模型
    cpx = cplex.Cplex()
    cpx.objective.set_sense(cpx.objective.sense.minimize)

    # 添加决策变量
    var_names = [f"x_{i}_{j}" for i in range(rows) for j in range(cols)]
    cpx.variables.add(names=var_names, types=["B"] * len(var_names))

    # 添加目标函数（最小化射灯数量）
    cpx.objective.set_linear([(var_name, 1.0) for var_name in var_names])

    # 添加约束（这里需要根据实际情况添加合适的覆盖约束）
    ## TODO: 需要推理精确的覆盖约束
    # for i in range(rows):
    #     for j in range(cols):
    #         # 选取射灯 (i, j) 可以覆盖的所有网格点
    #         covered_points = [(i + di, j + dj) for di in range(-1, 2) for dj in range(-1, 2)
    #                           if 0 <= i + di < rows and 0 <= j + dj < cols]
    #         # 添加覆盖约束
    #         for point in covered_points:
    #             var_name = f"x_{point[0]}_{point[1]}"
    #             # 每个点至少被一个射灯覆盖
    #             cpx.linear_constraints.add(
    #                 lin_expr=[cplex.SparsePair(ind=[var_name], val=[1])],
    #                 senses=["G"],
    #                 rhs=[1]
    #             )

    # 求解模型
    cpx.solve()

    # 获取结果
    solution = cpx.solution.get_values()
    for i in range(rows):
        for j in range(cols):
            if solution[i * cols + j] > 0.5:  # 如果在这个位置放置了射灯
                print(f"在位置 ({i}, {j}) 放置射灯")


if __name__ == "__main__":
    solve()