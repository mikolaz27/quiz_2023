FROM python:3.10

RUN apt update
RUN mkdir /quizez

WORKDIR /quizez

COPY ./src ./src
COPY ./commands ./commands

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["bash"]