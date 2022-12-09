from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Directory:
    name: str
    parent: "Directory" | None = None
    file_size: int = 0
    children: list[Directory] = field(default_factory=list)

    @property
    def total_file_size(self) -> int:
        return self.file_size + sum(child.total_file_size for child in self.children)

    @property
    def full_path(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent.full_path}/{self.name}"

    def __str__(self) -> str:
        return f"{self.full_path} ({self.total_file_size})"

    def full_print(self, indent: int = 0):
        print(" " * indent, self)
        for child in self.children:
            child.full_print(indent + 2)


def get_all_dirs(root: Directory) -> list[Directory]:
    dirs = [root]
    for child in root.children:
        dirs.extend(get_all_dirs(child))
    return dirs


def get_directories(raw_input: str) -> Directory:
    cds = raw_input.split("$ cd ")

    current_dir = None

    base_dir = None

    for cd in cds:
        if not cd:
            continue
        lines = cd.splitlines()
        dir_name = lines[0].strip()
        if dir_name == "..":
            if current_dir is None:
                raise ValueError("Can't go up from root")
            current_dir = current_dir.parent
        else:
            dir = Directory(dir_name, parent=current_dir)
            if current_dir is not None:
                current_dir.children.append(dir)
            current_dir = dir
            if base_dir is None:
                base_dir = current_dir
            for line in lines[1:]:
                if line.startswith("dir") or line == "$ ls":
                    pass
                else:
                    dir.file_size += int(line.split()[0])

    if base_dir is None:
        raise ValueError("No base dir found")

    return base_dir


def small_dirs(base_dir: Directory) -> int:
    return sum(
        dir.total_file_size
        for dir in get_all_dirs(base_dir)
        if dir.total_file_size <= 100000
    )


sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


sample_base_dir = get_directories(sample)

assert small_dirs(sample_base_dir) == 95437

full_input = Path("day07").read_text()

base_dir = get_directories(full_input)

print(small_dirs(base_dir))

TOTAL_SIZE = 70_000_000


def get_smallest_dir(base_dir: Directory, min_size: int = 30_000_000) -> int:
    all_dirs = get_all_dirs(base_dir)
    remaining_size = TOTAL_SIZE - base_dir.total_file_size
    dirs = [d for d in all_dirs if (remaining_size + d.total_file_size) >= min_size]
    dirs.sort(key=lambda dir: dir.total_file_size)
    return dirs[0].total_file_size


assert get_smallest_dir(sample_base_dir) == 24933642

print(get_smallest_dir(base_dir))
