Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	11
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

Provides:	devel(libLLVM-3.7)
Provides:	devel(libLLVM-3.6)
Provides:	devel(libLLVM-3.7(64bit))
Provides:	devel(libLLVM-3.6(64bit))
Provides:	libLLVM-3.7.so()(64bit)
Provides:	libLLVM-3.7.so()

BuildArch:	noarch

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist.

Do not install this package unless you're ABF. ;)

%prep

%build

%install

%files
