FROM golang:1.21.6

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . ./

EXPOSE 8585 

RUN CGO_ENABLED=0 GOOS=linux go build -o /app/cooljob-api

ENTRYPOINT ["/app/cooljob-api"]
