# This manifest uses makes changes to the configuration file in the `/etc/ssh/ssh_config.d` file

file_line { 'Turn off passwd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '     PasswordAuthentication no',
}

file_line {'Declare identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '     IdentityFile ~/.ssh/school',
}
