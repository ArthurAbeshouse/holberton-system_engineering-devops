# Fixes extension typo
exec { 'typo-fix':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
# Restart Apache2 server
exec { 'restart-server':
  command => 'sudo service apache2 restart',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}