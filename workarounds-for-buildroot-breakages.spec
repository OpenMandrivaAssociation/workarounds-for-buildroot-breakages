Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	25
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch
%if "%{_lib}" == "lib64"
Requires:	lib64double-conversion3
Provides:	libdouble-conversion.so.3.0.0()(64bit)
%else
Requires:	libdouble-conversion3
Provides:	libdouble-conversion.so.3.0.0
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
