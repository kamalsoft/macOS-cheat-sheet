#!/bin/sh

# Check if index.md is being committed
if git diff --cached --name-only | grep -q "^index.md$"; then
    echo "index.md is modified. Syncing index.html..."
    python3 update_site.py once

    if [ $? -ne 0 ]; then
        echo "Error: Failed to update index.html"
        exit 1
    fi

    # Stage the updated index.html so it's included in the commit
    git add index.html
fi