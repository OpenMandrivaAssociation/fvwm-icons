%define	name	fvwm-icons
%define	version	1.0
%define	release	%mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	FVWM icons
URL: 		http://www.fvwm.org/
Source:		http://www.fvwm.org/generated/icon_download/fvwm_icons.tar.bz2
License:	GPL
Group:		Graphical desktop/FVWM based
Obsoletes:	fvwm2-icons
Provides:	fvwm2-icons
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
# From twm
rm -f %{buildroot}%{_miconsdir}/twm.xpm

%files
%defattr(-,root,root)
%{_iconsdir}/*.xpm
%{_miconsdir}/*.xpm

%clean
rm -rf %{buildroot}




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 618376
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2010.0
+ Revision: 428979
- rebuild

* Thu Aug 07 2008 Olivier Thauvin <nanardon@mandriva.org> 1.0-8mdv2009.0
+ Revision: 265611
- kill twm icons because conflicts

* Tue Aug 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.0-7mdv2009.0
+ Revision: 264104
- obsolete and provide fvwm2-icons (currently it's an orphan of fvwm2)
- don't require fvwm (no reason to, any require should be in the other direction)
- fix some indentations

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2009.0
+ Revision: 245571
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-4mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-4mdv2007.0
+ Revision: 132919
- fix conflict with xmag (bug #27433)

* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2007.1
+ Revision: 84684
- new release
- install mini icons in dedicated directory

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2007.1
+ Revision: 84082
- bump release
- remove conflicting xemacs icon

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2007.1
+ Revision: 84056
- Import fvwm-icons

