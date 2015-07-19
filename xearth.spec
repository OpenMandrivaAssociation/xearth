%define name	xearth
%define version	1.1

Summary:	A display of the Earth from space
Name:		%{name}
Version:	%{version}
Release:	30
License:	MIT
Group:		Toys
BuildRequires:	pkgconfig(x11) libxext-devel libxt-devel imake
Source0:	ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.bz2
Source1:	xearth_locations.txt.bz2
Source11:	xearth16.png
Source12:	xearth32.png
Source13:	xearth48.png
Url:		http://www.cs.colorado.edu/~tuna/xearth/
Patch0:		xearth-1.0-mdk.patch

%description
Xearth is a graphic that shows a globe of the Earth, including markers 
for major cities and the Mandriva head office.  The Earth is correctly 
shaded for the current position of the sun, and the displayed image is 
updated every five minutes.

%prep
%setup -q
%patch0 -p0

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std} install.man
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/%{name}/xearth_locations.txt

#install menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xearth
Comment=Display the Earth on your desktop
Exec=%{_bindir}/%{name} -noroot -bigstars 20 -label -labelpos -5-150 -markerfile /usr/share/xearth/xearth_locations.txt
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Amusement;X-MandrivaLinux-MoreApplications-Games-Toys;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/xearth.1*
%{_datadir}/%{name}/xearth_locations.txt
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-20mdv2011.0
+ Revision: 671302
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-19mdv2011.0
+ Revision: 608201
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-18mdv2010.1
+ Revision: 524437
- rebuilt for 2010.1

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.1-17mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-17mdv2008.1
+ Revision: 179511
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
    - fix man pages extension

* Sat Jun 16 2007 Adam Williamson <awilliamson@mandriva.org> 1.1-16mdv2008.0
+ Revision: 40280
- XDG menu; fd.o icons; trim buildrequires; new X layout; rebuild for new era


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.1-15mdk
- Rebuild

* Thu Dec 23 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.1-14mdk
- fix buildrequires
- cosmetics

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1-13mdk
- rebuild
- use %%make macro
- cosmetics

* Mon Jan 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-12mdk
- build release

* Mon Feb 11 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-11mdk
- xpm -> png icons
- sanitize spec file

* Tue Oct 30 2001 Sebastien Dupont <sdupont@mandrakesoft.com> 1.1-10mdk
- url tag

* Fri Oct 19 2001 Sebastien Dupont <sdupont@mandrakesoft.com> 1.1-9mdk
- Lisence.

* Thu Apr 12 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1-8mdk
- Disable root windows under GNOME (don't work with Nautilus yet)
- Clean specfile

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1-7mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-6mdk
- fix buildroot

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-5mdk
- use new macros

* Fri Apr 28 2000 DindinX <odin@mandrakesoft.com> 1.1-4mdk
- Added 32x32 and 48x48 icons

* Fri Apr 28 2000 DindinX <odin@mandrakesoft.com> 1.1-3mdk
- remove menu icon path

* Wed Apr 26 2000 DindinX <odin@mandrakesoft.com> 1.1-2mdk
- added an icon for the menu

* Wed Apr 05 2000 DindinX <odin@mandrakesoft.com> 1.1-1mdk
- New version
- Added menu
- Use a more complete markerfile

* Sat Mar 25 2000 Dindinx <odin@mandrakesoft.com> 1.0-6mdk
- Use spec-helper
- Fix group

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Wed Jul 28 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- remove unuseful patch
- add MandrakeSoft home on map
- add french translation
- fix english description

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

