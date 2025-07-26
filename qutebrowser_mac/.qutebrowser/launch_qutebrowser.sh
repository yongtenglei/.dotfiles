#!/bin/bash

# A launch wrapper, have to be called by another script, see ./qutebrowser.
# ~/.local/qutebrowser/ is where you install qutebrowser or change this path as you need.
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
exec -a qutebrowser ~/.local/qutebrowser/.venv/bin/python3 -m qutebrowser "$@"
