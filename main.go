package main

import (
	"github.com/gofiber/fiber/v2"
	configs "github.com/khoramism/cooljob/pkg/config"
	"github.com/khoramism/cooljob/pkg/middleware"
	"github.com/khoramism/cooljob/pkg/routes"
	"github.com/khoramism/cooljob/pkg/utils"
)

func main() {

	app := fiber.New(configs.FiberConfig())

	// Middlewares.
	middleware.FiberMiddleware(app) // Register Fiber's middleware for app.

	routes.SwaggerRoute(app)  // Register a route for API Docs (Swagger).
	routes.PublicRoutes(app)  // Register a public routes for app.
	routes.NotFoundRoute(app) // Register route for 404 Error.

	utils.StartServerWithGracefulShutdown(app)
}
