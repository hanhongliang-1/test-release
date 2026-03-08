# Gateway Restart SOP

## Purpose
Standard procedure for restarting the OpenClaw Gateway service when needed.

## Pre-requisites
- Access to terminal/command line
- Permission to run system commands (may require elevated access)

## Steps

### 1. Check Current Status
```bash
openclaw gateway status
```

Expected output: Shows if Gateway is running, stopped, or error state.

### 2. Stop the Service
```bash
openclaw gateway stop
```

Wait for confirmation: "Gateway stopped successfully"

### 3. Verify Stop
```bash
openclaw gateway status
```

Should show: "Gateway is not running"

### 4. Start the Service
```bash
openclaw gateway start
```

Wait for confirmation: "Gateway started successfully"

### 5. Verify Start
```bash
openclaw gateway status
```

Should show: "Gateway is running" with process ID.

## Troubleshooting

### Gateway won't start
- Check if port is in use: `lsof -i :5678`
- Check logs: `openclaw gateway logs`
- Restart with elevated permissions if needed

### Gateway crashes immediately
- Check workspace permissions: `ls -la ~/.openclaw/workspace_stock`
- Verify config file is valid JSON
- Review system logs for errors

## Notes
- Gateway manages all agent sessions and skill execution
- Restart may disconnect active agents temporarily
- Schedule restarts during low-activity periods
