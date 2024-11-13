FROM  python:3.11.9-alpine3.20
WORKDIR /app
COPY . .
# RUN pip install
ENV API_URL http://example.com /API_URL
EXPOSE 8000
RUN addgroup app && adduser -S -G app app
USER app