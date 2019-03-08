Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	26
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch
Provides:	java-headless = 1.11.0-1
Requires:	java-11-openjdk

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build

%install

%files
