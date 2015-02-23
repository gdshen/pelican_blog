#!/bin/zsh

pwd
pelican content > /dev/null
git add -A
git commit -m $1
git push

cd output
git add -A
git commit -m $1
git push
cd ..
