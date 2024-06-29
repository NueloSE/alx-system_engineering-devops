# This puppet manifest installs flask from pip3.

package { 'python3':
    ensure => present,
}

package { 'python3-pip':
    ensure  => present,
    require => Package['python3'],
}

package {'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
}
