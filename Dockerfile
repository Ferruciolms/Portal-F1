FROM python:3.12

COPY portal_f1/applications applications
COPY portal_f1/core core
COPY portal_f1/core_access core_access
COPY portal_f1/core_log core_log
COPY portal_f1/core_pages core_pages
COPY portal_f1/core_registration core_registration
COPY portal_f1/gunicorn/gunicorn-cfg.py gunicorn-cfg.py
COPY portal_f1/static static
COPY portal_f1/staticfiles staticfiles
COPY portal_f1/manage.py .
COPY requirements.txt .
COPY portal_f1/.env .

RUN pip install -r requirements.txt

WORKDIR .
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]