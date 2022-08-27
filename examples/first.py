#!/usr/bin/python3

import sys

def capture_args() -> list[str]:
    acum = []

    for arg in sys.argv:
        index = sys.argv.index(arg)
        acum.append(f"arg[{index}] = {arg}")

    return acum

def main():
    args = capture_args()
    print(args)

if __name__ == "__main__":
    main()
