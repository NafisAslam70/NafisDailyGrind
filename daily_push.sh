#!/bin/bash

TODAY=$(date +%F)
LOG_FILE="logs/daily-log.md"
UPDATED=false

log_entry() {
  SECTION_NAME=$1
  FOLDER=$2

  # List all files in folder
  for FILE in "$FOLDER"/*; do
    [ -e "$FILE" ] || continue  # skip if folder is empty

    FILENAME=$(basename "$FILE")
    
    # Skip if already logged
    if grep -q "$FILENAME" "$LOG_FILE"; then
      echo "⚠️ Already logged: $FILENAME – Skipping."
      continue
    fi

    TASK_NAME=$(echo "$FILENAME" | sed "s/\..*//;s/_/ /g" | sed 's/\b\(.\)/\u\1/g')

    # Add to log
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
\\
---\\
" $LOG_FILE

    echo "✅ Logged: $TASK_NAME in $FOLDER"
    UPDATED=true
  done
}

log_entry "LeetCode" "leetcode"
log_entry "Coding Ninjas" "codingninjas"
log_entry "ML Projects" "ml-projects"
log_entry "MIT MicroMasters" "mit-micromasters"
log_entry "GFG Data Science" "gfg-ds"

if [ "$UPDATED" = false ]; then
  echo "⚠️ No new files found for today (or all already logged)."
  exit 0
fi

# Git commit and push
git add .
git commit -m "✅ Daily update: $TODAY"
git push

echo "🚀 Green square secured. Nothing else to do 😎"
