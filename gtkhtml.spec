Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Summary(pt_BR):	Biblioteca gtkhtml
Summary(ru):	GtkHTML - ÜÔÏ ÂÉÂÌÉÏÔÅËÁ ÒÅÎÄÅÒÉÎÇÁ/ÒÅÄÁËÔÉÒÏ×ÁÎÉÑ HTML
Summary(uk):	GtkHTML - ÃÅ Â¦ÂÌ¦ÏÔÅËÁ ÒÅÎÄÅÒÉÎÇÕ/ÒÅÄÁÇÕ×ÁÎÎÑ HTML
Name:		gtkhtml
Version:	1.0.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gtkhtml/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pixmap.patch
Patch2:		%{name}-%{name}-stream.h.patch
Patch3:		%{name}-get_default_fonts.patch
BuildRequires:	GConf-devel
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.9
BuildRequires:	control-center-devel
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	intltool
BuildRequires:	libghttp-devel >= 1.0
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkhtml20

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

%description -l pt_BR
Este é o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru
üÔÏ GtkHTML, ÌÅÇËÉÊ "Ä×ÉÖÏË" ÒÅÎÄÅÒÉÎÇÁ/ÐÅÞÁÔÉ/ÒÅÄÁËÔÉÒÏ×ÁÎÉÑ HTML.
óÎÁÞÁÌÁ ÏÎ ÂÁÚÉÒÏ×ÁÌÓÑ ÎÁ KHTMLW, ÎÏ ÔÅÐÅÒØ ÒÁÚÒÁÂÁÔÙ×ÁÅÔÓÑ
ÎÅÚÁ×ÉÓÉÍÏ.

%description -l uk
ãÅ GtkHTML, ÌÅÇËÅ ÑÄÒÏ ÒÅÎÄÅÒÉÎÇÕ/ÄÒÕËÕ/ÒÅÄÁÇÕ×ÁÎÎÑ HTML. ÷ÏÎÏ
ÓÐÏÞÁÔËÕ ÂÁÚÕ×ÁÌÏÓØ ÎÁ KHTMLW, ÁÌÅ ÔÅÐÅÒ ÒÏÚÒÏÂÌÑ¤ÔØÓÑ ÎÅÚÁÌÅÖÎÏ ×¦Ä
ÎØÏÇÏ.

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(es):	Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl):	Pliki nag³ówkowe i inne nizbêdne do tworzenia aplikacji u¿ywaj±cych gtkhtml
Summary(pt_BR):	Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações gtkhtml
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ gtkhtml
Summary(uk):	æÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ gtkhtml
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	bonobo-devel
Requires:	gal-devel
Requires:	gdk-pixbuf-devel
Requires:	gnome-print-devel >= 0.29
Requires:	libglade-devel
Requires:	libunicode-devel
Obsoletes:	lubgtkhtml20-devel

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel -l es
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl
Pliki nag³ówkowe i reszta niezbêdnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
gtkhtml.

%description devel -l ru
æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ gtkhtml.

%description devel -l uk
æÁÊÌÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es):	Bibliotecas estáticas para desarrollar aplicaciones gtkhtml
Summary(pl):	Biblioteki statyczne gtkhtml
Summary(pt_BR):	Bibliotecas estáticas para desenvolver aplicações gtkhtml
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ Ó gtkhtml
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ Ú gtkhtml
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%description static -l es
Bibliotecas estáticas para desarrollar aplicaciones gtkhtml.

%description static -l pl
Biblioteki statyczne gtkhtml.

%description static -l pt_BR
Bibliotecas estáticas para desenvolver aplicações gtkhtml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
xml-i18n-toolize --force
aclocal -I macros
autoconf
automake -a -c -f
GNOME_LIBCONFIG_PATH=/usr/lib
export GNOME_LIBCONFIG_PATH

%configure \
	--with-bonobo \
	--with-gconf

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
%attr(755,root,root) %{_libdir}/bonobo/plugin/lib*.so
%dir %{_datadir}/gtkhtml
%{_datadir}/gtkhtml/icons
%{_datadir}/gtkhtml/keybindingsrc*
%{_datadir}/gtkhtml/*.glade
%{_datadir}/control-center/Documents
#%{_datadir}/control-center/capplets
%{_datadir}/gnome/ui/*
%{_datadir}/oaf/*.oaf
%{_applnkdir}/Settings/GNOME/Documents
%{_sysconfdir}/CORBA/servers/html-component.gnorba
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/bonobo/plugin/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*
%{_datadir}/gtkhtml/*.idl
%{_datadir}/gnome/html*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/bonobo/plugin/lib*.a
