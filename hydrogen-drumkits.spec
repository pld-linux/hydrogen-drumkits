Summary:	Hydrogen drumkits
Summary(pl):	Zestawy perkusyjne dla Hydrogena
Name:		hydrogen-drumkits
Version:	1.0
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/hydrogen/3355606.tar.gz
# Source0-md5:	1980647fa79029fa1dd1eb4f5ad14d65
Source1:	http://dl.sourceforge.net/hydrogen/DrumkitPack1.tar.gz
# Source1-md5:	8ddc8e3f5d02f5e2f12533db45e77c55
Source2:	http://dl.sourceforge.net/hydrogen/DrumkitPack2.tar.gz
# Source2-md5:	535b873aead13de2105cc2a5609ec977
Source3:	http://dl.sourceforge.net/hydrogen/EasternHop-1.tar.gz
# Source3-md5:	def807440c5a5e01e22f2b7a52a872df
Source4:	http://dl.sourceforge.net/hydrogen/TD-7.tar.gz
# Source4-md5:	2ccaed2a392a97143f31f52488fdde74
Source5:	http://dl.sourceforge.net/hydrogen/UltraAcousticKit.tar.gz
# Source5-md5:	ee0974b404d34a2c5cf3d8f3952a80e9
Source6:	http://dl.sourceforge.net/hydrogen/Millo_MultiLayered2.h2drumkit
# Source6-md5:	9388f63cab321af979387493e0505ac6
Source7:	http://dl.sourceforge.net/hydrogen/HardElectro1.tar.gz
# Source7-md5:	bc2bcc16d404441ef3a5b1b86c6c4a25
Source8:	http://dl.sourceforge.net/hydrogen/ErnysPercussion.h2drumkit
# Source8-md5:	0e96f5971d5db887a186d5739c12ab77
Source9:	http://dl.sourceforge.net/hydrogen/Millo-Drums_v1.tar.gz
# Source9-md5:	8a573ea8040aa8ee3dacfcb3d3fc4ab8
URL:		http://hydrogen.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		hydrogen_version 0.9.0

%description
Hydrogen drumkits.

%description -l pl
Zestawy perkusyjne dla Hydrogena.

%package 3355606
Summary:	Hydrogen drumkit 3355606
Summary(pl):	Zestaw perkusyjny 3355606 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description 3355606
Hydrogen drumkit 3355606.

%description 3355606 -l pl
Zestaw perkusyjny 3355606 dla Hydrogena.

%package DrumkitPack1
Summary:	Hydrogen drumkit DrumkitPack1
Summary(pl):	Zestaw perkusyjny DrumkitPack1 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description DrumkitPack1
Hydrogen drumkit DrumkitPack1.

%description DrumkitPack1 -l pl
Zestaw perkusyjny DrumkitPack1 dla Hydrogena.

%package DrumkitPack2
Summary:	Hydrogen drumkit DrumkitPack2
Summary(pl):	Zestaw perkusyjny DrumkitPack2 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description DrumkitPack2
Hydrogen drumkit DrumkitPack2.

%description DrumkitPack2 -l pl
Zestaw perkusyjny DrumkitPack2 dla Hydrogena.

%package EasternHop-1
Summary:	Hydrogen drumkit EasternHop-1
Summary(pl):	Zestaw perkusyjny EasternHop-1 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description EasternHop-1
Hydrogen drumkit EasternHop-1.

%description EasternHop-1 -l pl
Zestaw perkusyjny EasternHop-1 dla Hydrogena.

%package TD-7
Summary:	Hydrogen drumkit TD-7
Summary(pl):	Zestaw perkusyjny TD-7 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description TD-7
Hydrogen drumkit TD-7.

%description TD-7 -l pl
Zestaw perkusyjny TD-7 dla Hydrogena.

%package UltraAcousticKit
Summary:	Hydrogen drumkit UltraAcousticKit
Summary(pl):	Zestaw perkusyjny UltraAcousticKit
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description UltraAcousticKit
Hydrogen drumkit UltraAcousticKit.

%description UltraAcousticKit -l pl
Zestaw perkusyjny UltraAcousticKit dla Hydrogena.

%package Millo-MultiLayered2
Summary:	Hydrogen drumkit Millo-MultiLayered2
Summary(pl):	Zestaw perkusyjny Millo-MultiLayered2 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description Millo-MultiLayered2
Hydrogen drumkit Millo-MultiLayered2.

%description Millo-MultiLayered2 -l pl
Zestaw perkusyjny Millo-MultiLayered2 dla Hydrogena.

