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



