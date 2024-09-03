Summary:	USB hub per-port power control
Name:		uhubctl
Version:	2.6.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/mvp/uhubctl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	61d0aaec37d9c121b59f824782e26f04
URL:		https://github.com/mvp/uhubctl
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uhubctl is utility to control USB power per-port on smart USB hubs.
Smart hub is defined as one that implements per-port power switching.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags}" \
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	GIT_VERSION="%{version}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sbindir="%{_sbindir}" \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_sbindir}/uhubctl
