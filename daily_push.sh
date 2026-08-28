#!/bin/bash

# === DailyGrind Logger ===
TODAY=$(date +%F)
LOG_FILE="logs/daily-log.md"
UPDATED=false

is_logged() {
  local file_path="$1"
  local previous_path="$file_path"

  # Keep old log entries valid after moving DSA solutions into Personal DSA Journey.
  previous_path=${previous_path#personal-dsa-journey/}

  awk -v file="$file_path" -v old_file="$previous_path" '
    index($0, file) || index($0, old_file) { found = 1; exit }
    END { exit !found }
  ' "$LOG_FILE"
}

log_entry() {
  SECTION_NAME=$1
  FOLDER=$2

  # A track can be added before its first piece of work exists.
  [ -d "$FOLDER" ] || return

  while IFS= read -r FILE; do
    [ -e "$FILE" ] || continue
    FILENAME=$(basename "$FILE")
    FILE_PATH=${FILE#./}

    # Log each file once, including files recorded before a folder was renamed.
    if is_logged "$FILE_PATH"; then
      echo "⚠️ Already logged: $FILE_PATH – Skipping."
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
  done < <(find "$FOLDER" -type f ! -name 'README.md' ! -name '.gitkeep')
}

# Finished tracks (ISI internship, MIT MicroMasters, GFG Data Science, and earlier
# ML projects) are kept in the repository for reference but are not daily-logged.
log_entry "LeetCode (Personal DSA)" "personal-dsa-journey/leetcode"
log_entry "Coding Ninjas (Personal DSA)" "personal-dsa-journey/codingninjas"
log_entry "IITM Academics — MFDS, FML & DSDS" "iitm-academics"
log_entry "WorldQuant Computer Vision" "worldquant-computer-vision"
log_entry "Computer Vision & Deep Learning" "ComputerVision&DL"

if [ "$UPDATED" = false ]; then
  echo "⚠️ No new files found for today (or all already logged)."
else
  git add .
  git commit -m "✅ Daily update: $TODAY"
  git push
  echo "🚀 Green square secured. Nothing else to do 😎"
fi
