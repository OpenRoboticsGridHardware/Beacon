FROM ubuntu:20.04
WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    python3 \
    python3-pip \
    tzdata \
    && rm -rf /var/lib/apt/lists/*
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000 8765
CMD ["bash", "-c", "python3 cod_rgb.py & python3 main-camera.py"]