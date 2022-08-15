#!/bin/bash

echo "We start out in the following directory..."
pwd

repo="Automatic-Programming"

echo "The real stuff starts here..."

# Test if the repo exists
if [ ! -d ${repo} ]; then

    git clone git@github.com:Seraph2000/Automatic-Programming.git

else
    echo "The repository already exists..."

    echo "cd'ing into Automatic-Programming..."
    cd Automatic-Programming
    pwd

    if [ ! -f "autocommit.sh" ]; then
        cp ../autocommit.sh autocommit.sh
        echo "Adding new script to staging area..."
        git add autocommit.sh
        echo "Committing the file..."
        git commit -m "Adding a new helper file to the collection." 
        echo "Pushing file to the main branch..."
        git push
        echo "Done."
    fi
    
    ls -la

    cd ..

fi


echo "Do we end up back where we started?"
pwd