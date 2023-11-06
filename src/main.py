#!/usr/bin/env python3

import lib
import os

if __name__ == "__main__":

    usr = os.getenv("USER")
    lib.func(f'Hello, {usr}')
