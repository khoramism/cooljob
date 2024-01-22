package database

import (
	"bytes"
	"encoding/json"
	"fmt"
)

func QueryGenerator(company string, title string, city string, detail string) (*bytes.Reader, error) {
	query := map[string]interface{}{
		"query": map[string]interface{}{
			"bool": map[string]interface{}{
				"should": []interface{}{
					map[string]interface{}{
						"match": map[string]interface{}{
							"company": company,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"company.english": company,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"title": title,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"title.english": title,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"city": city,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"city.english": city,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"detail": detail,
						},
					},
					map[string]interface{}{
						"match": map[string]interface{}{
							"detail.english": detail,
						},
					},
				},
			},
		},
	}
	jsonBytes, err := json.Marshal(query)

	if err != nil {
		fmt.Printf("Error marshaling the query: %v\n", err)
		return nil, err
	}
	reader := bytes.NewReader(jsonBytes)

	// Read data from the reader

	if err != nil {
		fmt.Printf("Error reading from reader: %v\n", err)
		return nil, err
	}
	return reader, nil

}
