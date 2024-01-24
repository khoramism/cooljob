package controller

import (
	"github.com/gofiber/fiber/v2"
	"github.com/khoramism/cooljob/internal/database"
)

// GetJobPosts func gets jobposts by given title or 404 error.
//	@Description	Get job post by given title.
//	@Summary		get jobpost by given title.
//	@Tags			JobPosts
//	@Accept			json
//	@Produce		json
//	@Param			title	path		string	true	"Job Post title"
//	@Success		200		{object}	database.JobPost
//	@Router			/v1/jobs/{title} [get]
func GetJobPosts(c *fiber.Ctx) error {
	// Catch title
	title := string(c.Params("title"))

	jobPosts, err := database.GetHits("cooljob", "", "", "", title)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	// Return status 200 OK.
	return c.JSON(fiber.Map{
		"error": false,
		"data":  jobPosts,
	})
}
