Name:       sailqemu-libslirp
Version:    4.9.5
Release:    2
Summary:    Private libslirp networking library for SailQEMU
Group:      System/Libraries
License:    BSD-3-Clause AND MIT
URL:        https://gitlab.com/qemu-project/libslirp
Source0:    %{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: ninja
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)

%description
Builds libslirp from pinned upstream source; includes headers and pkgconfig
metadata under /opt/sailqemu/libslirp-4.9.5 for a separate QEMU package.

%prep
%setup -q
test -f upstream/meson.build || { echo 'Upstream submodule missing'; exit 1; }

%build
meson setup _build upstream --prefix=/opt/sailqemu/libslirp-4.9.5 --libdir=lib64 --buildtype=release --wrap-mode=nodownload
ninja -C _build -j 2

%install
DESTDIR=%{buildroot} ninja -C _build install

%files
/opt/sailqemu/libslirp-4.9.5
