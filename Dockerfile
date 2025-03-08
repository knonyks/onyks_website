FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
RUN git clone https://github.com/knonyks/onyks_website.git


RUN pip install --no-cache-dir -r onyks_website/requirements.txt


RUN useradd app
# Setup an app user so the container doesn't run as the root user
RUN chown -R  app app onyks_website
WORKDIR ./onyks_website
USER app

CMD ["python", "manage.py", "runserver"]