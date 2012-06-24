%define		mver		1.1
%define		subver		6

Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Summary(pt_BR):	Biblioteca gtkhtml
Summary(ru):	GtkHTML - ��� ���������� ����������/�������������� HTML
Summary(uk):	GtkHTML - �� ¦�̦����� ����������/����������� HTML
Summary(zh_CN): gtkhtml ��
Name:		gtkhtml
Version:	%{mver}.%{subver}
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/mirror/gnome.org/sources/gtkhtml/%{mver}/%{name}-%{version}.tar.bz2
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
BuildRequires:	gal-devel >= 0.21
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.8.0
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.29
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libghttp-devel >= 1.0
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgtkhtml20

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl
GtkHTML jesrt "lekk�" bibilotek� do renderingu, drukowania i edycji
HTML. Pierwotne �r�d�a tej biblioteki bazuj� na KHTMLW ale teraz
GtkHTML jest rozwijana niezale�nie od KHTMLW,

%description -l pt_BR
Este � o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru
��� GtkHTML, ������ "������" ����������/������/�������������� HTML.
������� �� ����������� �� KHTMLW, �� ������ ���������������
����������.

%description -l uk
�� GtkHTML, ����� ���� ����������/�����/����������� HTML. ����
�������� ���������� �� KHTMLW, ��� ����� �������Ѥ���� ��������� צ�
�����.

%package devel
Summary:	Header files and etc neccessary to develop gtkhtml applications
Summary(es):	Bibliotecas, archivos de inclusi�n, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl):	Pliki nag��wkowe i inne nizb�dne do tworzenia aplikacji u�ywaj�cych gtkhtml
Summary(pt_BR):	Bibliotecas, arquivos de inclus�o, e etc para desenvolver aplica��es gtkhtml
Summary(ru):	�����, ����������� ��� ���������� �������� � �������������� gtkhtml
Summary(uk):	�����, ����Ȧ�Φ ��� �������� ������� � ������������� gtkhtml
Summary(zh_CN): gtkhtml������
Group:		X11/Libraries
Requires:	%{name} = %{version}
Requires:	bonobo-devel
Requires:	gal-devel
Requires:	gdk-pixbuf-gnome-devel
Requires:	gnome-print-devel >= 0.29
Requires:	gtk-doc-common
Requires:	libglade-gnome-devel
Requires:	libunicode-devel
Obsoletes:	lubgtkhtml20-devel

%description devel
Header files and etc neccessary to develop gtkhtml applications.

%description devel -l es
Bibliotecas, archivos de inclusi�n, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl
Pliki nag��wkowe i reszta niezb�dnych przy tworzeniu aplikacji
wykorzystujacych gtkhtml.

%description devel -l pt_BR
Bibliotecas, arquivos de inclus�o, e etc para desenvolver aplica��es
gtkhtml.

%description devel -l ru
�����, ����������� ��� ���������� �������� � �������������� gtkhtml.

%description devel -l uk
�����, ����Ȧ�Φ ��� �������� ������� � ������������� gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es):	Bibliotecas est�ticas para desarrollar aplicaciones gtkhtml
Summary(pl):	Biblioteki statyczne gtkhtml
Summary(pt_BR):	Bibliotecas est�ticas para desenvolver aplica��es gtkhtml
Summary(ru):	����������� ���������� ��� ���������� �������� � gtkhtml
Summary(uk):	������Φ ¦�̦����� ��� �������� ������� � gtkhtml
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static gtkhtml libraries.

%description static -l es
Bibliotecas est�ticas para desarrollar aplicaciones gtkhtml.

%description static -l pl
Biblioteki statyczne gtkhtml.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolver aplica��es gtkhtml.

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
%{__libtoolize}
xml-i18n-toolize --force
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
GNOME_LIBCONFIG_PATH=/usr/lib
export GNOME_LIBCONFIG_PATH

%configure \
	--with-bonobo \
	--with-gconf

%{__make} \
	idldir=%{_datadir}/idl \
	pkgconfigdir=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_applnkdir}/Settings/GNOME/Documents \
	pkgconfigdir=%{_pkgconfigdir} \
	idldir=%{_datadir}/idl \
	HTML_DIR=%{_gtkdocdir}
	
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/plugin/lib*.so
%dir %{_datadir}/gtkhtml-%{mver}
%{_datadir}/gtkhtml-%{mver}/icons
%{_datadir}/gtkhtml-%{mver}/keybindingsrc*
%{_datadir}/gtkhtml-%{mver}/*.glade
%{_datadir}/control-center/Documents/*
%{_datadir}/gnome/ui/*
%{_datadir}/oaf/*.oaf
%{_applnkdir}/Settings/GNOME/Documents/*
%{_pixmapsdir}/*
%{_pkgconfigdir}/*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/bonobo/plugin/lib*.la
%{_includedir}/*
%{_datadir}/idl/*.idl
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/bonobo/plugin/lib*.a
