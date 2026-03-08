# 飞书集成配置

## Webhook URL
```
https://open.feishu.cn/open-apis/bot/v2/hook/ceab419d-7560-47e4-a731-452628c9c211
```

## 飞书文档配置
**文档地址**: https://ocn7qwdoevu4.feishu.cn/wiki/Westwcumdi5AKckknlycezganKe  
**Doc Token**: `Westwcumdi5AKckknlycezganKe`  
**用途**: CEO 日报自动同步

## 使用方式
- **日报推送**: 每日 24:00 GMT+8 自动发送 CEO 日报到群聊 + 更新文档
- **紧急通知**: 重大事件/风险预警实时推送到群聊
- **里程碑庆祝**: 重要节点达成时推送

## 定时任务配置
- **频率**: 每日 24:00 GMT+8
- **触发器**: cron job (0 0 * * *)
- **执行脚本**: generate-and-send-daily-report.sh
