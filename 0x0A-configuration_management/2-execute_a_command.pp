# This pupppet manifest kills a running process named killmenow.

exec {'kill-killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin/',
    returns => [0, 1],
}
