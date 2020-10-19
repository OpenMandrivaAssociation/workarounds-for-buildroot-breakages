Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	37
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch

Provides:	xdg-desktop-portal-implementation

%ifarch %{riscv}
# Make basesystem happy
Provides:	kernel = 5.2.14-1
Provides:	bootloader
Provides:	pinentry
%endif

Provides:	python(abi) = 3.8
%if "%{_lib}" == "lib64"
Provides:	libpython3.8.so.1()(64bit)
%else
Provides:	libpython3.8.so.1
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
