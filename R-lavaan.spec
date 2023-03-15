#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lavaan
Version  : 0.6.15
Release  : 50
URL      : https://cran.r-project.org/src/contrib/lavaan_0.6-15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lavaan_0.6-15.tar.gz
Summary  : Latent Variable Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mnormt
Requires: R-numDeriv
Requires: R-pbivnorm
Requires: R-quadprog
BuildRequires : R-mnormt
BuildRequires : R-numDeriv
BuildRequires : R-pbivnorm
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
factor analysis, structural equation modeling and latent growth curve models.

%prep
%setup -q -n lavaan
cd %{_builddir}/lavaan

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678894567

%install
export SOURCE_DATE_EPOCH=1678894567
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lavaan/CITATION
/usr/lib64/R/library/lavaan/DESCRIPTION
/usr/lib64/R/library/lavaan/INDEX
/usr/lib64/R/library/lavaan/Meta/Rd.rds
/usr/lib64/R/library/lavaan/Meta/data.rds
/usr/lib64/R/library/lavaan/Meta/features.rds
/usr/lib64/R/library/lavaan/Meta/hsearch.rds
/usr/lib64/R/library/lavaan/Meta/links.rds
/usr/lib64/R/library/lavaan/Meta/nsInfo.rds
/usr/lib64/R/library/lavaan/Meta/package.rds
/usr/lib64/R/library/lavaan/NAMESPACE
/usr/lib64/R/library/lavaan/R/lavaan
/usr/lib64/R/library/lavaan/R/lavaan.rdb
/usr/lib64/R/library/lavaan/R/lavaan.rdx
/usr/lib64/R/library/lavaan/data/Rdata.rdb
/usr/lib64/R/library/lavaan/data/Rdata.rds
/usr/lib64/R/library/lavaan/data/Rdata.rdx
/usr/lib64/R/library/lavaan/help/AnIndex
/usr/lib64/R/library/lavaan/help/aliases.rds
/usr/lib64/R/library/lavaan/help/lavaan.rdb
/usr/lib64/R/library/lavaan/help/lavaan.rdx
/usr/lib64/R/library/lavaan/help/paths.rds
/usr/lib64/R/library/lavaan/html/00Index.html
/usr/lib64/R/library/lavaan/html/R.css
