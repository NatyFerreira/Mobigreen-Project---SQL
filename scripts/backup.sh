#!/bin/bash
set -e

export BORG_PASSPHRASE="${BORG_PASSPHRASE}"

REPO="$HOME/borg_repo"
ARCHIVE="backup-postgres-$(date +%Y-%m-%d-%H%M%S)"

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v mobigreen_postgres_data:/volume \
  -v "$REPO":/repo \
  borgbackup/borg create \
    --compression zstd \
    --stats \
    /repo::"$ARCHIVE" \
    /volume

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v "$REPO":/repo \
  borgbackup/borg check /repo::"$ARCHIVE"

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v "$REPO":/repo \
  borgbackup/borg prune \
    --keep-daily=7 \
    --keep-weekly=4 \
    --keep-monthly=6 \
    /repo
