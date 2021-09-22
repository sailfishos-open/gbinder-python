%define _disable_source_fetch 0

%define _proj_name gbinder-python
%define _git_refspec 79d40e9e564772973f7f085ed5c48e3fc625e0f5
%define _git_refspec_short %(echo %{_git_refspec} | cut -c -7)
%define _build_date %(date +%Y%m%d)

%define modname %{_proj_name}
%define fedname %{modname}
%define internal_name gbinder

Name: python-%{modname}
Version: 1.0.0git.%{_build_date}.%{_git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: Python bindings for libgbinder

BuildRequires: gcc
BuildRequires: libgbinder-devel libglibutil-devel pkgconfig

Source: https://github.com/erfanoabdi/%{_proj_name}/tarball/%{_git_refspec}#%{name}-%{_git_refspec}.tar.gz

%description
Cython extension module for gbinder

%package -n python3-%{fedname}
Summary: %{summary}
BuildRequires: python3-devel python3-setuptools
BuildRequires: python3-Cython
%{?python_provide:%python_provide python3-%{fedname}}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{fedname} 
%{description}

Python 3 version.

%prep
%setup -qn erfanoabdi-%{_proj_name}-%{_git_refspec_short}/upstream

%build
%{set_build_flags}
%{python3} ./setup.py build_ext --inplace --cython
env WITH_CYTHON=true %{py3_build}

%install
%{py3_install}

%files -n python3-%{fedname}
%{python3_sitearch}/%{internal_name}*.so
%{python3_sitearch}/%{internal_name}*.egg-info