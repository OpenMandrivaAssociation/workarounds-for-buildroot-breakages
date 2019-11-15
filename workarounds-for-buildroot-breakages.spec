Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	28
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

# Crosscompiler breakage...
Provides:	libgcc_s.so.1(GCC_4.5.0)(64bit)
Provides:	libgcc_s.so.1(GCC_3.5)

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
