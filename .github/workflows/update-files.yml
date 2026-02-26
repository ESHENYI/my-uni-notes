name: Update Files JSON

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '23 03 * * *'
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: update-files-json
  cancel-in-progress: false

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Pull latest main (safety)
        run: |
          git fetch origin main
          git checkout main
          git pull --rebase origin main

      # ✅ Detect if anything inside files/ changed
      - name: Check if files folder changed
        id: files_changed
        run: |
          echo "Checking for changes in files/..."

          # Handle first commit safely
          if [ "${{ github.event.before }}" = "0000000000000000000000000000000000000000" ]; then
            echo "First commit detected — running generator."
            echo "changed=true" >> $GITHUB_OUTPUT
            exit 0
          fi

          if git diff --name-only ${{ github.event.before }} ${{ github.sha }} | grep '^files/'; then
            echo "Changes detected in files/."
            echo "changed=true" >> $GITHUB_OUTPUT
          else
            echo "No changes in files/."
            echo "changed=false" >> $GITHUB_OUTPUT
          fi

      # ✅ Only run generator if files changed
      - name: Run the generator
        if: steps.files_changed.outputs.changed == 'true'
        run: python update_files.py

      # Optional debug output
      - name: Show generated files.json (for debugging)
        if: steps.files_changed.outputs.changed == 'true'
        run: |
          echo "====== files.json ======"
          cat files.json || true
          echo "========================"

      # ✅ Only commit if files changed AND files.json changed
      - name: Commit and push if files.json changed
        if: steps.files_changed.outputs.changed == 'true'
        run: |
          if git diff --quiet -- files.json; then
            echo "files.json unchanged. Exiting."
            exit 0
          fi

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add files.json
          git commit -m "Auto-update files.json [skip ci]" || exit 0
          (git push origin main) || (git pull --rebase origin main && git push origin main)
