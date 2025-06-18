FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install axios

COPY . .

CMD ["npm", "run", "dev"]