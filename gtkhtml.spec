%define ver      0.1
%define prefix   /usr

Summary: gtkhtml library
Name: gtkhtml
Version: %ver
Release: 1
Copyright: LGPL
Group: X11/Libraries
Source: ftp://ftp.gnome.org/pub/GNOME/sources/gtkhtml/gtkhtml-%{ver}.tar.gz
BuildRoot: /var/tmp/gtkhtml-%{PACKAGE_VERSION}-root
Provides: gtkhtml.so.0

Docdir: %{prefix}/doc

%description
This is GtkHTML, a lightweight HTML rendering/printing/editing engine.
It was originally based on KHTMLW, but is now being developed
independently of it.

%package devel
Summary: Libraries, includes, etc to develop gtkhtml applications
Group: X11/libraries
Requires: gtkhtml

%description devel
Libraries, include files, etc you can use to develop gtkhtml applications.




%prep
%setup

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --host=alpha-redhat-linux --prefix=%prefix --sysconfdir="/etc" --with-bonobo
%else
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --sysconfdir="/etc" --with-bonobo
%endif
else
%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-redhat-linux --prefix=%prefix --sysconfdir="/etc" --with-bonobo
%else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir="/etc" --with-
%endif
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

# Note how DESTDIR is passed. Using prefix=$RPM_BUILD_ROOT%{prefix} instaead
# nearly worked, but problems occured for /etc/CORBA/servers, where prefix
# was ignored completely.
make -k DESTDIR=$RPM_BUILD_ROOT prefix=%{prefix} install


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING TODO
%{prefix}/lib/lib*.so.*

# /etc/CORBA/servers/*

%files devel
%defattr(-, root, root)

%{prefix}/lib/lib*.so
%{prefix}/lib/*a
%{prefix}/lib/*.sh
%{prefix}/include/*
