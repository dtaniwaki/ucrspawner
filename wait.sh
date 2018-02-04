#!/bin/bash

set -e

until curl -sf --connect-timeout 1 "$MARATHON_HOST"; do
  >&2 echo "Marathon is unavailable - sleeping"
  sleep 3
done


>&2 echo "Ready to start - executing command"
exec $@
