package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net/http"
)

type APIResponse struct {
	Data       interface{} `json:"data"`
	StatusCode int         `json:"status_code"`
	StatusText string      `json:"status_txt"`
}

func main() {
	var (
		port = flag.Int("port", 11000, "port on which to listen for incoming http requests")
	)

	flag.Parse()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// get request args
		var data = map[string]string{
			"key1":  r.FormValue("key1"),
			"key2":  r.FormValue("key2"),
			"key3":  r.FormValue("key3"),
			"key4":  r.FormValue("key4"),
			"key5":  r.FormValue("key5"),
			"key6":  r.FormValue("key6"),
			"key7":  r.FormValue("key7"),
			"key8":  r.FormValue("key8"),
			"key9":  r.FormValue("key9"),
			"key10": r.FormValue("key10"),
		}
		// format into APIResponse
		var resp_body = APIResponse{
			Data:       data,
			StatusCode: 200,
			StatusText: "OK",
		}
		// convert to JSON
		resp_json, err := json.Marshal(resp_body)
		if err != nil {
			fmt.Println("error:", err)
		}
		// write header
		w.Header().Set("Content-Type", "application/json; charset=utf-8")
		// write response body
		w.Write(resp_json)
	})

	addr := fmt.Sprintf(":%d", *port)
	log.Fatal(http.ListenAndServe(addr, nil))
}
