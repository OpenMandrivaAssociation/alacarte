Summary:	Simple menu editor for Gnome
Name:		alacarte
Version:	0.13.2
Release:	5
Group:		System/Configuration/Other
License:	LGPLv2+
URL:		http://www.realistanew.com/projects/alacarte/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(pygtk-2.0)

Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	gnome-python
Requires:	python-gnome-menus

%description
Alacarte is a menu editor for GNOME that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q -a1

%build
%configure2_5x \
	--prefix=%{_prefix} \
	--libdir=%{_prefix}/lib

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
	--add-category="GNOME" \
	--add-category="X-MandrivaLinux-System-Configuration-Other" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

install -D -m 644 %{name}48.png %{buildroot}/%{_liconsdir}/%{name}.png
install -D -m 644 %{name}32.png %{buildroot}/%{_iconsdir}/%{name}.png
install -D -m 644 %{name}16.png %{buildroot}/%{_miconsdir}/%{name}.png

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING
%{py_puresitedir}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/*/%{name}.png
%{_iconsdir}/%{name}.png

