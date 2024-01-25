package middleware

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/compress"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"github.com/gofiber/fiber/v2/middleware/limiter"
	"github.com/gofiber/fiber/v2/middleware/logger"
	configs "github.com/khoramism/cooljob/utils/config"
)

// FiberMiddleware provide Fiber's built-in middlewares.
// See: https://docs.gofiber.io/api/middleware
func FiberMiddleware(a *fiber.App) {
	a.Use(
		cors.New(configs.CorsConfig()),
		// Add simple logger.
		logger.New(configs.LoggerConfig()),
		compress.New(configs.CompressionConfig()),
		limiter.New(configs.LimiterConfig()),
	)
}
