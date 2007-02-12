Summary:	JPEG/TIFF image probe
Summary(pl.UTF-8):   Sprawdzanie informacji o obrazach JPEG/TIFF
Name:		exifprobe
Version:	2.0.1
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://www.virtual-cafe.com/~dhh/tools.d/exifprobe.d/%{name}-%{version}.tar.gz
# Source0-md5:	3aa2ba4baa6d60c72fb8a4b9b6341c4c
URL:		http://www.virtual-cafe.com/~dhh/tools.d/exifprobe.d/
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

%description -l pl.UTF-8
Exifprobe sprawdza i podaje zawartość i strukturę plików obrazów JPEG
i TIFF. Rozpoznaje wszystkie standardowe znaczniki JPEG (włącznie z
APPn) i podaje zawartość każdego prawidłowo zbudowanego TIFF IFD,
nawet jeśli nie rozpoznano znaczników. Rozpoznawane znaczniki TIFF i
TIFF/EP są rozwijane, w tym sekcje EXIT2.2 i MakerNotes z aparatów,
które można znaleźć w plikach w formacie TIFF IFD. Znaczniki GPS i
GeoTIFF są rozpoznawane i wypisywane w postaci surowej, ale nie
rozwijane. Podawane jest położenie, rozmiar i format danych obrazu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -Wno-unused -Wno-parentheses -Wno-trigraphs"

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
