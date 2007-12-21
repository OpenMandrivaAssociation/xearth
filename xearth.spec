%define name	xearth
%define version	1.1
%define release	%mkrel 16

Summary:	A display of the Earth from space
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Toys
BuildRequires:	libx11-devel libxext-devel libxt-devel imake
Source0:	ftp://cag.lcs.mit.edu/pub/tuna/%{name}-%{version}.tar.bz2
Source1:	xearth_locations.txt.bz2
Source11:	xearth16.png
Source12:	xearth32.png
Source13:	xearth48.png
Url:		http://www.cs.colorado.edu/~tuna/xearth/
Patch0:		xearth-1.0-mdk.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

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

