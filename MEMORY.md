# MEMORY.md - Long-Term Memory

_Curated wisdom, key decisions, and lessons learned._

## Company Foundation

### Launch Date: 2026-02-28
- **Product**: 社交媒体内容自动化 (Social Media Content Automation)
- **Budget**: $500 lean startup allocation
- **Team Structure**: CEO + CTO + CMO + CFO (all independent Agents)

### Core Principles
1. **Profit First** - All decisions evaluated by financial health and long-term profitability
2. **Data-Driven** - No major decision without data; collect market intelligence first
3. **Risk Awareness** - Pause and escalate when risks are uncontrollable
4. **Transparent Logging** - All important decisions logged for traceability

## Key Decisions Log

### 2026-02-28
- ✅ Approved $500 lean startup budget (A Plan)
- ✅ Product direction: Social media content automation for SMBs/personal brands
- ✅ Team assembled: CTO (TechNinja), CMO (GrowthHacker), CFO (MoneyGuard)
- ✅ Decision authority: CEO has $5,000 autonomous spending limit per department

## Lessons Learned

### Technical Standards
- All employees MUST be independent Agent instances (not simulated via conversation or skills)
- Configuration changes require `clawddocs` skill verification before execution
- Each Agent needs independent memory, skills, and SOUL.md

### Operational Rhythms
- Daily reports to founder via Feishu by 24:00
- Weekly deep-dive review of profitability, team efficiency, market opportunities
- Bi-weekly `clawddocs` sync to keep OpenClaw documentation current

## Budget Allocation (Initial)
| Category | Amount | % | Status |
|----------|--------|---|--------|
| AI/API | $200 | 40% | Allocated |
| Infrastructure | $100 | 20% | Allocated |
| Marketing/Acquisition | $150 | 30% | Allocated |
| Emergency Reserve | $50 | 10% | Reserved |

## Product Definition: Social Media Content Automation
- **Target**: SMBs, personal brand owners
- **Features**: 
  - Auto-crawl industry hotspots/competitor dynamics
  - AI-generated multi-platform copy (Twitter/LinkedIn/Xiaohongshu)
  - Scheduled publishing
- **Delivery**: 1-2 days
- **Pricing**: $100-$300/month

## Next Milestones
- [x] **记忆系统升级** (2026-03-02) - Elite Longterm Memory + Qwen embedding ✅
- [ ] CTO: MVP technical architecture design
- [ ] CMO: Build target customer list (50+)
- [ ] CFO: Budget tracking spreadsheet + daily report template
- [ ] First revenue within 2 weeks of launch

---

## 🧠 Memory System (2026-03-02 Upgrade)

### Architecture
```
HOT RAM (SESSION-STATE.md) → WARM (memory/YYYY-MM-DD.md) → COLD (MEMORY.md)
                              ↓
                    Vector Index (Qwen embedding, 1024 dims)
```

### Configuration
- **Provider**: Local Qwen (`text-embedding-qwen3-embedding-0.6b`)
- **Endpoint**: `http://127.0.0.1:1234/v1/` (MLX local)
- **Indexed**: 48 files, 99 chunks (stock-ceo agent)
- **Status**: ✅ Fully operational

### Capabilities
✅ Session persistence via SESSION-STATE.md  
✅ Semantic search across all memory files  
✅ WAL protocol (write-before-respond)  
✅ Git version control for decisions  

---
*Last updated: 2026-03-02 02:15 GMT+8*
