package main

import (
	"fmt"

	"github.com/khoramism/cooljob/internal/database"
)

func main() {

	// Print the ID and document source for each hit.
	// for _, hit := range r["hits"].(map[string]interface{})["hits"].([]interface{}) {
	// 	log.Printf(" * ID=%s, %s", hit.(map[string]interface{})["_id"], hit.(map[string]interface{})["_source"])
	// }

	// log.Println(strings.Repeat("=", 37))

	// defer res.Body.Close()

	response, err := database.GetHits("cool_job", "digikala", "", "", "")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%v\n", response)
}
