BuildArch: noarch
Group: System Environment/Base
License: GPLv3
Name: hos-devel-selinux-interfaces
Source0: hos-add.if
Source1: hos-auth.if
Source2: hos-bind.if
Source3: hos-can.if
Source4: hos-corecmd.if
Source5: hos-create.if
Source6: hos-delete.if
Source7: hos-dev.if
Source8: hos-domain.if
Source9: hos-exec.if
Source10: hos-files.if
Source11: hos-fs.if
Source12: hos-getty.if
Source13: hos-gnome.if
Source14: hos-init.if
Source15: hos-kernel.if
Source16: hos-list.if
Source17: hos-logging.if
Source18: hos-manage.if
Source19: hos-miscfiles.if
Source20: hos-mmap.if
Source21: hos-mozilla.if
Source22: hos-objpermsets.if
Source23: hos-ps.if
Source24: hos-read.if
Source25: hos-r.if
Source26: hos-rw.if
Source27: hos-selinux.if
Source28: hos-seutil.if
Source29: hos-snapper.if
Source30: hos-sysnetwork.if
Source31: hos-systemd.if
Source32: hos-term.if
Source33: hos-thumb.if
Source34: hos-udev.if
Source35: hos-userdom.if
Source36: hos-virt.if
Source37: hos-xserver.if
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

%files
%{_contribdir}/hos-*.if
