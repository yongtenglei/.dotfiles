#!/bin/bash

# A launch wrapper, have to be called by another script.
# ~/.local/qutebrowser/ is where you install qutebrowser or change this path as you need.
exec -a qutebrowser ~/.local/qutebrowser/.venv/bin/python3 -m qutebrowser "$@"
