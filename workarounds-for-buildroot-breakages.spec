Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	14
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch
Provides: python(abi) = 3.4
%ifarch aarch64
Provides: devel(libLLVMLanaiInstPrinter(64bit)))
%endif

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build

%install

%files
