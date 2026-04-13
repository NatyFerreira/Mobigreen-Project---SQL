#!/bin/bash
set -e

export BORG_PASSPHRASE="${BORG_PASSPHRASE}"

REPO="$HOME/borg_repo"
ARCHIVE="$1"

if [ -z "$ARCHIVE" ]; then
  echo "Uso: ./restore.sh <nome-da-archive>"
  exit 1
fi

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v mobigreen_postgres_data:/volume \
  -v "$REPO":/repo \
  borgbackup/borg extract /repo::"$ARCHIVE"
