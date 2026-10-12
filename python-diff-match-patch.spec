Name:		python-diff-match-patch
Version:	20241021
Release:	2
Summary:	Diff, match and patch algorithms for plain text
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/diff-match-patch-python/diff-match-patch
Source0:	https://files.pythonhosted.org/packages/source/d/diff-match-patch/diff_match_patch-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(flit-core)

%description
Python port of Google's diff-match-patch libraries. Used by Aider
to apply code edits.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/diff_match_patch
%{py_sitedir}/diff_match_patch-*.*-info
