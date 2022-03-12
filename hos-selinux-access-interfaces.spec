Name:       hos-selinux-access-interfaces
Version:    1.0
Release:    1%{?dist}
Summary:    SELinux access interfaces for the Hard Hat OS (HOS) project

Group:      System Environment/Base
License:    GPLv3
URL:        https://github.com/HardHatOS/selinux-access-interfaces
Source0:    hos-access-interfaces.if
Requires:   policycoreutils, libselinux-utils
BuildArch:  noarch
BuildRequires: make, selinux-policy-devel

%description
This package installs and sets up a hardened SELinux policy module for D-Bus.

%pre
# RPM macro that defines the SELinux directory where the interface files are placed in
%define _contribdir %{_datadir}/selinux/devel/include/contrib

%install
# Copy the compiled SELinux policy module to the proper directory
%{__install} -D -m 0644 %{SOURCE0} -t %{buildroot}%{_contribdir}

%files
%{_contribdir}/hos-access-interfaces.if
