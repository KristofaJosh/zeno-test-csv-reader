FROM node

MAINTAINER Chris Josh "christopherjoshua25@hotmail.com"

WORKDIR /zeno_task/frontend

COPY package.json /zeno_task/frontend
COPY yarn.lock /zeno_task/frontend

RUN yarn install
COPY . /zeno_task/frontend

EXPOSE 3000

CMD ["yarn", "start"]

