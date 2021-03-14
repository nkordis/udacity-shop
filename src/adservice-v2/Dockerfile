FROM python:3.7-slim
RUN apt-get update -qqy && \
    apt-get -qqy install wget g++ && \
    rm -rf /var/lib/apt/lists/*
# show python logs as they occur
ENV PYTHONUNBUFFERED=0

# download the grpc health probe
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.6 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe


# TODO: Place Dockerfile instructions below
# Copy files from host to the container filesystem
COPY . /app
#  Set the working directory within the container
WORKDIR /app
# Install dependencies defined in requirements.txt file
RUN pip install -r requirements.txt
# Expose the container port
EXPOSE 9556
# Run on container start 
CMD ["python", "adservice-v2.py"]