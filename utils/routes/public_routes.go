package routes

import (
	"github.com/gofiber/fiber/v2"
	"github.com/khoramism/cooljob/internal/controller"
)

func PublicRoutes(a *fiber.App) {
	route := a.Group("/api/v1")
	route.Get("/jobs/:title", controller.GetJobPosts) // get list of all books
}
