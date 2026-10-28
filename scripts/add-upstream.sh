#!/bin/sh
set -eu
# Run from this packaging repository AFTER git init, before initial commit.
[ -d .git ] || { echo 'Run git init -b main first'; exit 1; }
[ ! -e upstream ] || { echo 'upstream exists; inspect its pinned revision'; exit 1; }
git submodule add https://gitlab.com/qemu-project/libslirp.git upstream
git -C upstream checkout 390848f47391f412451b2d259d8527fabb51e5e3
actual=$(git -C upstream rev-parse HEAD)
[ "$actual" = 390848f47391f412451b2d259d8527fabb51e5e3 ] || exit 1
printf 'Pinned upstream commit: %s\n' "$actual"
