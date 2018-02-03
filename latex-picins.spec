Name: 		latex-picins
Version: 	3.0
Release: 	1
Summary: 	LaTeX package allowing to wrap text around an inserted picture
License: 	Public Domain
Group: 		Publishing
URL:		https://ctan.org/pkg/picins
Source0: 	http://mirrors.ctan.org/macros/latex209/contrib/picins.zip
Requires: 	texlive-latex texlive-collection-latex
BuildRequires:	texlive-latex texlive-collection-latex
BuildArch:	noarch

Requires(post):		texlive-kpathsea.bin
Requires(postun):	texlive-kpathsea.bin

%description
LaTeX package allowing to wrap text around an inserted picture

%prep
%setup -q -n picins

%build

%install
install -d -m 755 %{buildroot}%{_datadir}/texmf-dist/tex/latex/picins
install -m 644 *.{sty,msp} %{buildroot}%{_datadir}/texmf-dist/tex/latex/picins

install -d -m 755 %{buildroot}%{_datadir}/texmf-dist/doc/latex/picins
install -m 644 *.{doc,dvi} %{buildroot}%{_datadir}/texmf-dist/doc/latex/picins

%post -p %_bindir/texhash

%postun -p %_bindir/texhash

%files
%defattr(-,root,root)
%doc README.1st picins.txt
%{_datadir}/texmf-dist/tex/latex/picins
%{_datadir}/texmf-dist/doc/latex/picins
