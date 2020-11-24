# -*- coding: utf-8 -*-

name = "ptex"

version = "4.1.4"

authors = ["Walt Disney Animation Studio"]

requires = [
    "gcc",
    "cmake",
]

build_system = "cmake"

def commands():
    env.PTEX_ROOT = "{root}"
    env.PTEX_LOCATION = "{root}"
    env.PATH.append("{root}/bin")

uuid = "repository.ptex"
