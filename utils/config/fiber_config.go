package configs

import (
	"strings"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/compress"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"github.com/gofiber/fiber/v2/middleware/limiter"
	"github.com/gofiber/fiber/v2/middleware/logger"
)

// FiberConfig func for configuration Fiber app.
func FiberConfig() fiber.Config {
	// Define server settings.
	readTimeoutSecondsCount := 100

	// Return Fiber configuration.
	return fiber.Config{
		Prefork:       false,
		CaseSensitive: true,
		ReadTimeout:   time.Second * time.Duration(readTimeoutSecondsCount),
		AppName:       "CoolJob",
	}
}

func CompressionConfig() compress.Config {
	return compress.Config{
		Next:  nil,
		Level: compress.LevelBestCompression,
	}
}

func CorsConfig() cors.Config {
	return cors.Config{
		AllowOrigins: "https://cooljob.ir",
		AllowHeaders: "Origin, Content-Type, Accept",

		// We don't need more methods yet
		AllowMethods: strings.Join([]string{
			fiber.MethodGet,
			fiber.MethodHead,
		}, ","),
	}
}

func LoggerConfig() logger.Config {
	return logger.Config{
		Format:     "[${ip}]:${port} ${status} - ${method} ${path}\n",
		TimeFormat: "2006-01-02",
		TimeZone:   "Asia/Tehran",
	}
}

func LimiterConfig() limiter.Config {
	return limiter.Config{
		Next: func(c *fiber.Ctx) bool {
			return c.IP() == "https://cooljob.ir"
		},
		Max:        20,
		Expiration: 30 * time.Second,
		KeyGenerator: func(c *fiber.Ctx) string {
			return c.Get("x-forwarded-for")
		},
		LimitReached: func(c *fiber.Ctx) error {
			return c.Redirect("https://www.google.com/search?&q=bad+boy")
		},
	}
}

// func RedisConfig() redis.Config {
// 	return redis.Config{
// 		Host:      "redis-db",
// 		Port:      6379,
// 		Username:  "",
// 		Password:  "",
// 		Database:  0,
// 		Reset:     false,
// 		TLSConfig: nil,
// 		PoolSize:  10 * runtime.GOMAXPROCS(0),
// 	}
// }
