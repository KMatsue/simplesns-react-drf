FROM node:20-alpine
# FROM node:20

# Install basic development tools
RUN apk update && \
    apk add git

# RUN apt update && \
#     apt install -y vim less

ENV NODE_ENV=development

WORKDIR /usr/src/app

COPY package.json ./
RUN npm install

COPY . ./