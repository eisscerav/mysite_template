# mysite_template

## nginx error: 
 - see /var/log/nginx/error.log

## Setup uWSGI+nginx+Django
[reference doc](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site)
 - /etc/nginx/sites-available/mysite_nginx.conf 

## Start nginx for serving django
- Let uwsgi talk with socket on linux
- uwsgi --socket mysite.sock --wsgi-file test.py --chmod-socket=666
- uwsgi --socket mysite.sock --module mysite.wsgi --chmod-socket=666
- Start service nginx with config file [config sample](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site)


## Dependencies
 - [mysql](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
 - [django access mysql](https://askubuntu.com/questions/1321141/unable-to-install-mysqlclient-on-ubuntu-20-10)
 - sudo apt install python3-dev build-essential
 - sudo apt install libssl1.1
 - sudo apt install libssl1.1=1.1.1f-1ubuntu2
 - sudo apt install libssl-dev
 - sudo apt install libmysqlclient-dev
 - pip3 install mysqlclient (need by django)
