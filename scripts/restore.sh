#!/bin/bash
set -e

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v mobigreen_postgres_data:/volume \
  -v ~/borg_repo:/repo \
  borgbackup/borg extract /repo::"$1"
