Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	32
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

# libstdc++ requiring python(abi) = 3.7 because of
# gdb scripts is very messed up...
Provides:	python(abi) = 3.7
Provides:	libpython3.7m.so.1.0
Provides:	libpython3.7m.so.1.0()(64bit)
Provides:	/usr/bin/bash
Requires:	bash

BuildArch:	noarch

%ifarch %{riscv}
# Make basesystem happy
Provides:	kernel = 5.2.14-1
Provides:	bootloader
Provides:	pinentry
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
