%global packname  Cairo
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.5_1
Release:          2
Summary:          R graphics device using cairo graphics library for creating high-quality bitmap (PNG, JPEG, TIFF), vector (PDF, SVG, PostScript) and display (X11 and Win32) output
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-1.tar.gz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    cairo-devel
BuildRequires:    glib2-devel
BuildRequires:    libice-devel
BuildRequires:    libsm-devel
BuildRequires:    libxmu-devel
BuildRequires:    libxt-devel
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


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5_1-2
+ Revision: 775066
- Update to latest version
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5_0-1
+ Revision: 774884
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Fri Dec 25 2009 Jérôme Brenier <incubusss@mandriva.org> 2.10-1mdv2010.1
+ Revision: 482262
- new version 2.10

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.8-1mdv2009.0
+ Revision: 270294
- update to new version 2.8

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Fri Feb 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.6-2mdv2008.1
+ Revision: 176958
- remove requires on libR.so

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.6-1mdv2008.1
+ Revision: 169889
- fix buildrequires
- fix Url
- suggests R-cran-RGtk2
- add source and spec file
- Created package structure for R-cran-cairoDevice.

