# Increases the number of requests allowed on the nginx server

exec { 'os_config_fix':
  command => '/usr/bin/sed -i "s/holberton/47/g" /etc/security/limits.conf',
}