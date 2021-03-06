#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtr
Version  : 0.94
Release  : 8
URL      : https://github.com/traviscross/mtr/archive/v0.94/mtr-0.94.tar.gz
Source0  : https://github.com/traviscross/mtr/archive/v0.94/mtr-0.94.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mtr-bin = %{version}-%{release}
Requires: mtr-data = %{version}-%{release}
Requires: mtr-license = %{version}-%{release}
Requires: mtr-man = %{version}-%{release}
Requires: mtr-setuid = %{version}-%{release}
BuildRequires : libcap-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(jansson)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)

%description
WHAT IS MTR?
===
mtr combines the functionality of the 'traceroute' and 'ping' programs
in a single network diagnostic tool.

%package bin
Summary: bin components for the mtr package.
Group: Binaries
Requires: mtr-data = %{version}-%{release}
Requires: mtr-setuid = %{version}-%{release}
Requires: mtr-license = %{version}-%{release}

%description bin
bin components for the mtr package.


%package data
Summary: data components for the mtr package.
Group: Data

%description data
data components for the mtr package.


%package license
Summary: license components for the mtr package.
Group: Default

%description license
license components for the mtr package.


%package man
Summary: man components for the mtr package.
Group: Default

%description man
man components for the mtr package.


%package setuid
Summary: setuid components for the mtr package.
Group: Default

%description setuid
setuid components for the mtr package.


%prep
%setup -q -n mtr-0.94
cd %{_builddir}/mtr-0.94

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600963002
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1600963002
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mtr
cp %{_builddir}/mtr-0.94/COPYING %{buildroot}/usr/share/package-licenses/mtr/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mtr

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mtr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mtr/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/mtr-packet.8
/usr/share/man/man8/mtr.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/mtr-packet
