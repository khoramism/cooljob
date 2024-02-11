package caching

import (
	"context"
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
)

var ctx = context.Background()

func CreateClient() *redis.Client {
	err := godotenv.Load(".env")
	if err != nil {
		panic(err.Error())
	}
	REDIS_PASSWORD := os.Getenv("REDIS_PASS")

	redisClient := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379", // or the address of your Redis server
		Password: REDIS_PASSWORD,   // no password set
		DB:       0,                // use default DB
	})
	pong, err := redisClient.Ping(ctx).Result()
	if err != nil {
		// If there is an error, log it
		log.Fatalf("Failed to connect to Redis: %v", err)
	} else {
		// If successful, log the pong response
		log.Printf("Connected to Redis: %s", pong)
	}
	return redisClient
}
