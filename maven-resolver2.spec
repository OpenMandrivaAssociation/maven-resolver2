Name:           maven-resolver2
Epoch:          1
Version:        2.0.9
Release:        1
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
URL:            https://maven.apache.org/resolver/
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/maven/resolver/maven-resolver-%{version}-source-release.zip

Patch1:         0001-Remove-use-of-deprecated-SHA-1-and-MD5-algorithms.patch
Patch2:         0002-Make-I-O-errors-during-test-cleanup-non-fatal.patch

BuildRequires:  javapackages-bootstrap

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%prep
%autosetup -p1 -C

# Skip tests that require internet connection
#rm maven-resolver-supplier/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java
#rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/{HttpServer,HttpTransporterTest}.java
%pom_remove_dep :jetty-bom

#%pom_remove_plugin -r :bnd-maven-plugin
#%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
#%pom_remove_plugin -r :japicmp-maven-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
#%pom_disable_module maven-resolver-transport-classpath
#%mvn_package :maven-resolver-test-util __noinstall
%pom_disable_module maven-resolver-test-http
%pom_disable_module maven-resolver-transport-jetty
%pom_disable_module maven-resolver-transport-minio
%pom_disable_module maven-resolver-generator-sigstore
%pom_disable_module maven-resolver-generator-gnupg
%pom_disable_module maven-resolver-tools
%pom_disable_module maven-resolver-supplier-mvn3

%pom_remove_plugin :bnd-maven-plugin
%pom_remove_plugin :maven-jar-plugin

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :japicmp-maven-plugin

%mvn_compat_version : 2.0.9

%build
%mvn_build -j -f -j -- -Dmaven4Version=4.0.0-rc-4

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
