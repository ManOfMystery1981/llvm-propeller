Name:           llvm-propeller
Version:        23.0.0
Release:        1%{?dist}
Summary:        LLVM/Clang 23 profile tooling from Google LLVM Propeller
Group:          Development/Tools
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/google/llvm-propeller
# Prebuilt /opt/llvm-propeller-23 tree (clang, llvm-profgen,
# generate_propeller_profiles, builtin headers), packed as:
#   cd /opt && tar cJf llvm-propeller-23-23.0.0.tar.xz llvm-propeller-23
# then uploaded to the ABF file store. The tarball MUST contain the
# top-level llvm-propeller-23/ directory.
Source0:        llvm-propeller-23-23.0.0.tar.xz

%description
# rpmlint: disable=devel-file-in-non-devel-package
# rpmlint: disable=binary-or-shlib-defines-rpath
LLVM/Clang 23 profile tooling built from the LLVM source tree pinned by
the Google LLVM Propeller project.

Installed under /opt/llvm-propeller-23 so it does not conflict with the
system LLVM/Clang installation. Provides the profile-generation tools
(llvm-profgen, generate_propeller_profiles) used by the
omx-kernel-build AutoFDO/Propeller pipeline.

%prep
%setup -q -n llvm-propeller-23

%build
# Prebuilt tree; no compilation on the farm.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt
cp -a . %{buildroot}/opt/llvm-propeller-23/

# Normalize permissions for RPM packaging.
find %{buildroot}/opt/llvm-propeller-23/bin -type f -exec chmod 0755 {} +
find %{buildroot}/opt/llvm-propeller-23/bin -type l -exec chmod 0755 {} +
find %{buildroot}/opt/llvm-propeller-23/lib -type d -exec chmod 0755 {} +
find %{buildroot}/opt/llvm-propeller-23/lib -type f -exec chmod 0644 {} +

%files
/opt/llvm-propeller-23/bin/clang
/opt/llvm-propeller-23/bin/clang-23
/opt/llvm-propeller-23/bin/clang++
/opt/llvm-propeller-23/bin/clang-cl
/opt/llvm-propeller-23/bin/clang-cpp
/opt/llvm-propeller-23/bin/llvm-profgen
/opt/llvm-propeller-23/bin/generate_propeller_profiles
/opt/llvm-propeller-23/lib/clang/23/include

%changelog
* Wed Oct 07 2026 noncitizen-national <noncitizen-national@localhost> - 23.0.0-1
- Initial package of LLVM/Clang built from Google LLVM Propeller.
* Thu Oct 08 2026 noncitizen-national <noncitizen-national@localhost> - 23.0.0-1
- ABF adaptation: ship the prebuilt /opt tree as a file-store tarball
  instead of copying from local build trees.
