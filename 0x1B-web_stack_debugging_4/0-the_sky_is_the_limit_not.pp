# Fixes extension typo
exec { 'ulimit-fix':
  command => "sed -i 's/15/404/g' /etc/default/nginx",
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
# Restart nginx server
exec { 'restart-server':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
