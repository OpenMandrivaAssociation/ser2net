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


%changelog
* Mon May 16 2011 Jani Välimaa <wally@mandriva.org> 2.7-2mdv2011.0
+ Revision: 675031
- clean .spec
- add post and preun for service
- clean init file (make rpmlint happy)

* Tue Nov 30 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.7-1mdv2011.0
+ Revision: 603622
- Fixed group.

  + zamir <zamir@mandriva.org>
    - first build
    - Created package structure for ser2net.

