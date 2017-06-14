FROM python:alpine3.6
MAINTAINER Tim Stoop <tim@kumina.nl>

# Copy the script in
COPY app.py /app.py
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install -r /requirements.txt


CMD ["python3", "-u", "/app.py"]
