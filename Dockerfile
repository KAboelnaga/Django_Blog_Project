# استخدم Python image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# استخدم pip مع retry و mirror لتقليل المشاكل
RUN pip install --upgrade pip \
    && pip install -r requirements.txt 

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]