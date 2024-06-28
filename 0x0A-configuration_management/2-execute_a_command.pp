# This pupppet manifest kills a running process named killmenow.

exec {
    'killprocess':
    command => 'pkill -f killmenow',
    path    => ['usr/bin','usr/sbin']
}
