Summary:	JPEG/TIFF image probe
Summary(pl):	Sprawdzanie informacji o obrazach JPEG/TIFF
Name:		exifprobe
Version:	1.2.5
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://www.monroe.net/~dhh/exifprobe.d/%{name}-%{version}.tar.gz
# Source0-md5:	0c4b2103cf04ca66bf48707ae89db8d5
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

%description -l pl
Exifprobe sprawdza i podaje zawarto¶æ i strukturê plików obrazów JPEG
i TIFF. Rozpoznaje wszystkie standardowe znaczniki JPEG (w³±cznie z
APPn) i podaje zawarto¶æ ka¿dego prawid³owo zbudowanego TIFF IFD,
nawet je¶li nie rozpoznano znaczników. Rozpoznawane znaczniki TIFF i
TIFF/EP s± rozwijane, w tym sekcje EXIT2.2 i MakerNotes z aparatów,
które mo¿na znale¼æ w plikach w formacie TIFF IFD. Znaczniki GPS i
GeoTIFF s± rozpoznawane i wypisywane w postaci surowej, ale nie
rozwijane. Podawane jest po³o¿enie, rozmiar i format danych obrazu.

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
