BMI 计算器：输入身高体重，输出 BMI 数值与健康建议。

import sys

# 分级标准：中国成人体重判定 WS/T 428-2013
# （WHO 国际标准的分界线为 18.5 / 25 / 30，比这里宽松）
BANDS = [
    (18.5, "偏瘦", [
        "先确认是长期体质偏瘦，还是近期非计划性下降——半年内无故减重超过 5% 建议就医。",
        "增重靠能量密度而非份量：坚果、乳制品、鸡蛋、全脂奶，并在三餐外加两次加餐。",
        "每周 2-3 次抗阻训练，让增加的重量长成肌肉而不只是脂肪。",
    ]),
    (24.0, "正常", [
        "维持比减重容易得多：稳住现在的进食节奏和活动量，定期同一时间称重即可。",
        "每周 150 分钟中等强度有氧，加 2 次力量训练。",
        "同时留意腰围、血压、血脂和血糖——BMI 正常不等于代谢指标正常。",
    ]),
    (28.0, "超重", [
        "目标定在减去当前体重的 5%-10%，这个幅度已足以改善血压、血糖和血脂。",
        "每日减少约 300-500 kcal，优先砍掉含糖饮料、精制碳水和油炸食品。",
        "把活动嵌进日常：通勤步行、爬楼、久坐每小时起身。",
    ]),
    (float("inf"), "肥胖", [
        "按半年以上的长期计划推进，每周减 0.5-1 kg 既安全也更容易守住成果。",
        "建议做一次代谢检查（血压、空腹血糖、血脂、肝功能与肝脏超声）。",
        "从低冲击运动起步（快走、游泳、骑行）保护关节，必要时由医生或营养师制定方案。",
    ]),
]

NORMAL_LOW, NORMAL_HIGH = 18.5, 23.9  # 正常区间，用于反算健康体重


def classify(bmi):
    """返回 BMI 对应的 (分级名称, 建议列表)。"""
    for upper, name, tips in BANDS:
        if bmi < upper:
            return name, tips


def ask(prompt, low, high):
    """读取一个在 [low, high] 范围内的数字，输入不合法就重问。"""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("  请输入数字。")
            continue
        except (EOFError, KeyboardInterrupt):
            sys.exit("\n已取消。")
        if low <= value <= high:
            return value
        print("  超出合理范围（%g-%g），请重新输入。" % (low, high))


def report(height_cm, weight_kg):
    h = height_cm / 100
    bmi = weight_kg / (h * h)
    name, tips = classify(bmi)
    low_kg = NORMAL_LOW * h * h
    high_kg = NORMAL_HIGH * h * h

    print()
    print("身高 %.1f cm   体重 %.1f kg" % (height_cm, weight_kg))
    print("-" * 42)
    print("BMI：%.1f kg/m^2    分级：%s" % (bmi, name))
    print("健康体重区间：%.1f - %.1f kg（BMI %.1f-%.1f）"
          % (low_kg, high_kg, NORMAL_LOW, NORMAL_HIGH))

    if weight_kg < low_kg:
        print("距离健康区间下限还差 %.1f kg。" % (low_kg - weight_kg))
    elif weight_kg > high_kg:
        print("超出健康区间上限 %.1f kg；先减去 %.1f kg（约 5%%）即有明确获益。"
              % (weight_kg - high_kg, weight_kg * 0.05))
    else:
        print("目前在健康区间内，距上限还有 %.1f kg 余量。" % (high_kg - weight_kg))

    print()
    print("建议：")
    for tip in tips:
        print("  · " + tip)

    print()
    print("注：BMI 不区分肌肉与脂肪，也不反映脂肪分布；不适用于未成年人、"
          "孕期哺乳期女性和运动员。仅供参考，不能替代医生诊断。")


def main():
    args = sys.argv[1:]
    if len(args) == 2:
        try:
            height_cm, weight_kg = float(args[0]), float(args[1])
        except ValueError:
            sys.exit("用法：python bmi.py [身高cm] [体重kg]")
    else:
        print("BMI 计算器")
        height_cm = ask("身高（cm）：", 50, 250)
        weight_kg = ask("体重（kg）：", 10, 400)
    report(height_cm, weight_kg)


if __name__ == "__main__":
    main()
