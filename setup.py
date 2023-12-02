import os

year = "2023"

for i in range(2, 25):
    path = f"{year}/day-{i}"
    if not os.path.exists(path):
        os.mkdir(path)
        py_file = f"{year}/day-{i}/part-1.py"
        input_file = f"{year}/day-{i}/input.txt"
        if not os.path.exists(py_file):
            with open(py_file, "w") as new_py_file:
                pass
        if not os.path.exists(input_file):
            with open(input_file, "w") as new_input_file:
                pass

print(f"Structure for {year} created!")