%package HardElectro1
Summary:	Hydrogen drumkit HardElectro1
Summary(pl):	Zestaw perkusyjny HardElectro1 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description HardElectro1
Hydrogen drumkit HardElectro1.

%description HardElectro1 -l pl
Zestaw perkusyjny HardElectro1 dla Hydrogena.

%package ErnysPercussion
Summary:	Hydrogen drumkit ErnysPercussion
Summary(pl):	Zestaw perkusyjny ErnysPercussion dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description ErnysPercussion
Hydrogen drumkit ErnysPercussion.

%description ErnysPercussion -l pl
Zestaw perkusyjny ErnysPercussion dla Hydrogena.

%package Millo-Drums_v.1
Summary:	Hydrogen drumkit Millo-Drums_v.1
Summary(pl):	Zestaw perkusyjny Millo-Drums_v.1 dla Hydrogena
Group:          Applications/Sound
Requires:	hydrogen >= %{hydrogen_version}

%description Millo-Drums_v.1
Hydrogen drumkit Millo-Drums_v.1.

%description Millo-Drums_v.1 -l pl
Zestaw perkusyjny Millo-Drums_v.1 dla Hydrogena.

%prep
%setup -q -c -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs

mv Millo-Drums_v1/demo\ songs Millo-Drums_v1/demo_songs

for dir in 3355606 DrumkitPack1 DrumkitPack2 EasternHop-1 TD-7 \
	UltraAcousticKit HardElectro1 Millo-Drums_v1/demo_songs
do
install $dir/*.h2song \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/demo_songs
done

tar zxf 3355606/3355606kit.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf DrumkitPack1/HipHop-1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf DrumkitPack1/HipHop-2.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf DrumkitPack2/Synthie-1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf DrumkitPack2/TR808909.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf DrumkitPack2/Techno-1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf EasternHop-1/EasternHop-1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf TD-7/TD-7kit.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf UltraAcousticKit/UltraAcousticKit.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf HardElectro1/HardElectro1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits
tar zxf Millo-Drums_v1/Millo-Drums_v.1.h2drumkit -C \
	$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits

install -d \
$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits/Millo_MultiLayered2
install Millo_MultiLayered2/* \
$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits/Millo_MultiLayered2

install -d \
$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits/ErnysPercussion
install ErnysPercussion/* \
$RPM_BUILD_ROOT%{_datadir}/hydrogen/data/drumkits/ErnysPercussion

%clean
rm -rf $RPM_BUILD_ROOT

%files 3355606
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/3355606kit
%{_datadir}/hydrogen/data/demo_songs/3355606demo.h2song

%files DrumkitPack1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/HipHop-1
%{_datadir}/hydrogen/data/drumkits/HipHop-2
%{_datadir}/hydrogen/data/demo_songs/HipHop*.h2song

%files DrumkitPack2
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/Synthie-1
%{_datadir}/hydrogen/data/drumkits/Techno-1
%{_datadir}/hydrogen/data/drumkits/TR808909
%{_datadir}/hydrogen/data/demo_songs/Synthie-1.demo1.h2song
%{_datadir}/hydrogen/data/demo_songs/Techno-1*.h2song
%{_datadir}/hydrogen/data/demo_songs/TR808909demo1.h2song

%files EasternHop-1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/EasternHop-1
%{_datadir}/hydrogen/data/demo_songs/EasternHop-1*.h2song

%files TD-7
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/TD-7kit
%{_datadir}/hydrogen/data/demo_songs/TD7.h2song

%files UltraAcousticKit
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/UltraAcousticKit
%{_datadir}/hydrogen/data/demo_songs/UltraAcousticKitDemo.h2song

%files HardElectro1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/HardElectro1
%{_datadir}/hydrogen/data/demo_songs/HardElectro1_demo.h2song

%files Millo-MultiLayered2
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/Millo_MultiLayered2

%files ErnysPercussion
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/ErnysPercussion

%files Millo-Drums_v.1
%defattr(644,root,root,755)
%{_datadir}/hydrogen/data/drumkits/Millo-Drums_v.1
%{_datadir}/hydrogen/data/demo_songs/Groovy.h2song
%{_datadir}/hydrogen/data/demo_songs/Mildrums.h2song
%{_datadir}/hydrogen/data/demo_songs/Mildrums2-2.h2song
%{_datadir}/hydrogen/data/demo_songs/Mildrums3.h2song
%{_datadir}/hydrogen/data/demo_songs/Millo-Drums.h2song
%{_datadir}/hydrogen/data/demo_songs/NewJazzy.h2song
%{_datadir}/hydrogen/data/demo_songs/rullada.h2song
%{_datadir}/hydrogen/data/demo_songs/tipododiciottavi.h2song
