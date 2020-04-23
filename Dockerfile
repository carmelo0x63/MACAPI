FROM python:3-alpine3.9
MAINTAINER "carmelo.califano@gmail.com"
RUN apk add --no-cache curl
WORKDIR /app
COPY macapi.py .
ENTRYPOINT ["/app/macapi.py"]
