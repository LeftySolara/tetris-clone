#!/bin/bash

sphinx-apidoc -f --ext-autodoc -o docs/source tetris 
sphinx-build -b html docs/source/ docs/build/html
