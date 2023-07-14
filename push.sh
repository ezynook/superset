#!/bin/sh
MSG=""
if [ -n "$1" ]; then
    MSG=$1
else
    MSG="*"
fi
find . -name ".DS_Store" -delete
git add .
git commit -m "[$MSG] at: $(date +'%Y%m%d %H:%M:%S')"
git push -u origin main
echo "-------"
echo "Pushed"
echo "-------"