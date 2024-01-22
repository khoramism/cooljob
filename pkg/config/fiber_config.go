package configs

import (
	"time"

	"github.com/gofiber/fiber/v2"
)

// FiberConfig func for configuration Fiber app.
func FiberConfig() fiber.Config {
	// Define server settings.
	readTimeoutSecondsCount := 100

	// Return Fiber configuration.
	return fiber.Config{
		Prefork:       true,
		CaseSensitive: true,
		ReadTimeout:   time.Second * time.Duration(readTimeoutSecondsCount),
		AppName:       "CoolJob",
	}
}
