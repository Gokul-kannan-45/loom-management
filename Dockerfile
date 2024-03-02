FROM python:3.13.0a4-slim-bullseye
WORKDIR /src
COPY src /src
COPY req.txt req.txt
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install --no-cache-dir -r req.txt
CMD ["sh","-c", "python main.py"]


