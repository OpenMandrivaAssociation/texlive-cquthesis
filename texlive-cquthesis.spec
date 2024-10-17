Name:		texlive-cquthesis
Version:	55643
Release:	2
Summary:	LaTeX Thesis Template for Chongqing University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cquthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cquthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cquthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cquthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
CQUThesis stands for Chongqing University Thesis Template for
LaTeX, bearing the ability to support bachelor, master, doctor
dissertations with grace and speed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cquthesis
%{_texmfdistdir}/tex/latex/cquthesis
%{_texmfdistdir}/bibtex/bst/cquthesis
%doc %{_texmfdistdir}/doc/latex/cquthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
