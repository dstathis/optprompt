%global srcname optprompt

Name:           python%{python3_pkgversion}-%{srcname}
Version:        0.4.0
Release:        1%{?dist}
Summary:        A prompting option parser

License:        LGPL
URL:            https://git.nasuni.net/projects/TOOL/repos/filer-deploy/browse
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-toml

# For pytest
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-toml

%description
A prompting option parser

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=".:${PYTHONPATH}" pytest-3

%files
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue Jun 02 2020 Dylan Stephano-Shachter <dylan@theone.ninja> - 0.4.0-1
- Initial Package

