Name:       hos-selinux-access-interfaces
Version:    1.0
Release:    1%{?dist}
Summary:    SELinux access interfaces required by the Hard Hat OS (HOS) project

Group:      System Environment/Base
License:    AGPLv3
URL:        https://github.com/HardHatOS/selinux-access-interfaces
Source0:    hardhatos.if
BuildArch:  noarch
Requires:   policycoreutils, libselinux-utils
Requires(post):   selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils

%description
SELinux access interaces required by the Hard Hat OS (HOS) project

%build

%install
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/devel/include/contrib/

%files
%{_datadir}/selinux/devel/include/contrib/hardhatos.if
