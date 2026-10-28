# sailqemu-libslirp 4.9.5 — source RPM recipe (EXPERIMENTAL)

This is a **GitHub packaging repository starter**, not an upstream source fork,
OBS result or tested SDK build. It builds the upstream libslirp v4.9.5 sources
from a fixed git submodule in a Sailfish SDK or OBS tar_git source archive.

**Setup after extracting the ZIP**:

```sh
git init -b main
sh scripts/add-upstream.sh
git add .
git commit -m "Package libslirp 4.9.5 from pinned source"
git tag v4.9.5   # local build version; push only after testing
```

The pinned upstream commit is `390848f47391f412451b2d259d8527fabb51e5e3`.
The source is not copied into this starter ZIP. `git submodule add` fetches it
from the official upstream, and records the actual gitlink in the repository.
The OBS tar_git service should include git submodules; **verify it on your OBS**.

Select an `aarch64` target in Sailfish SDK 5.1 and run `sfdk build`.
Build on `armv7hl` too once a matching target exists. Check build dependencies,
RPM architecture, shared-library path, licenses and symbols before installation.

Expected private install prefix: `/opt/sailqemu/libslirp-4.9.5`.
The package also provides headers and `slirp.pc` under its private prefix;
QEMU must set `PKG_CONFIG_PATH` to discover it. Do not publish until the SDK
and OBS builds and the network smoke test pass.

Upstream: https://gitlab.com/qemu-project/libslirp
