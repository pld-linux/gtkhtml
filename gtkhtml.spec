Summary:	Gtkhtml library
Summary(pl.UTF-8):	Biblioteka gtkhtml
Summary(pt_BR.UTF-8):	Biblioteca gtkhtml
Summary(ru.UTF-8):	GtkHTML - это библиотека рендеринга/редактирования HTML
Summary(uk.UTF-8):	GtkHTML - це бібліотека рендерингу/редагування HTML
Summary(zh_CN.UTF-8):	gtkhtml 库
Name:		gtkhtml
Version:	3.16.1
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkhtml/3.16/%{name}-%{version}.tar.bz2
# Source0-md5:	71d2d115e3629a634e115b8c0b0fd5b5
Patch0:		%{name}-pixmap.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-crash.patch
BuildRequires:	ORBit2-devel >= 1:2.14.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.20.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-icon-theme >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonoboui-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libsoup-devel >= 2.2.100
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gnome-icon-theme >= 2.20.0
Requires:	gtk+2 >= 2:2.12.0
Requires:	libgnomeui >= 2.20.0
Obsoletes:	gal
Obsoletes:	libgtkhtml20
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%description -l pl.UTF-8
GtkHTML jest "lekką" biblioteką do renderingu, drukowania i edycji
HTML. Pierwotne źródła tej biblioteki bazują na KHTMLW ale teraz
GtkHTML jest rozwijana niezależnie od KHTMLW.

%description -l pt_BR.UTF-8
Este é o GtkHTML, uma ferramenta de renderizar/imprimir/editar HTML
leve e pequeno

%description -l ru.UTF-8
Это GtkHTML, легкий "движок" рендеринга/печати/редактирования HTML.
Сначала он базировался на KHTMLW, но теперь разрабатывается
независимо.

%description -l uk.UTF-8
Це GtkHTML, легке ядро рендерингу/друку/редагування HTML. Воно
спочатку базувалось на KHTMLW, але тепер розробляється незалежно від
нього.

%package devel
Summary:	Header files etc. neccessary to develop gtkhtml applications
Summary(es.UTF-8):	Bibliotecas, archivos de inclusión, e etc. para desarrollar aplicaciones gtkhtml
Summary(pl.UTF-8):	Pliki nagłówkowe i inne niezbędne do tworzenia aplikacji używających gtkhtml
Summary(pt_BR.UTF-8):	Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações gtkhtml
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ с использованием gtkhtml
Summary(uk.UTF-8):	Файли, необхідні для розробки програм з використанням gtkhtml
Summary(zh_CN.UTF-8):	gtkhtml开发库
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.20.0
Requires:	libgnomeui-devel >= 2.20.0
Obsoletes:	gal-devel
Obsoletes:	libgtkhtml20-devel

%description devel
Header files etc. neccessary to develop gtkhtml applications.

%description devel -l es.UTF-8
Bibliotecas, archivos de inclusión, y etc para desarrollar
aplicaciones gtkhtml.

%description devel -l pl.UTF-8
Pliki nagłówkowe i reszta niezbędnych przy tworzeniu aplikacji
wykorzystujących gtkhtml.

%description devel -l pt_BR.UTF-8
Bibliotecas, arquivos de inclusão, e etc para desenvolver aplicações
gtkhtml.

%description devel -l ru.UTF-8
Файлы, необходимые для разработки программ с использованием gtkhtml.

%description devel -l uk.UTF-8
Файли, необхідні для розробки програм з використанням gtkhtml.

%package static
Summary:	Static gtkhtml libraries
Summary(es.UTF-8):	Bibliotecas estáticas para desarrollar aplicaciones gtkhtml
Summary(pl.UTF-8):	Biblioteki statyczne gtkhtml
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolver aplicações gtkhtml
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с gtkhtml
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з gtkhtml
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gal-static

%description static
Static gtkhtml libraries.

%description static -l es.UTF-8
Bibliotecas estáticas para desarrollar aplicaciones gtkhtml.

%description static -l pl.UTF-8
Biblioteki statyczne gtkhtml.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolver aplicações gtkhtml.

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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libgnome-gtkhtml-editor-3.14.so
%{_libdir}/bonobo/servers/GNOME_GtkHTML_Editor-3.14.server
%{_datadir}/%{name}-3.14
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtml-3.14.so
%{_libdir}/libgtkhtml-3.14.la
%{_includedir}/libgtkhtml-3.14
%{_datadir}/idl/Editor.idl
%{_pkgconfigdir}/libgtkhtml-3.14.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtml-3.14.a
