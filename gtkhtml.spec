Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Name:		gtkhtml
Version:	0.15.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gtkhtml/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pixmap.patch
Patch2:		%{name}-gtkhtml-stream.h.patch
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.9
BuildRequires:	control-center-devel
BuildRequires:	gal-devel >= 0.11.2
BuildRequires:	gdk-pixbuf-devel >= 0.6.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.13
BuildRequires:	libghttp-devel >= 1.0
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl
GtkHTML jesrt "lekk±" bibilotek± do renderingu, drukowania i edycji
HTML. Pierwotne ¼ród³a tej biblioteki bazuj± na KHTMLW ale teraz
GtkHTML jest rozwijana niezale¿nie od KHTMLW,

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(pl):	Pliki nag³ówkowe i inne nizbêdne do tworzenia aplikacji u¿ywaj±cych gtkhtml
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}
Requires:	gnome-print-devel >= 0.13

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel
Pliki nag³ówkowe i reszta niezbêdnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(pl):	Biblioteki statyczne gtkhtml
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%description -l pl static
Biblioteki statyczne gtkhtml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
GNOME_LIBCONFIG_PATH=/usr/lib
export GNOME_LIBCONFIG_PATH
%configure \
	--without-bonobo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_applnkdir}/Settings/GNOME/Documents
	
install components/html-editor/*.idl $RPM_BUILD_ROOT%{_datadir}/gtkhtml

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/control-center/Documents
%{_applnkdir}/Settings/GNOME/Documents
%dir %{_datadir}/gtkhtml
%{_datadir}/gtkhtml/icons
%{_datadir}/gtkhtml/keybindingsrc*
%{_datadir}/gtkhtml/*.glade
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_datadir}/gtkhtml/*.idl

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
