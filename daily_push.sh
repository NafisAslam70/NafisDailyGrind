#!/bin/bash

TODAY=$(date +%F)
LOG_FILE="logs/daily-log.md"
UPDATED=false

log_entry() {
  SECTION_NAME=$1
  FOLDER=$2

  FILE=$(find "$FOLDER" -type f -name "*.*" -newermt "$TODAY" ! -newermt "$TODAY 23:59:59" | head -n 1)

  if [[ -n "$FILE" ]]; then
    FILENAME=$(basename "$FILE")
    TASK_NAME=$(echo "$FILENAME" | sed "s/\..*//;s/_/ /g" | sed 's/\b\(.\)/\u\1/g')

    # Check if already logged
    if grep -q "$FILENAME" "$LOG_FILE"; then
      echo "⚠️ Already logged: $FILENAME – Skipping."
      return
    fi

    # Ask user for image
    echo "🖼️ Do you want to attach a picture for notes? (y/n)"
    read ADD_IMAGE

    IMAGE_MARKDOWN=""
    if [[ "$ADD_IMAGE" == "y" || "$ADD_IMAGE" == "Y" ]]; then
      echo "📂 Please move your image (png/jpg) to 'notes-images/' and enter the filename (e.g. mynote.png):"
      read IMAGE_FILE
      IMAGE_PATH="notes-images/$IMAGE_FILE"

      if [[ -f "$IMAGE_PATH" ]]; then
        IMAGE_MARKDOWN="![Note Image]($IMAGE_PATH)"
      else
        echo "⚠️ File not found. Skipping image."
      fi
    fi

    # Create log entry
    sed -i '' "2i\\
\\
## ✅ $TODAY\\
\\
**$SECTION_NAME:**\\
- [x] $TASK_NAME\\
- 📁 File: \`$FOLDER/$FILENAME\`\\
\\
📝 Notes:\\
- Practiced key concepts.\\
$IMAGE_MARKDOWN\\
\\
---\\
" $LOG_FILE

    echo "✅ Logged: $TASK_NAME in $FOLDER"
    UPDATED=true
  fi
}

log_entry "LeetCode" "leetcode"
log_entry "Coding Ninjas" "codingninjas"
log_entry "ML Projects" "ml-projects"
log_entry "MIT MicroMasters" "mit-micromasters"
log_entry "GFG Data Science" "gfg-ds"

if [ "$UPDATED" = false ]; then
  echo "⚠️ No new files found for today (or already logged)."
  exit 0
fi

# Git commit and push
git add .
git commit -m "✅ Daily update: $TODAY"
git push

echo "🚀 All done! Green square + visual proof locked in!"
