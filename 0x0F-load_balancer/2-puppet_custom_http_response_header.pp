# puppet
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
->

package { 'nginx':
  ensure   => present,
  name     => 'nginx',
  provider => 'apt'
}
->

file { 'index':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School'
}
->

exec { 'Set X-Served-By':
  command  => 'sed -i "/server_name _;/a add_header X-Served-By \$hostname;" /etc/nginx/sites-enabled/default',
  user     => 'root',
  provider => 'shell'
}
->

exec { 'restart nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}