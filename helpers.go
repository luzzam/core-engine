package coreengine

import (
	"errors"
	"fmt"
	"log"
	"net/http"
	"strings"
	"time"
)

// HandleError handles errors in a standardized way
func HandleError(err error) {
	if err != nil {
		log.Println(err)
	}
}

// IsEmpty checks if a string is empty
func IsEmpty(s string) bool {
	return strings.TrimSpace(s) == ""
}

// IsValidURL checks if a URL is valid
func IsValidURL(url string) bool {
	_, err := http.Get(url)
	if err != nil {
		return false
	}
	return true
}

// GetCurrentTime returns the current time
func GetCurrentTime() time.Time {
	return time.Now().UTC()
}

// ValidateInput validates input parameters
func ValidateInput(params map[string]string) error {
	if params == nil {
		return errors.New("params cannot be nil")
	}
	for key, value := range params {
		if IsEmpty(value) {
			return fmt.Errorf("param %s cannot be empty", key)
		}
	}
	return nil
}