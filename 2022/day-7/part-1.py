with open("2022/day-7/input.txt", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    print("nr of dirs", len([l for l in lines if l.startswith('dir')]))


def find_next_index(list_to_check, item_to_find, start, directory):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value.startswith(item_to_find):
            indices.append(idx)
    indices = [i for i in indices if i > start] 
    if indices:
        return indices[0]
    else: 
        return None

def find_last_index(list_to_check, item_to_find, before):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    indices = [i for i in indices if i < before] 
    return indices[-1]

dirs = dict()

def get_dir_size(lines):
    for i, line in enumerate(lines):
        if line.startswith('$ cd') and not line == '$ cd ..':
            directory = line.split(' ')[2]
        if line == '$ ls':
            start = i
            end = find_next_index(lines, '$', start, directory)
            dir_content = lines[start:end]
            dir_content = dir_content[1:]
            files_only = all(d[0].isdigit() for d in dir_content)
            if files_only:
                content_size = 0
                for item in dir_content:
                    if item[0].isdigit():
                        content_size += int(item.split(' ')[0])
                dirs[directory] = content_size
                if directory != '/' and end is not None:
                    lines[find_last_index(lines, f'dir {directory}', start)] = str(content_size)
                    del lines[start:end+1]
                    get_dir_size(lines)
            else:
                continue

get_dir_size(lines)
print("nr of found dirs", len(dirs.keys()))

below_10000 = 0
for k, v in dirs.items():
    if v < 100000:
        below_10000 += v

print(below_10000)