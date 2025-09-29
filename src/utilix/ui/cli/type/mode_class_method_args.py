import argparse

class ModeClassMethodArgs(Command):
    def __init__(self, package_name:str):
        parser = argparse.ArgumentParser(prog=package_name)
        parser.add_argument("namespace", help="Main mode (e.g., experiment)")
        parser.add_argument("class", help="class name (e.g., old)")
        parser.add_argument("method", help="method name (e.g., learn)")
        parser.add_argument("arguments", help="arguments (--epochs 10)")
        self._args = parser.parse_args()