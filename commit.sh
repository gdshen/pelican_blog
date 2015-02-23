#!/bin/zsh

pwd
pelican content
echo $1
git add -A
git commit -m $1
git push
cd output
git status
git add -A
git commit -m $1
git push
cd ..
