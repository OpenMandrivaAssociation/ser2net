Summary: Serial to network proxy
Summary(pl.UTF-8): Proxy między portem szeregowym a siecią
Summary(ru.UTF-8): Параллельный порт поверх IP сети
Name: ser2net
Version: 2.7
Release: %mkrel 1
License: GPL v2+
Group: Networking/Daemons
Source0: http://dl.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
Source1: ser2net.init
URL: http://ser2net.sourceforge.net/
BuildRequires: autoconf, automake, libtool, libwrap-devel
BuildRoot: %{tmpdir}/%{name}-%{version}

%description
Make serial ports available to network via TCP/IP connection.

%description -l pl.UTF-8
Program udostępniający porty szeregowe przez połączenie TCP/IP.

%description -l ru.UTF-8
Данная программа позволяет предоставить доступ к параллельному порту (COM) через IP сеть.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --with-tcp-wrappers
%make

%install
rm -rf %{buildroot}
%{__install} -d %{buildroot}/%{_sysconfdir}

%makeinstall

%{__install} %{name}.conf %{buildroot}/%{_sysconfdir}
%{__install} -d %{buildroot}/%{_sysconfdir}/etc/rc.d/init.d
%{__install} -Dpm755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/init.d/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/ser2net
%attr(755,root,root) %{_sysconfdir}/init.d/%{name}
%{_mandir}/man8/ser2net.8*
%config(noreplace) %{_sysconfdir}/%{name}.conf
