FROM python:3.12-slim

WORKDIR /countries

COPY requirements.txt /countries/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /countries/

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
