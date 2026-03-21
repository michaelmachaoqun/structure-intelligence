import argparse

# ------------------------------------------------------------
#  Energy–Intelligence Calculator
#  基于论文《元智能——定义下的跨域比较框架》
#
#  本工具实现论文中的核心物理定义，包括：
#  - 原级能量 E0 = μk * m * g * L
#  - 智能刻度 I0 = 1 / E0
#  - 轮子智能比值 I_wheel / I_lever = μk / c_rr
#  - 发动机智能 I_engine = P / E0
#  - 信息结构智能 I_info = (ops/J) * E0
#
#  所有公式均来自论文原文，并在注释中标明出处。
# ------------------------------------------------------------


# -----------------------------
# 1. 原级能量 E0
# -----------------------------
def compute_E0(mu_k, m, g, L):
    """
    计算原级能量 E0 = μk * m * g * L
    公式来源：论文第 2.3 节
    参数：
        mu_k : 滑动摩擦系数（无量纲）
        m    : 质量（kg）
        g    : 重力加速度（m/s^2）
        L    : 水平移动距离（m）
    返回：
        E0   : 原级任务所需能量（J）
    """
    return mu_k * m * g * L


# -----------------------------
# 2. 智能刻度 I0 = 1 / E0
# -----------------------------
def compute_I0(E0):
    """
    计算智能刻度 I0 = 1 / E0
    公式来源：论文第 2.3.1 节
    返回：
        I0 : 智能刻度（单位：J^-1）
    """
    return 1.0 / E0


# -----------------------------
# 3. 轮子智能比值 μk / c_rr
# -----------------------------
def compute_wheel_ratio(mu_k, c_rr):
    """
    计算轮子相对于杠杆的智能比值：
        I_wheel / I_lever = μk / c_rr
    公式来源：论文第 3 节
    """
    return mu_k / c_rr if c_rr else None


# -----------------------------
# 4. 发动机智能 I_engine = P / E0
# -----------------------------
def compute_engine_intelligence(P, E0):
    """
    计算发动机智能：
        I_engine = P / E0
    公式来源：论文第 4 节
    参数：
        P  : 发动机功率（W = J/s）
        E0 : 原级能量（J）
    返回：
        I_engine : 每秒可完成的“原级任务等价次数”
    """
    return P / E0 if P else None


# -----------------------------
# 5. 信息结构智能
# -----------------------------
def compute_info_intelligence(ops_per_s, power, E0):
    """
    计算信息结构智能：
        ops/J = (operations per second) / power
        I_info = (ops/J) * E0
    公式来源：论文第 5 节
    参数：
        ops_per_s : 每秒运算次数
        power     : 功耗（W = J/s）
        E0        : 原级能量（J）
    返回：
        I_info : 信息结构智能
    """
    if ops_per_s and power:
        ops_per_joule = ops_per_s / power
        return ops_per_joule * E0
    return None


# -----------------------------
# 主程序入口
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Energy–Intelligence Calculator based on the Archi framework."
    )

    # 基础参数（论文第 2.3 节）
    parser.add_argument("--mu_k", type=float, required=True, help="Sliding friction coefficient μk")
    parser.add_argument("--mass", type=float, default=1.0, help="Mass m (kg)")
    parser.add_argument("--distance", type=float, default=1.0, help="Distance L (m)")
    parser.add_argument("--g", type=float, default=9.81, help="Gravity acceleration g (m/s^2)")

    # 发动机参数（论文第 4 节）
    parser.add_argument("--power", type=float, help="Engine power P (W)")

    # 轮子参数（论文第 3 节）
    parser.add_argument("--c_rr", type=float, help="Rolling resistance coefficient c_rr")

    # 信息结构参数（论文第 5 节）
    parser.add_argument("--ops", type=float, help="Operations per second")
    parser.add_argument("--p_info", type=float, help="Power consumption of info structure (W)")

    args = parser.parse_args()

    # -----------------------------
    # 计算原级能量 E0
    # -----------------------------
    E0 = compute_E0(args.mu_k, args.mass, args.g, args.distance)
    I0 = compute_I0(E0)

    print("--------------------------------------------------")
    print("原级能量与智能刻度（论文第 2.3 节）")
    print("--------------------------------------------------")
    print(f"E0 = {E0:.4f} J")
    print(f"I0 = {I0:.6f} 1/J")

    # -----------------------------
    # 轮子智能比值
    # -----------------------------
    if args.c_rr:
        ratio = compute_wheel_ratio(args.mu_k, args.c_rr)
        print("\n轮子智能比值（论文第 3 节）")
        print(f"I_wheel / I_lever = {ratio:.4f}")

    # -----------------------------
    # 发动机智能
    # -----------------------------
    if args.power:
        I_engine = compute_engine_intelligence(args.power, E0)
        print("\n发动机智能（论文第 4 节）")
        print(f"I_engine = {I_engine:.4f} Archis/s")

    # -----------------------------
    # 信息结构智能
    # -----------------------------
    if args.ops and args.p_info:
        I_info = compute_info_intelligence(args.ops, args.p_info, E0)
        print("\n信息结构智能（论文第 5 节）")
        print(f"I_info = {I_info:.4e}")

    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
