Name:           perl-XML-Stream
Version:        1.22 
Release:        12%{?dist}
Summary:        XML::Stream - streaming XML library

Group:          Development/Libraries
License:        (GPL+ or Artistic) or LGPLv2+
URL:            http://search.cpan.org/dist/XML-Stream/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RE/REATMON/XML-Stream-%{version}.tar.gz 
Source1:        LICENSING.correspondance
Patch0:         tests.patch
BuildArch:      noarch 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Authen::SASL)
BuildRequires:  perl(MIME::Base64)
        
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Net::DNS)
# also pulled in via a 'requires' construct; but not yet in Fedora
#Requires:       perl(HTTP::ProxyAutoConfig)

%description
This module provides the user with methods to connect to a remote server, 
send a stream of XML to the server, and receive/parse an XML stream from 
the server.  It is primarily based work for the Etherx XML router 
developed by the Jabber Development Team.  For more information about this 
project visit http://etherx.jabber.org/stream/.  

XML::Stream gives the user the ability to define a central callback that 
will be used to handle the tags received from the server.  These tags are 
passed in the format defined at instantiation time.  the closing tag of an
object is seen, the tree is finished and passed to the call back function.  
What the user does with it from there is up to them.

For a detailed description of how this module works, and about the data 
structure that it returns, please view the source of Stream.pm and 
look at the detailed description at the end of the file.

%prep
%setup -q -n XML-Stream-%{version}
%patch0

cp %{SOURCE1} .

# generate our other two licenses...
perldoc perlgpl      > LICENSE.GPL
perldoc perlartistic > LICENSE.Artistic

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*


%check
%{?_with_network_tests: make test}

rm -rf t/lib

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES README INFO LICENSE.* LICENSING* t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.22-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-9
- fix license tag (technically, it was correct before, but this change prevents
  rpmlint from flagging it as bad in a false positive)

* Mon Jul 14 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.22-8
- add IO::Socket::SSL as a BR/R (see BZ#455344)
- also add Net::DNS
- make tests run if --with network-tests
- misc spec touchups

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-7
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-6.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-6
- bump for mass rebuild

* Sat May 27 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-5
- bump release, to deal with cvs-import.sh being confused by .rpmmacros

* Thu May 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-4
- include license text, including generated ones
- include correspondance with the module's author

* Wed May 24 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-3
- update license to triple licensed, based on conversations with upstream

* Mon May 15 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-2
- add CHANGES, README, INFO to docs

* Fri May 12 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.22-1
- first f-e spec.
- patched the tests to try to connect to the gtalk jabber servers, since the
  default one seemed to be "non-funct"
  
