FROM node:14

RUN apt-get update && apt-get -y install iputils-ping protobuf-compiler
RUN apt-get -y install net-tools 
RUN npm install -g grpc-tools

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

COPY ./protos ./protos

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080 50051
CMD [ "node", "protos/server.js" ]