package database

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
)

func GetHits(index_name, company, title, city, detail string) ([]JobPost, error) {
	var (
		result map[string]interface{}
	)

	es := CreateClient()

	QueryBody, err := QueryGenerator(company, title, city, detail)

	if err != nil {
		log.Fatalln("Generate the Query")
		return nil, err
	}

	res, err := es.Search(
		es.Search.WithContext(context.Background()),
		es.Search.WithIndex(index_name), // Replace with your index name
		es.Search.WithBody(QueryBody),
		es.Search.WithTrackTotalHits(true),
		es.Search.WithPretty(),
	)

	if err != nil {
		log.Fatalln("Failed to search")
		return nil, err
	}

	// Declaration of error
	if res.IsError() {
		var e map[string]interface{}
		if err := json.NewDecoder(res.Body).Decode(&e); err != nil {
			log.Fatalf("Error parsing the response body: %s", err)
			return nil, err
		} else {
			// Print the response status and error information.
			log.Fatalf("[%s] %s: %s",
				res.Status(),
				e["error"].(map[string]interface{})["type"],
				e["error"].(map[string]interface{})["reason"],
			)
		}
	}

	if err := json.NewDecoder(res.Body).Decode(&result); err != nil {
		log.Fatalf("Error parsing the response body: %s", err)
		return nil, err
	}
	log.Printf(
		"[%s] %d hits; took: %dms",
		res.Status(),
		int(result["hits"].(map[string]interface{})["total"].(map[string]interface{})["value"].(float64)),
		int(result["took"].(float64)),
	)

	var allJobPosts []JobPost

	for _, hit := range result["hits"].(map[string]interface{})["hits"].([]interface{}) {
		fmt.Println(hit.(map[string]interface{})["_source"])
		thisJob := JobPost{
			Team:     hit.(map[string]interface{})["_source"].(map[string]interface{})["team"].(string),
			Location: hit.(map[string]interface{})["_source"].(map[string]interface{})["location"].(string),
			Title:    hit.(map[string]interface{})["_source"].(map[string]interface{})["title"].(string),
			Company:  hit.(map[string]interface{})["_source"].(map[string]interface{})["company"].(string),
			Detail:   hit.(map[string]interface{})["_source"].(map[string]interface{})["detail"].(string),
			URL:      hit.(map[string]interface{})["_source"].(map[string]interface{})["url"].(string),
		}
		allJobPosts = append(allJobPosts, thisJob)
	}
	return allJobPosts, nil
}
