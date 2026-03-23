package core

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"runtime/debug"
	"syscall"
	"time"

	"github.com/getsentry/sentry-go"
	"github.com/sirupsilon/gotenberg/internal/config"
)

func SentryInit() {
	sentryInit := func() {
		dsn := config.Config.SentryDsn
		if dsn != "" {
			sentry.Init(sentry.ClientOptions{
				Dsn: dsn,
			})
		}
	}
	defer func() {
		if r := recover(); r != nil {
			debug.PrintStack()
			if err, ok := r.(error); ok {
				log.Println(err)
			}
			time.Sleep(1 * time.Second)
			os.Exit(1)
		}
	}()
	sentryInit()
}

func HandleSignals() {
	signalCh := make(chan os.Signal, 1)
	signal.Notify(signalCh, syscall.SIGINT, syscall.SIGTERM)
	go func() {
		<-signalCh
		if err := os.Remove("core.pid"); err != nil && !os.IsNotExist(err) {
			log.Printf("Error removing PID file: %v", err)
		}
		close(signalCh)
		os.Exit(0)
	}()
}