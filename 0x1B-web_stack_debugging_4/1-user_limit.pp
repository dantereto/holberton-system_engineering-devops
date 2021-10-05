#web solution 
exec { 'fix error':
  command  => "sudo sed -i 's/nofile 5/nofile 50000/' /etc/security/limits.conf",
  provider => shell;
}

exec { 'f error':
  command  => "sudo sed -i 's/nofile 4/nofile 40000/' /etc/security/limits.conf",
  provider => shell;
}