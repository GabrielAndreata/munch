FROM python:3.10

WORKDIR /munch

COPY ./requirements.txt /munch/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /munch/requirements.txt

COPY ./app /munch/app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]