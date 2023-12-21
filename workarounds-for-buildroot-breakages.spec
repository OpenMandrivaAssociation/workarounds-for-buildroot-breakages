Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	51
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch

%ifarch %{riscv}
# Make basesystem happy
Provides:	kernel = 5.2.14-1
Provides:	bootloader
Provides:	pinentry
%endif

Requires:	coreutils
Provides:	/bin/true
Provides:	/bin/false
Provides:	openlitespeed
Provides:	xdg-desktop-portal-implementation
Provides:	%{_lib}gpuruntime
Provides:	group(mock)

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build

%install

%files
