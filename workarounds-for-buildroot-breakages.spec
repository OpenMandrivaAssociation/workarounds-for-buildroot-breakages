Name:		workarounds-for-buildroot-breakages

Version:	0
Release:	27
Summary:	Workarounds for buildroot breakages
Group:		System/Configuration/Packaging
License:	Public Domain

BuildArch:	noarch

BuildRequires:	clang

%description
Workarounds for buildroot breakages

This package is bogus and just used to temporarily pretend that build
dependencies for some core packages exist, or to test various failures.

Do not install this package unless you're ABF. ;)

%prep

%build
# This is just a test to see if clang on RISC-V is working now

cat >test.c <<'EOF'
#include <stdio.h>
int main(int argc, char **argv) {
	puts("GTK sucks");
}
EOF
clang -O2 test.c
[ "$(./a.out)" = "GTK sucks" ] || exit 1

# Since hardfloat was the problem before, let's try something
# a little more float-ish too
cat >test.c <<'EOF'
#include <math.h>
#include <stdio.h>
int main(int argc, char **argv) {
	float f = -1.0;
	printf("%f\n", fabs(f));
}
EOF
clang -O2 test.c
[ "$(./a.out)" = '1.000000' ] || exit 1

exit 2

%install

%files
