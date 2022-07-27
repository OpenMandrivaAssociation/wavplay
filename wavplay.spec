Summary:	WAV file Play & Record applications
Name:		wavplay
Version:	2.0
Release:	1
License:	GPL
Group:		Sound
URL:		ftp://sunsite.unc.edu/pub/Linux/apps/sound/
Source:		https://sourceforge.net/projects/wavplay/files/Release%20Downloads/wavplay-%{version}.tar.gz

BuildRequires:  motif-devel
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xmu)

%description
%{name} package contains:

wavplay - plays WAV format file to the audio device.
wavrec - samples the audio device and writes WAV file.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install


%files
%doc COPYING README
%{_bindir}/wavplay*
%{_bindir}/xltwavplay
%{_bindir}/wavrec
%{_datadir}/wavplay/wavplay.1
%{_mandir}/man?/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4-6mdv2010.0
+ Revision: 434703
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-5mdv2009.0
+ Revision: 261921
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-4mdv2009.0
+ Revision: 255837
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.4-2mdv2008.1
+ Revision: 129286
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import wavplay


* Fri Jan 21 2005 Abel Cheung <deaddog@mandrake.org> 1.4-2mdk
- rebuild
- enable suid
- P0: fix compilation

* Wed Oct 08 2003 Abel Cheung <deaddog@deaddog.org> 1.4-1mdk
- First Mandrake package
- Don't suid the binary, but lost the ability for real time
  scheduling
