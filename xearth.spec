Summary:	An X display of the Earth from space
Name:		xearth
Version:	1.1
Release:	15mdk
License:	MIT
Group:		Toys
BuildRequires:	XFree86-devel X11
Source0:	ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.bz2
Source1:	xearth_locations.txt.bz2
Source11:	xearth16.png
Source12:	xearth32.png
Source13:	xearth48.png
Url:		http://www.cs.colorado.edu/~tuna/xearth/
Patch0:		xearth-1.0-mdk.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xearth is an X Window System based graphic that shows a globe of the
Earth, including markers for major cities and MandrakeSoft.  The
Earth is correctly shaded for the current position of the sun, and the
displayed image is updated every five minutes.

%prep
%setup -q
%patch0 -p0

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std} install.man
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xearth
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_datadir}/xearth/xearth_locations.txt

#install menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF >$RPM_BUILD_ROOT%{_menudir}/%{name}
?package(xearth): needs="gnome" icon="xearth.png" section="Amusement/Toys" \
title="Xearth" longtitle="Display the Earth on your desktop" \
command="xearth -noroot -bigstars 20 -label -labelpos -5-150 -markerfile /usr/share/xearth/xearth_locations.txt"
?package(xearth): needs="X11" icon="xearth.png" section="Amusement/Toys" \
title="Xearth" longtitle="Display the Earth on your desktop" \
command="xearth -bigstars 20 -label -labelpos -5-150 -markerfile /usr/share/xearth/xearth_locations.txt"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xearth
/usr/X11R6/man/man1/xearth.1x*
/usr/X11R6/lib/X11/doc/html/xearth.1.html
%{_datadir}/xearth/xearth_locations.txt
%{_miconsdir}/xearth.png
%{_iconsdir}/xearth.png
%{_liconsdir}/xearth.png
%{_menudir}/xearth

