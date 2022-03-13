BuildArch: noarch
BuildRequires: make, selinux-policy-devel
Group: System Environment/Base
License: GPLv3
Name: hos-selinux-access-interfaces
Release: 1%{?dist}
Requires: policycoreutils, libselinux-utils
Source0: hos-add.if
Source1: hos-auth.if
Source2: hos-bind.if
Source3: hos-can.if
Source4: hos-corecmd.if
Source5: hos-create.if
Source6: hos-dbus.if
Source7: hos-delete.if
Source8: hos-dev.if
Source9: hos-domain.if
Source10: hos-exec.if
Source11: hos-files.if
Source12: hos-fs.if
Source13: hos-getty.if
Source14: hos-gnome.if
Source15: hos-init.if
Source16: hos-kernel.if
Source17: hos-list.if
Source18: hos-logging.if
Source19: hos-manage.if
Source20: hos-miscfiles.if
Source21: hos-mmap.if
Source22: hos-mozilla.if
Source23: hos-objpermsets.if
Source24: hos-ps.if
Source25: hos-read.if
Source26: hos-r.if
Source27: hos-rw.if
Source28: hos-selinux.if
Source29: hos-seutil.if
Source30: hos-snapper.if
Source31: hos-sysnetwork.if
Source32: hos-systemd.if
Source33: hos-term.if
Source34: hos-thumb.if
Source35: hos-udev.if
Source36: hos-userdom.if
Source37: hos-virt.if
Source38: hos-xserver.if
Summary: SELinux access interfaces for Hard Hat OS (HOS)
URL: https://github.com/HardHatOS/selinux-access-interfaces
Version: 1.0

%description
SELinux access interfaces for the Hard Hat OS (HOS) project

%pre
# RPM macro that defines the SELinux directory where the interface files are placed in
%define _contribdir %{_datadir}/selinux/devel/include/contrib

%install
# Copy the interaces to the SELinux contrib directory
%{__install} -D -m 0644 %{SOURCE0} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE1} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE2} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE3} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE4} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE5} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE6} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE7} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE8} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE9} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE10} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE11} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE12} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE13} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE14} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE15} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE16} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE17} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE18} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE19} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE20} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE21} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE22} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE23} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE24} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE25} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE26} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE27} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE28} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE29} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE30} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE31} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE32} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE33} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE34} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE35} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE36} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE37} -t %{buildroot}%{_contribdir}
%{__install} -D -m 0644 %{SOURCE38} -t %{buildroot}%{_contribdir}

%files
%{_contribdir}/hos-*.if
