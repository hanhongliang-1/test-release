#!/bin/bash
echo "=== Testing daily-report-writer ==="
ls -la skills/daily-report-writer/ 2>/dev/null

echo ""
echo "=== Testing business-model-canvas ===" 
ls -la skills/business-model-canvas/ 2>/dev/null

echo ""
echo "=== Testing marketing-mode ==="
ls -la skills/marketing-mode/ 2>/dev/null

echo ""
echo "=== Testing feishu-calendar ==="
ls -la skills/feishu-calendar/ 2>/dev/null

echo ""
echo "=== Summary ==="
echo "Total skills: $(ls -d skills/*/ 2>/dev/null | wc -l)"
