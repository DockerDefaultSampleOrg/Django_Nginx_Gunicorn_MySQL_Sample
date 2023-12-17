#
# Gunicorn config file
#
wsgi_app = '<プロジェクト名>.wsgi:application'

# Server Mechanics
#========================================
# current directory
chdir = '.'

# daemon mode
daemon = False

# Server Socket
#========================================
bind = 'unix:/app/tmp/sockets/gunicorn.sock'

# Worker Processes
#========================================
workers = 4
threads = 2

#  Logging
#========================================
# access log
accesslog = '/var/log/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
errorlog = '-'
loglevel = 'info'
