"""Command line entry point for dynamoslira4e_kit."""
import argparse

from .core import Dynamoslira4eTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="organize files by type")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    sorter = Dynamoslira4eTool(args.path)
    if args.dry_run:
        for name, folder in sorter.plan():
            print(f"{name} -> {folder}/")
        return 0
    for name, folder in sorter.apply():
        print(f"{name} -> {folder}/")
    return 0
