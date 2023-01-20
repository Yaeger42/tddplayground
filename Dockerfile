FROM python:3.9
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt 
COPY . /app/ 
RUN pip install -e .
