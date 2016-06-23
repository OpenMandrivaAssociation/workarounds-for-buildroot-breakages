Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	13
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch
Provides: python(abi) = 3.4

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build
# The cross_compiling macro is malfunctioning on aarch64, let's see the
# output of each individual step.
echo cross_compiling: %{cross_compiling}
echo 'int main() { return 0; }' >/tmp/rpm_cc_test
%{__cc} %{optflags} -x c - -o /tmp/rpm_cc_test 

%install

%files
