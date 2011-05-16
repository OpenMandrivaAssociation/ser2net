Summary:	Serial to network proxy
Name:		ser2net
Version:	2.7
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Servers
Source0:	http://dl.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
Source1:	ser2net.init
URL:		http://ser2net.sourceforge.net/
BuildRequires:	libwrap-devel
Requires(pre):		rpm-helper
Requires(preun):	rpm-helper

%description
Make serial ports available to network via TCP/IP connection.

%prep
%setup -q

%build
%configure2_5x --with-tcp-wrappers
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{__install} -Dpm644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}.conf
%{__install} -Dpm755 %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

%clean
rm -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_sbindir}/ser2net
%{_mandir}/man8/ser2net.8*
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
