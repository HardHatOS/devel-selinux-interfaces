BuildArch: noarch
Group: System Environment/Base
License: GPLv3
Name: hos-devel-selinux-interfaces
Source0: hos-*.if
Release: 1%{?dist}
Summary: SELinux access interfaces for Hard Hat OS (HOS)
URL: https://github.com/HardHatOS/devel-selinux-interfaces
Version: 1.0

%description
SELinux access interfaces for the Hard Hat OS (HOS) project

%pre
# RPM macro that defines the SELinux directory where the interface files are placed in
%define _contribdir %{_datadir}/selinux/devel/include/contrib

%install
# Copy the interaces to the SELinux contrib directory
%{__install} -D -m 0644 %{SOURCE0} -t %{buildroot}%{_contribdir}

%files
%{_contribdir}/hos-*.if
