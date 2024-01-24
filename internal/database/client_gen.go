package database

import (
	"fmt"
	"log"
	"os"

	"github.com/elastic/go-elasticsearch/v8"
	"github.com/joho/godotenv"
)

func CreateClient() *elasticsearch.Client {
	err := godotenv.Load(".env")
	if err != nil {
		panic(err.Error())
	}
	elUsername := os.Getenv("ELASTIC_USERNAME")
	elPassword := os.Getenv("ELASTIC_PASSWORD")

	connection_url := fmt.Sprintf("http://%s:%s@elasticsearch:9200", elUsername, elPassword)
	cfg := elasticsearch.Config{
		Addresses: []string{connection_url},
	}

	es, err := elasticsearch.NewClient(cfg)
	if err != nil {
		log.Fatalln("We Failed to Create a Client in ElasticSearch")
	}
	return es
}
