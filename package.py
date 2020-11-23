# -*- coding: utf-8 -*-

name = "ptex"

version = "4.1.4"

authors = ["Walt Disney Animation Studio"]

requires = [
    "gcc",
    "cmake",
    "zlib",
]

build_system = "cmake"

def commands():
    env.PTEX_ROOT = "{root}"
    env.PTEX_LOCATION = "{root}"

uuid = "repository.ptex"
