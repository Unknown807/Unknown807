#!/bin/bash

msg=$(git status)

if [[ $msg == *"nothing to commit, working tree clean"* ]]; then
    echo "Clean working tree, no commits necessary";
else
    echo "New files to be committed";
    git add -A
    git config --global user.email "github-action-bot@example.com"
    git config --global user.name "Github Action Bot"
    git commit -am "Updated Readme"
    git push
fi