%define	name	fvwm-icons
%define	version	1.0
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	FVWM icons
URL: 		http://www.fvwm.org/
Source:     http://www.fvwm.org/generated/icon_download/fvwm_icons.tar.bz2
License:	GPL
Group:		Graphical desktop/FVWM based
Requires:	fvwm
BuildArch:  noarch

%description
The icons that used to be part of the fvwm source distribution are now
accessible separately.

%prep
%setup -q -n fvwm_icons

%build

%install
shopt -s extglob
install -d -m 755 %{buildroot}%{_iconsdir}
install -d -m 755 %{buildroot}%{_miconsdir}

for i in mini.*; do
    install -m 644 $i %{buildroot}%{_miconsdir}/${i#mini.}
done
for i in !(mini.*); do
    install -m 644 $i %{buildroot}%{_iconsdir}/${i}
done

# prevent conflicts
rm -f %{buildroot}%{_iconsdir}/xemacs.xpm
rm -f %{buildroot}%{_miconsdir}/xmag.xpm

%files
%defattr(-,root,root)
%{_iconsdir}/*.xpm
%{_miconsdir}/*.xpm

%clean
rm -rf %{buildroot}


