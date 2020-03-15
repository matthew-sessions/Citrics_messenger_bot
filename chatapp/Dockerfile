FROM python:3.6
MAINTAINER Matthew Sessions "matthewlsessions@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ACCESS_KEY=jkekal6d6e5si3i2ld66d4dl
ENV MONGO_URI=mongodb+srv://admin:rNuKKxAX3UL59FIt@cluster0-xt3at.mongodb.net/citydata?retryWrites=true&w=majority
ENV SQLALCHEMY_DATABASE_URI=postgres://hipuvjcl:IeSzNxtK-dT3K9ZEQ_TkM-pzWmG9mdnR@drona.db.elephantsql.com:5432/hipuvjcl
ENV verify_token=jkekal6d6e5si3i2ld66d4dl
ENV token=EAAJWLXZAZC6bABAH9CJuj1YeAtOmFgVxcddZCdvmNGZCCPCaigCvnI6NOI5zO4V8ZBc4CgtC4q2Y18wLeTZA1JiIhMDiy5HFn6ZAp5ZAMOJkhIZCcGqOeoVgU0gLxRzZBRNQAlVjR5lEocvaWIC50G1c65CTNPPG7V6zmhEbs0NeCse39iQdu4Bwsy72Jj1RwjZBr8ZD
ENV SITE=https://image.matthewlsessions.com
ENV page_id=101328654803716
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]