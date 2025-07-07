import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import random


def generate_triangle_area_question():
    base = random.randint(3, 10)
    height = random.randint(3, 10)
    area = base * height / 2

    fig, ax = plt.subplots()
    ax.set_xlim(0, base)
    ax.set_ylim(0, height)
    triangle = plt.Polygon([(0,0), (base,0), (0,height)], closed=True, fill=None, edgecolor='blue')
    ax.add_patch(triangle)
    ax.text(base/2, -0.2, f"{base} cm", ha='center')
    ax.text(-0.2, height/2, f"{height} cm", va='center', rotation='vertical')
    ax.axis('off')

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    plt.close(fig)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    options = [
        f"{area}",
        f"{area + random.randint(1,5)}",
        f"{area - random.randint(1,3)}",
        f"{area + random.randint(6,10)}"
    ]
    random.shuffle(options)

    return {
        "question": "Koks yra pateiktame trikampyje pavaizduoto plotas?",  # Lithuanian
        "image": img_str,
        "options": options,
        "answer": f"{area}",
        "hint": "Trikampio plotas = b*h/2"
    }
