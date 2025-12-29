#!/bin/bash

# === DailyGrind Logger ===
TODAY=$(date +%F)
LOG_FILE="logs/daily-log.md"
UPDATED=false

is_logged_today() {
  local file_path="$1"
  awk -v date="$TODAY" -v file="$file_path" '
    /^## ✅ / { in_day = ($0 == "## ✅ " date); next }
    in_day && index($0, file) { exit 0 }
    END { exit 1 }
  ' "$LOG_FILE"
}

log_entry() {
  SECTION_NAME=$1
  FOLDER=$2

  while IFS= read -r FILE; do
    [ -e "$FILE" ] || continue
    FILENAME=$(basename "$FILE")
    FILE_PATH=${FILE#./}

    # Skip if already logged today
    if is_logged_today "$FILE_PATH"; then
      echo "⚠️ Already logged today: $FILE_PATH – Skipping."
      continue
    fi

    TASK_NAME=$(echo "$FILENAME" | sed "s/\\..*//;s/_/ /g" | sed 's/\\b\\(\\.\\)/\\u\\1/g')

    sed -i '' "2i\\
\\
## ✅ $TODAY\\
\\

**$SECTION_NAME:**\\
- [x] $TASK_NAME\\
- 📁 File: \`$FILE_PATH\`\\
\\
📝 Notes:\\
- Practiced key concepts.\\
\\
---\\
" $LOG_FILE

    echo "✅ Logged: $TASK_NAME in $FILE_PATH"
    UPDATED=true
  done < <(find "$FOLDER" -type f)
}

log_entry "LeetCode" "leetcode"
log_entry "Coding Ninjas" "codingninjas"
log_entry "ML Projects" "ml-projects"
log_entry "MIT MicroMasters" "mit-micromasters"
log_entry "GFG Data Science" "gfg-dataScience"

if [ "$UPDATED" = false ]; then
  echo "⚠️ No new files found for today (or all already logged)."
else
  git add .
  git commit -m "✅ Daily update: $TODAY"
  git push
  echo "🚀 Green square secured. Nothing else to do 😎"
fi
