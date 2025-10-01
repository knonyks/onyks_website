FROM python:3.13

RUN mkdir /app
WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

RUN git clone https://github.com/knonyks/onyks_website.git
#COPY onyks_website onyks_website

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r onyks_website/requirements.txt

RUN useradd app
RUN chown -R  app:app onyks_website
USER app

WORKDIR onyks_website

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
