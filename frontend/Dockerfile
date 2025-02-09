FROM node:23 AS builder
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . . 
RUN npm run build


FROM node:22-slim AS runner
WORKDIR /app

COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 5173
CMD ["node", "build"]
