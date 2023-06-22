#!/bin/bash

sphinx-apidoc -f --ext-autodoc -o docs/source src/tetris 
sphinx-build -b html docs/source/ docs/build/html
