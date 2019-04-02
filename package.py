# -*- coding: utf-8 -*-

name = "ptex"

version = "2.1.28"

authors = ["Walt Disney Animation Studio"]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.ptexs"
