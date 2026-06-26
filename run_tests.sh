#!/bin/bash
SUITE=${1:-"all"}
REPORT_DIR="reports/allure-results"

# Clean previous results
rm -rf $REPORT_DIR
mkdir -p $REPORT_DIR

echo "Running $SUITE suite..."
if [ "$SUITE" = "smoke" ]; then
    pytest tests/ -v -m smoke --alluredir=$REPORT_DIR
elif [ "$SUITE" = "regression" ]; then
    pytest tests/ -v -m regression --alluredir=$REPORT_DIR
else
    pytest tests/ -v --alluredir=$REPORT_DIR
fi

echo "Generating Allure report..."
/opt/homebrew/bin/allure serve $REPORT_DIR