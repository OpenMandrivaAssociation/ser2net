Summary:	Serial to network proxy
Name:		ser2net
Version:	2.9.1
Release:	1
License:	GPLv2+
Group:		System/Servers
Source0:	http://dl.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
Source1:	ser2net.service
URL:		http://ser2net.sourceforge.net/
BuildRequires:	libwrap-devel

%description
Make serial ports available to network via TCP/IP connection.

%prep
%setup -q

%build
%configure2_5x --with-tcp-wrappers
%make

%install
%makeinstall_std

%{__install} -Dpm644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}.conf
%{__install} -Dpm755 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

%post
%systemd_post ser2net.service

%preun
%systemd_preun ser2net.service

%postun
%systemd_postun_with_restart ser2net.service

%files
%doc AUTHORS ChangeLog NEWS README
%{_sbindir}/ser2net
%{_mandir}/man8/ser2net.8*
%{_unitdir}/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf


