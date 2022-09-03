FROM python:3.7.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends python3-dev \
    default-libmysqlclient-dev libgomp1 build-essential cmake libboost-all-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && pip install -U pip==21.3.1 --no-cache-dir

RUN mkdir -p /opt/
ARG project_dir=/opt/
ADD . $project_dir
WORKDIR $project_dir

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
ENTRYPOINT ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80", "--forwarded-allow-ips", "*", "--timeout-keep-alive", "90"]
