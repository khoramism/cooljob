package middleware

import (
	"context"
	"encoding/json"
	"log"

	"github.com/go-redis/redis/v8"
	"github.com/gofiber/fiber/v2"
	"github.com/khoramism/cooljob/internal/caching"
	"github.com/khoramism/cooljob/internal/database"
)

func CachingMiddleware(c *fiber.Ctx) error {

	jobTitle := c.Params("title")
	var jobPosts []database.JobPost // Replace with your job post type

	cachedData, err := caching.CreateClient().Get(context.Background(), jobTitle).Result()
	if err == redis.Nil {
		// Cache miss, log and proceed to the next middleware
		log.Printf("Cache miss for key: %s", jobTitle)
		// return c.Next()
	} else if err != nil {
		// Handle potential Redis errors
		log.Println("Error retrieving from cache:", err)
		// return c.JSON(fiber.Map{
		// 	"error": true,
		// 	"data":  err.Error(),
		// })
		// c.Next()
	} else {
		err = json.Unmarshal([]byte(cachedData), &jobPosts)
		if err != nil {
			// handle error
			log.Println("Error unmarshalling cached data:", err)
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
				"error": true,
				"data":  err.Error(),
			})
		}
	}

	// Cache hit, send the response from cache
	err = json.Unmarshal([]byte(cachedData), &jobPosts)
	if err != nil {
		// handle error
		log.Println("Error unmarshalling cached data:", err)
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": true,
			"data":  err.Error(),
		})
	}

	return c.JSON(jobPosts)

}
