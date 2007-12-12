%define	version	1.4
%define release	%mkrel 2

Summary:	WAV file Play & Record applications
Name:		wavplay
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		ftp://sunsite.unc.edu/pub/Linux/apps/sound/
Source:		%{name}-%{version}.tar.bz2
Patch0:		wavplay-1.4-fix-compile.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
%{name} package contains:

wavplay - plays WAV format file to the audio device.
wavrec - samples the audio device and writes WAV file.

%prep
%setup -q
%patch0 -p1 -b .fix-compile
chmod -R o+r .

%build
%__make CPU="" OPT="%{optflags}" INSTDIR="%{_bindir}" no_x

%install
rm -rf %{buildroot}
install -m 0755 -D wavplay %{buildroot}%{_bindir}/wavplay
ln -s wavplay %{buildroot}%{_bindir}/wavrec
install -m 0644 -D wavplay.1 %{buildroot}%{_mandir}/man1/wavplay.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS COPYING README
%attr(4511,root,root) %{_bindir}/wavplay
%{_bindir}/wavrec
%{_mandir}/man?/*

