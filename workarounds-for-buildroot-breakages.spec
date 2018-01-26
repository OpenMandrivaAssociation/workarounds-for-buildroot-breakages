Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	18
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch
Provides:	devel(libLLVMRISCVInfo(64bit))
Provides:	devel(libLLVMRISCVCodeGen(64bit))
Provides:	devel(libLLVMRISCVDesc(64bit))
Provides:	devel(libLLVMRISCVInfo)
Provides:	devel(libLLVMRISCVCodeGen)
Provides:	devel(libLLVMRISCVDesc)
Provides: pinentry-1.1.0-2

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build

%install

%files
