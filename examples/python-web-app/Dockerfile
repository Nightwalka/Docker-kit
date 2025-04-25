FROM ubuntu

WORKDIR /app

COPY requirements.txt /app/
COPY devops /app/

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create and activate virtual environment
RUN python3 -m venv venv1 && \
    . venv1/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Use bash to run the command and activate the virtual environment
CMD ["bash", "-c", "source venv1/bin/activate && python3 manage.py runserver 0.0.0.0:8000"]
