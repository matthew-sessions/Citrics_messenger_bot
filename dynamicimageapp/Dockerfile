FROM python:3.6
MAINTAINER Matthew Sessions "matthewlsessions@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV MONGO_URI=mongodb+srv://admin:rNuKKxAX3UL59FIt@cluster0-xt3at.mongodb.net/citydata?retryWrites=true&w=majority
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]