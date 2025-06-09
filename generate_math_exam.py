import random
import argparse
import os
import math
from typing import Tuple
import matplotlib.pyplot as plt


def generate_algebra_task() -> Tuple[str, str]:
    a = random.randint(1, 10)
    x = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    question = f"Solve for x: {a}x + {b} = {c}"
    return question, str(x)


def generate_geometry_task(output_dir: str) -> Tuple[str, str]:
    a = random.randint(3, 10)
    b = random.randint(3, 10)
    c = math.sqrt(a ** 2 + b ** 2)

    # Draw right triangle
    fig, ax = plt.subplots()
    ax.plot([0, a, 0, 0], [0, 0, b, 0], "k-")
    ax.set_aspect("equal")
    ax.axis("off")

    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"triangle_{a}_{b}.png")
    plt.savefig(filename, bbox_inches="tight")
    plt.close(fig)

    question = f"Consider a right triangle with legs a={a} and b={b}. What is the length of the hypotenuse? See diagram: {filename}"
    return question, f"{c:.2f}"


def generate_arithmetic_task() -> Tuple[str, str]:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    else:
        result = a * b
    question = f"Calculate: {a} {op} {b}"
    return question, str(result)


def generate_tasks(num: int, output_dir: str) -> list[Tuple[str, str]]:
    task_funcs = [
        lambda: generate_algebra_task(),
        lambda: generate_geometry_task(output_dir),
        lambda: generate_arithmetic_task(),
    ]
    tasks = []
    for _ in range(num):
        func = random.choice(task_funcs)
        tasks.append(func())
    return tasks


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate exam-style math tasks")
    parser.add_argument("--num", type=int, default=5, help="Number of tasks to generate")
    parser.add_argument("--out", default="tasks.txt", help="Output text file")
    parser.add_argument("--img-dir", default="images", help="Directory to save generated images")
    args = parser.parse_args()

    tasks = generate_tasks(args.num, args.img_dir)
    with open(args.out, "w") as f:
        for idx, (question, answer) in enumerate(tasks, start=1):
            f.write(f"Task {idx}: {question}\nAnswer: {answer}\n\n")
    print(f"Generated {len(tasks)} tasks in {args.out}")


if __name__ == "__main__":
    main()
