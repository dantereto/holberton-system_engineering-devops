#web solution 
exec { 'fix error':
  command  => "sudo sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  provider => shell;
}