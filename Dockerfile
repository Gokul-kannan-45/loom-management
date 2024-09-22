FROM python:3.13.0a4-slim-bullseye
WORKDIR /src
COPY src /src
RUN pip install --no-cache-dir -r req.txt
CMD ["sh","-c", "python main.py"]


