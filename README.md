# Math Exam Task Generator

This repository provides a simple Python script that generates math exam-style tasks. Some questions require geometric diagrams, which are automatically created using `matplotlib`.

## Requirements

- Python 3.11+
- `matplotlib` (install via `pip install matplotlib`)

## Usage

Run the script to create tasks and save them to a text file. Images for geometry questions will be stored in the specified directory.

```bash
python3 generate_math_exam.py --num 3 --out tasks.txt --img-dir images
```

This command generates three random tasks and writes them along with their answers to `tasks.txt`. Any geometry diagrams are saved under the `images` folder.
