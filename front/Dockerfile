FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install axios
RUN npm install vue3-cookies
RUN npm install pinia

COPY . .

CMD ["npm", "run", "dev"]