Summary:	JPEG/TIFF image probe
Name:		exifprobe
Version:	1.2.4
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://www.monroe.net/~dhh/exifprobe.d/%{name}-%{version}.tar.gz
# Source0-md5:	e10f72205e805928102fdcf44c508a64
URL:		http://www.monroe.net/~dhh/exifprobe.d/exifprobe.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exifprobe examines and reports the contents and structure of JPEG and
TIFF image files. It will recognize all standard JPEG markers
(including APPn markers) and will report the contents of any properly
structured TIFF IFD encountered, even when entry tags are not
recognized. Recognized TIFF and TIFF/EP tags are expanded, including
EXIF2.2 sections and camera MakerNotes which are found to be in TIFF
IFD format. GPS and GeoTIFF tags are recognized and entries printed in
"raw" form, but are not expanded. Location, size, and format of image
data is reported.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -DCOLOR -Wall -Wno-unused -Wno-parentheses -Wno-trigraphs"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CAMERA_makes_and_models CREDITS DESCRIPTION *.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*1.*
