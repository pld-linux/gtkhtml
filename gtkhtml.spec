Summary:	gtkhtml library
Name:		gtkhtml
Version:	0.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gtkhtml/%{name}-%{version}.tar.gz
BuildRequires:	w3c-libwww-devel
BuildRequires:	bonobo-devel >= 0.9
BuildRequires:	gnome-print-devel >= 0.13
BuildRequires:	gdk-pixbuf-devel >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, but is now being developed independently of
it.

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%package static
Summary:	Static gtkhtml libraries
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-bonobo

make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_sysconfdir}/CORBA/servers/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
