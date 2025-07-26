#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: quickmark_load.sh <quickmark_name>"
  exit 1
fi

QUICKMARK="$1"
URL="${QUTE_URL:-}"

# fallback
if [ -z "$URL" ] && [ -n "$2" ]; then
  URL="$2"
fi

if [ "$URL" = "about:blank" ]; then
  CMD="quickmark-load $QUICKMARK"
else
  CMD="quickmark-load -t $QUICKMARK"
fi

echo "$CMD" >>"$QUTE_FIFO"
