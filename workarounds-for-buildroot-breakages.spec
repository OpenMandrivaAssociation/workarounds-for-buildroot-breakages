Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	45
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

%ifarch %{aarch64}
Provides:	libomptarget.so()(64bit)
Provides:	libomptarget.so(VERS1.0)(64bit)
Provides:	lib64gpuruntime = 14.0.3-2
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
