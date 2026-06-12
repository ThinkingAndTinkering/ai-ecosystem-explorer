#!/usr/bin/env bash
# Render static-site build: publish The Machine as the front page,
# the 3D Explorer as /explorer.html, plus the handbook (md + pdf).
set -euo pipefail
rm -rf dist && mkdir -p dist

# The Machine becomes the site root; its footer link to the Explorer is repointed.
sed 's|href="index.html"|href="explorer.html"|' the-machine.html > dist/index.html

cp index.html dist/explorer.html
cp handbook.pdf dist/handbook.pdf
cp handbook.md dist/handbook.md

echo "dist/ ready:" && ls -la dist
