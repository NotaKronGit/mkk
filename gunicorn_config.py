command = '/home/sergey/pyproject/djreport/bin/gunicorn'
pythonpath = '/home/sergey/pyproject/mkk'
bind = '0.0.0.0:8001'
workers = 3
user = 'sergey'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=mkk.settings'
