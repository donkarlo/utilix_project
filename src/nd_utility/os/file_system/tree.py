from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class TreePrinterConfig:
    root: Path
    max_depth: Optional[int]
    include_files: bool
    show_hidden: bool
    exclude_names: List[str]


class DirectoryTreePrinter:
    def __init__(self, config: TreePrinterConfig) -> None:
        self._config = config

    def print_tree(self) -> None:
        root = self._config.root.resolve()
        print(root.as_posix())
        self._print_dir(current_dir=root, prefix="", depth=0)

    def _print_dir(self, current_dir: Path, prefix: str, depth: int) -> None:
        if self._config.max_depth is not None and depth >= self._config.max_depth:
            return

        children = self._list_children(current_dir)
        if not children:
            return

        last_index = len(children) - 1
        for index, child in enumerate(children):
            is_last = index == last_index
            branch = "└── " if is_last else "├── "
            print(f"{prefix}{branch}{child.name}")

            if child.is_dir():
                extension = "    " if is_last else "│   "
                self._print_dir(child, prefix + extension, depth + 1)

    def _list_children(self, directory: Path) -> List[Path]:
        try:
            entries = list(directory.iterdir())
        except (PermissionError, FileNotFoundError):
            return []

        filtered: List[Path] = []
        for entry in entries:
            if not self._config.show_hidden and entry.name.startswith("."):
                continue
            if entry.name in self._config.exclude_names:
                continue
            if entry.is_dir():
                filtered.append(entry)
            else:
                if self._config.include_files:
                    filtered.append(entry)

        filtered.sort(key=self._sort_key)
        return filtered

    def _sort_key(self, path: Path) -> tuple:
        is_file = 1 if path.is_file() else 0
        return (is_file, path.name.lower())


class ArgumentParserFactory:
    def create(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="Print a directory tree (copy-paste friendly) to the terminal."
        )
        parser.add_argument("path", nargs="?", default=".", help="Root directory (default: .)")
        parser.add_argument("--max-depth", type=int, default=None, help="Limit depth (default: unlimited)")
        parser.add_argument("--dirs-only", action="store_true", help="Show directories only (exclude files)")
        parser.add_argument("--hidden", action="store_true", help="Include hidden files/directories")
        parser.add_argument(
            "--exclude",
            action="append",
            default=[],
            help="Exclude by name (repeatable). Example: --exclude .git --exclude __pycache__",
        )
        return parser


class Application:
    def __init__(self) -> None:
        self._parser = ArgumentParserFactory().create()

    def run(self) -> None:
        args = self._parser.parse_args()

        if args.path == ".":
            user_input = input("Enter directory path: ").strip()
            if user_input:
                root = Path(user_input)
            else:
                root = Path(".")
        else:
            root = Path(args.path)

        config = TreePrinterConfig(
            root=root,
            max_depth=args.max_depth,
            include_files=not args.dirs_only,
            show_hidden=args.hidden,
            exclude_names=list(args.exclude),
        )
        DirectoryTreePrinter(config).print_tree()


if __name__ == "__main__":
    Application().run()