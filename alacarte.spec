Summary:	Simple menu editor for Gnome
Name:		alacarte
Version:	0.13.3
Release:	1
Group:		System/Configuration/Other
License:	LGPLv2+
URL:		http://www.realistanew.com/projects/alacarte/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
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



%changelog
* Mon May 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.13.3-1
+ Revision: 800983
- version update 0.13.3

* Fri Mar 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.13.2-5
+ Revision: 785404
- rebuild
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.13.2-4
+ Revision: 662757
- mass rebuild

* Sun Nov 21 2010 Jani Välimaa <wally@mandriva.org> 0.13.2-3mdv2011.0
+ Revision: 599589
- fix file list
  - own unowned data dir
  - don't own icon dirs

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.13.2-2mdv2011.0
+ Revision: 590148
- rebuild for python 2.7

* Wed Sep 15 2010 Götz Waschk <waschk@mandriva.org> 0.13.2-1mdv2011.0
+ Revision: 578496
- update to new version 0.13.2

* Sun Apr 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.13.1-1mdv2010.1
+ Revision: 531219
- use %%configure2_5x
- update to 0.13.1

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.4-2mdv2010.1
+ Revision: 521935
- rebuilt for 2010.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 0.12.4-1mdv2010.0
+ Revision: 446552
- update to new version 0.12.4

* Fri Sep 11 2009 Götz Waschk <waschk@mandriva.org> 0.12.3-1mdv2010.0
+ Revision: 437892
- new version
- update gnome-menus dep

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2010.0
+ Revision: 371818
- update to new version 0.12.1

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2010.0
+ Revision: 371793
- update to new version 0.12.0

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 0.11.10-1mdv2009.1
+ Revision: 356643
- update to new version 0.11.10

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 0.11.9-1mdv2009.1
+ Revision: 340897
- update to new version 0.11.9

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 0.11.8-1mdv2009.1
+ Revision: 336522
- update to new version 0.11.8

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 0.11.7-1mdv2009.1
+ Revision: 331286
- update to new version 0.11.7

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.11.6-2mdv2009.1
+ Revision: 318559
- rebuild for new python

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 0.11.6-1mdv2009.0
+ Revision: 287290
- new version
- fix license
- cleanup build deps

* Tue Jul 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.11.5-3mdv2009.0
+ Revision: 252942
- fix deps pkg-config/pkgconfig
- fix deps
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.11.5-2mdv2009.0
+ Revision: 220347
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 11 2008 Götz Waschk <waschk@mandriva.org> 0.11.5-1mdv2008.1
+ Revision: 185003
- new version

* Sun Feb 17 2008 Götz Waschk <waschk@mandriva.org> 0.11.4-1mdv2008.1
+ Revision: 169928
- fix installation
- new version

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.11.3-4mdv2008.1
+ Revision: 148441
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 02 2007 Funda Wang <fwang@mandriva.org> 0.11.3-3mdv2008.0
+ Revision: 94724
- fix provides

* Sun Sep 16 2007 Emmanuel Andry <eandry@mandriva.org> 0.11.3-2mdv2008.0
+ Revision: 88611
- drop old menu

