Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	3
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain
Provides:	python(abi) = 2.7
Provides:	freetype2 = 2.1.10
Requires:	python-devel
%ifarch %{ix86}
Provides:	libpthread.so.0.9.33
%endif

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
