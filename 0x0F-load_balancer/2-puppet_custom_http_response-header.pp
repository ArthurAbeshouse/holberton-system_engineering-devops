# Adds a custom HTTP header

exec { 'Custom HTTP Header':
     command => 'INDEX="Holberton School" && ERROR="Ceci n\'est pas une page - 404" && sudo apt-get -y update && sudo apt-get -y install nginx && echo "$INDEX" | sudo tee /var/www/html/index.html > /dev/null && echo "$ERROR" | sudo tee /var/www/html/error_404.html > /dev/null && sudo sed -i "s|server_name\ _;|server_name _;\n\trewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;|" /etc/nginx/sites-available/default && sudo sed -i "51i\ \n\terror_page 404 /error_404.html;\n\tlocation = /error_404.html {\n\t\troot /var/www/html/;\n\t\tinternal;\n\t}\n" /etc/nginx/sites-available/default && sudo sed -i "32i\\\tadd_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx start',
     provider => shell,
}