# This puppet manifest is used to create a file called school in /tmp folder

file {
    '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
