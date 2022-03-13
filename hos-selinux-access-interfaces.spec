BuildArch: noarch
BuildRequires: make, selinux-policy-devel
Group: System Environment/Base
License: GPLv3
Name: hos-selinux-access-interfaces
Release: 1%{?dist}
Requires: policycoreutils, libselinux-utils
Source0: hos-access-interfaces.if
Summary: SELinux access interfaces for Hard Hat OS (HOS)
URL: https://github.com/HardHatOS/selinux-access-interfaces
Version: 1.0

%description
SELinux access interfaces for the Hard Hat OS (HOS) project

%pre
# RPM macro that defines the SELinux directory where the interface files are placed in
%define _contribdir %{_datadir}/selinux/devel/include/contrib

%install
# Copy the compiled SELinux policy module to the proper directory
%{__install} -D -m 0644 %{SOURCE0} -t %{buildroot}%{_contribdir}

%files
%{_contribdir}/hos-access-interfaces.if
