%global packname  Cairo
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.5.2
Release:          2
Summary:          Graphics device using cairo for creating high-quality output
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Cairo_1.5-2.tar.gz
Requires:         R-png
BuildRequires:    R-devel Rmath-devel R-png texlive-collection-latex 
BuildRequires:    cairo-devel
BuildRequires:    glib2-devel
BuildRequires:    libice-devel
BuildRequires:    pkgconfig(sm)
BuildRequires:    pkgconfig(xmu)
BuildRequires:    pkgconfig(xt)
%rename R-cran-Cairo

%description
This package provides a Cairo graphics device that can be use to create
high-quality vector (PDF, PostScript and SVG) and bitmap output
(PNG,JPEG,TIFF), and high-quality rendering in displays (X11 and Win32).
Since it uses the same back-end for all output, copying across formats is
WYSIWYG. Files are created without the dependence on X11 or other external
programs. This device supports alpha channel (semi-transparent drawing)
and resulting images can contain transparent and semi-transparent regions.
It is ideal for use in server environemnts (file output) and as a
replacement for other devices that don't have Cairo's capabilities such as
alpha support or anti-aliasing. Backends are modular such that any subset
of backends is supported.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
