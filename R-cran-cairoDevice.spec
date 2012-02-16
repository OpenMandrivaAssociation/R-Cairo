%define modulename cairoDevice
%define realver 2.10
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	A cairo antialiased graphics device driver for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	gtk2-devel
Requires:	R-base
Suggests:	R-cran-RGtk2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Cairo/GTK graphics device driver with output to screen, 
file (png, svg, pdf, and ps) or memory (GdkDrawable).
The screen device may be embedded into RGtk2 interfaces.
Supports all interactive features of other graphics devices,
including getGraphicsEvent().

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/R/library/%{modulename}
