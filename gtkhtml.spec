Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Name:		gtkhtml
Version:	0.8
Release:	2
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gtkhtml/%{name}-%{version}.tar.gz
BuildRequires:	ORBit-devel
#BuildRequires:	bonobo-devel >= 0.9
BuildRequires:	gal-devel >= 0.4.1
BuildRequires:	gdk-pixbuf-devel >= 0.6.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl
GtkHTML jesrt "lekk�" bibilotek� do renderingu, drukowania i edycji HTML.
Pierwotne �r�d�a tej biblioteki bazuj� na KHTMLW ale teraz GtkHTML jest
rozwijana niezale�nie od KHTMLW,
 
%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(pl):	Pliki nag��wkowe i inne nizb�dne do tworzenia aplikacji u�ywaj�cych gtkhtml
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel
Pliki nag��wkowe i reszta niezb�dnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(pl):	Biblioteki statyczne gtkhtml
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%description -l pl static
Biblioteki statyczne gtkhtml.

%prep
%setup -q

%build
%configure \
	--without-bonobo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install components/html-editor/*.idl $RPM_BUILD_ROOT/%{_datadir}/gtkhtml

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
#%{_sysconfdir}/CORBA/servers/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_datadir}/gtkhtml

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
