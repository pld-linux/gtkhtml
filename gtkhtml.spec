Summary:	Gtkhtml library
Summary(pl):	Biblioteka gtkhtml
Summary(pt_BR):	Biblioteca gtkhtml
Summary(ru):	GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk):	GtkHTML - це б╕бл╕отека рендерингу/редагування HTML
Summary(zh_CN):	gtkhtml ©Б
Name:		gtkhtml
Version:	3.7.5
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtkhtml/3.7/%{name}-%{version}.tar.bz2
# Source0-md5:	729330ab9fbf27245372d490711d3799
Patch0:		%{name}-pixmap.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-crash.patch
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.8.3
BuildRequires:	gal-devel >= 1:2.5.3
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-icon-theme >= 2.10.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libsoup-devel >= 2.2.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gal >= 1:2.5.3
Requires:	gnome-icon-theme >= 2.10.0
Requires:	gtk+2 >= 2:2.6.4
Obsoletes:	libgtkhtml20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl
GtkHTML jest "lekk╠" bibliotek╠ do renderingu, drukowania i edycji
HTML. Pierwotne ╪rСdЁa tej biblioteki bazuj╠ na KHTMLW ale teraz
GtkHTML jest rozwijana niezale©nie od KHTMLW.

%description -l pt_BR
Este И o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru
Это GtkHTML, легкий "движок" рендеринга/печати/редактирования HTML.
Сначала он базировался на KHTMLW, но теперь разрабатывается
независимо.

%description -l uk
Це GtkHTML, легке ядро рендерингу/друку/редагування HTML. Воно
спочатку базувалось на KHTMLW, але тепер розробля╓ться незалежно в╕д
нього.

%package devel
Summary:	Header files etc. neccessary to develop gtkhtml applications
Summary(es):	Bibliotecas, archivos de inclusiСn, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl):	Pliki nagЁСwkowe i inne niezbЙdne do tworzenia aplikacji u©ywaj╠cych gtkhtml
Summary(pt_BR):	Bibliotecas, arquivos de inclusЦo, e etc para desenvolver aplicaГУes gtkhtml
Summary(ru):	Файлы, необходимые для разработки программ с использованием gtkhtml
Summary(uk):	Файли, необх╕дн╕ для розробки програм з використанням gtkhtml
Summary(zh_CN):	gtkhtml©╙╥╒©Б
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.8.3
Requires:	gal-devel >= 1:2.4.2
Requires:	libgnomeprintui-devel >= 2.10.2
Requires:	libgnomeui-devel >= 2.10.0-2
Obsoletes:	libgtkhtml20-devel

%description devel
Header files etc. neccessary to develop gtkhtml applications.

%description devel -l es
Bibliotecas, archivos de inclusiСn, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl
Pliki nagЁСwkowe i reszta niezbЙdnych przy tworzeniu aplikacji
wykorzystuj╠cych gtkhtml.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusЦo, e etc para desenvolver aplicaГУes
gtkhtml.

%description devel -l ru
Файлы, необходимые для разработки программ с использованием gtkhtml.

%description devel -l uk
Файли, необх╕дн╕ для розробки програм з використанням gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es):	Bibliotecas estАticas para desarrollar aplicaciones gtkhtml
Summary(pl):	Biblioteki statyczne gtkhtml
Summary(pt_BR):	Bibliotecas estАticas para desenvolver aplicaГУes gtkhtml
Summary(ru):	Статические библиотеки для разработки программ с gtkhtml
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм з gtkhtml
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtkhtml libraries.

%description static -l es
Bibliotecas estАticas para desarrollar aplicaciones gtkhtml.

%description static -l pl
Biblioteki statyczne gtkhtml.

%description static -l pt_BR
Bibliotecas estАticas para desenvolver aplicaГУes gtkhtml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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
	pkgconfigdir=%{_pkgconfigdir} \
	idldir=%{_datadir}/idl

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}-3.8
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_datadir}/idl/*.idl
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
