FROM python:3.6

ADD . /Scraping-and-Analysis-on-Sneakers

COPY . /Scraping-and-Analysis-on-Sneakers

WORKDIR /Scraping-and-Analysis-on-Sneakers

RUN pip install -r requirements.txt
