package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	configs "github.com/khoramism/cooljob/utils/config"
	"github.com/khoramism/cooljob/utils/middleware"
	"github.com/khoramism/cooljob/utils/routes"
)

func main() {

	app := fiber.New(configs.FiberConfig())

	
	// Middlewares.
	middleware.FiberMiddleware(app) // Register Fiber's middleware for app.

	
	routes.SwaggerRoute(app)  // Register a route for API Docs (Swagger).
	routes.PublicRoutes(app)  // Register a public routes for app.
	routes.NotFoundRoute(app) // Register route for 404 Error.

	// utils.StartServer(app)
	fiberConnURL := "0.0.0.0:8585"
	err := app.Listen(fiberConnURL)
	if err != nil {
		log.Fatalln(err)
	}
}
