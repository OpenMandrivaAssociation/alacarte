Summary:	Simple menu editor for Gnome
Name:		alacarte
Version:        3.11.91
Release:	1
Group:		System/Configuration/Other
License:	LGPLv2+
URL:		http://www.realistanew.com/projects/alacarte/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  python3
BuildRequires:  pkgconfig(python3)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:  intltool
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  docbook-style-xsl

Requires:	typelib(GMenu) = 3.0
Requires:	typelib(Gtk) = 3.0

BuildArch:	noarch

%description
Alacarte is a menu editor for GNOME that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q 

autoreconf -i -f

%build
%configure 
%make

%install
%makeinstall_std

sed -i -e 's/NotShowIn=KDE;/OnlyShowIn=GNOME;/' \
  %{buildroot}%{_datadir}/applications/alacarte.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/alacarte.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README AUTHORS COPYING
%{py_puresitedir}/Alacarte
%{_bindir}/alacarte
%{_datadir}/applications/alacarte.desktop
%{_datadir}/alacarte
%{_datadir}/icons/hicolor/16x16/apps/alacarte.png
%{_datadir}/icons/hicolor/22x22/apps/alacarte.png
%{_datadir}/icons/hicolor/24x24/apps/alacarte.png
%{_datadir}/icons/hicolor/32x32/apps/alacarte.png
%{_datadir}/icons/hicolor/48x48/apps/alacarte.png
%{_datadir}/icons/hicolor/256x256/apps/alacarte.png
%{_mandir}/man1/alacarte.1.*

