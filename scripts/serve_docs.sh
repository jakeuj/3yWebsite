#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"
if ! command -v bundle >/dev/null 2>&1; then
  echo "bundle command not found. Install Ruby Bundler first." >&2
  exit 1
fi
bundle exec jekyll serve --source docs --livereload "$@"
