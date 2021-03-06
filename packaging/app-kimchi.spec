
Name: app-kimchi
Epoch: 1
Version: 1.1.2
Release: 1%{dist}
Summary: Kimchi
License: GPLv3
Group: ClearOS/Apps
Packager: eGloo
Vendor: Marc Laporte
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base

%description
Kimchi is an HTML5 based management tool for KVM. It is designed to make it as easy as possible to get started with KVM.

%package core
Summary: Kimchi - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: kimchi
Requires: app-base >= 1:2.3.7
Requires: app-nginx-core

%description core
Kimchi is an HTML5 based management tool for KVM. It is designed to make it as easy as possible to get started with KVM.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/kimchi
cp -r * %{buildroot}/usr/clearos/apps/kimchi/

install -d -m 0755 %{buildroot}/var/clearos/kimchi
install -d -m 0755 %{buildroot}/var/clearos/kimchi/backup
install -D -m 0644 packaging/wokd.php %{buildroot}/var/clearos/base/daemon/wokd.php

%post
logger -p local6.notice -t installer 'app-kimchi - installing'

%post core
logger -p local6.notice -t installer 'app-kimchi-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/kimchi/deploy/install ] && /usr/clearos/apps/kimchi/deploy/install
fi

[ -x /usr/clearos/apps/kimchi/deploy/upgrade ] && /usr/clearos/apps/kimchi/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kimchi - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-kimchi-core - uninstalling'
    [ -x /usr/clearos/apps/kimchi/deploy/uninstall ] && /usr/clearos/apps/kimchi/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/kimchi/controllers
/usr/clearos/apps/kimchi/htdocs
/usr/clearos/apps/kimchi/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/kimchi/packaging
%dir /usr/clearos/apps/kimchi
%dir /var/clearos/kimchi
%dir /var/clearos/kimchi/backup
/usr/clearos/apps/kimchi/deploy
/usr/clearos/apps/kimchi/language
/usr/clearos/apps/kimchi/libraries
/var/clearos/base/daemon/wokd.php
