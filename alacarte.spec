Name:           alacarte
Version:        0.11.3
Release:        %mkrel 3
Summary:        Simple menu editor for Gnome

Group:          System/Configuration/Other
License:        GPL
URL:            http://www.realistanew.com/projects/alacarte/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%name-icons.tar.bz2
BuildArch:      noarch

BuildRequires:  pygtk2.0-devel
BuildRequires: 	desktop-file-utils
BuildRequires:  gnome-menus-devel >= 2.15.4.1
BuildRequires:  perl-XML-Parser
Requires: 	pygtk2.0, gnome-python-gconf, gnome-python
Requires: 	python-gnome-menus
Obsoletes:      smeg
Provides:       smeg = %{version}-%{release}

%description
Alacarte is a menu editor for GNOME that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q -a1

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name --with-gnome

# move from /usr/lib to /usr/lib
%if %_lib != lib
mkdir -p %buildroot%_prefix/lib
mv %buildroot%_libdir/python* %buildroot%_prefix/lib
%endif

desktop-file-install --vendor="" \
  --add-category="GNOME" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING
%py_puresitedir/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%name/*
%{_datadir}/icons/*
%{_iconsdir}/*/%name.png
%{_iconsdir}/%name.png


