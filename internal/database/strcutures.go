package database

type JobPost struct {
	Team     string `json:"team"`
	Location string `json:"location"`
	Title    string `json:"title"`
	Company  string `json:"company"`
	Detail   string `json:"detail"`
	URL      string `json:"url"`
}
