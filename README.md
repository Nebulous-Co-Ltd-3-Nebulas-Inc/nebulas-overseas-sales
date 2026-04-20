# Nebulas Overseas Sales Platform

海外営業プラットフォーム — AI リード生成・自動アウトリーチ・CRM・マーケティング統合基盤

An AI-powered full-stack platform for overseas sales automation — from lead generation to payment collection and customer success.

<div align="center">

### 🇬🇧 English

<img src="homepage 1 english.png" width="80%" alt="Homepage English 1" />
<img src="homepage 2 english.png" width="80%" alt="Homepage English 2" />

### 🇯🇵 日本語

<img src="homepage 1 japanese.png" width="80%" alt="Homepage Japanese 1" />
<img src="homepage 2 japanese.png" width="80%" alt="Homepage Japanese 2" />

</div>

---

## System Architecture

```
nebulas-dashboard (:80) → Unified Login + PWA + GDPR Consent
    │
    ├── nebulas-infra/core
    │   ├── FlowEngine → Workflow Orchestration (400+ integrations)
    │   └── Analytics  → Data Dashboards (AI-powered BI)
    │
    ├── nebulas-leadgen/core   → Multi-source Lead Scraping
    ├── nebulas-outreach/core  → AI Cold Email + Voice Pipeline
    ├── nebulas-contracts/     → E-Signature Platform
    ├── nebulas-payments/      → Payment Gateway (50+ processors)
    ├── nebulas-crm/core       → Customer Management
    ├── nebulas-marketing/core → Omnichannel Marketing + Page Builder
    ├── nebulas-experiments/   → A/B Testing + Feature Flags
    ├── nebulas-voip/          → Video Calls + AI Voice Agent
    ├── nebulas-privacy/       → GDPR/CCPA Compliance
    ├── nebulas-i18n/          → 50+ Languages + 135 Currencies
    └── nebulas-plugins/       → Social CRM (WhatsApp/IG/TG/LINE)
```

## Full Sales Cycle

```
1. nebulas-leadgen scrapes business data (Google Maps / Yelp / OSINT)
       ↓
2. FlowEngine auto-pushes new leads to nebulas-outreach
       ↓
3. nebulas-outreach researches → scores → generates personalized emails → sends
       ↓  (+ nebulas-voip for AI voice calls)
4. Interested leads receive contracts via nebulas-contracts
       ↓
5. Signed contracts trigger payment via nebulas-payments
       ↓
6. Paid customers auto-enter nebulas-crm
       ↓
7. CRM customers enter nebulas-marketing for ongoing engagement
       ↓  (+ nebulas-experiments for A/B testing email/landing pages)
8. Support tickets handled by nebulas-support
       ↓
9. All data flows into Analytics for dashboards
```

## Quick Start

```bash
# Core services only
docker compose up -d

# Full deployment (all modules)
docker compose --profile all up -d

# Or pick specific profiles
docker compose --profile marketing --profile contracts --profile payments up -d
```

Wait ~60 seconds for all services to initialize, then open:

| URL | Service | Credentials |
|-----|---------|-------------|
| http://localhost | Dashboard | admin / abc123 |
| http://localhost:81 | FlowEngine (workflow builder) | admin@nebulas.co.jp / abc123 |
| http://localhost:82 | Analytics (BI dashboards) | admin@nebulas.co.jp / Abc123!! |
| http://localhost:83 | CRM (customer management) | — |
| http://localhost:84 | Contracts (e-signature) | — |
| http://localhost:85 | Payments (control center) | — |
| http://localhost:86 | Experiments (A/B testing) | — |
| http://localhost:87 | VoIP (video conferencing) | — |


## Tech Stack

| Layer | Technologies |
|-------|-------------|
| AI / ML | Python, LangChain, LangGraph, Groq, OpenAI, ChromaDB |
| Backend | Node.js, Express, Go, Rust, Ruby on Rails, PHP |
| Frontend | Next.js 15, React 19, TypeScript, Tailwind CSS |
| Database | PostgreSQL, MongoDB, Redis, ClickHouse |
| Infrastructure | Docker, Nginx, Temporal |
| Workflow | Custom FlowEngine (400+ integrations) |
| Analytics | Custom BI Dashboard (AI-powered queries) |
| CRM | Full-featured CRM Platform |
| Marketing | Journey Builder, High-performance Mailer (Go), Live Chat, Lead Scoring |
| Payments | Rust-based Payment Router (50+ processors, 135+ currencies) |
| Contracts | E-Signature Platform (multi-party signing, eIDAS compliant) |
| Experiments | A/B Testing + Feature Flags (Bayesian statistics) |
| VoIP | WebRTC Video Conferencing (up to 8K) + AI Voice Agent |
| Privacy | GDPR/CCPA/LGPD Consent Management |
| i18n | 50+ Languages, RTL support, SSR-friendly |
| Social CRM | WhatsApp, Instagram, Telegram, LINE plugins |

## Modules

| Module | Path | Description | Key Tech |
|--------|------|-------------|----------|
| LeadGen | `nebulas-leadgen/` | Multi-source lead scraping with AI enrichment | Python, Playwright, Groq |
| Outreach | `nebulas-outreach/` | AI-powered sales outreach pipeline (8-stage sales model) | Python, LangChain, LangGraph |
| Contracts | `nebulas-contracts/` | E-signature & document signing platform | Ruby/Rails, PostgreSQL |
| Payments | `nebulas-payments/` | Unified payment gateway (50+ processors) | Rust, PostgreSQL, Redis |
| CRM | `nebulas-crm/` | Customer management with PDF/email extensions | Node.js, TypeScript, PostgreSQL |
| Marketing | `nebulas-marketing/` | Unified marketing gateway with journey builder | Node.js, Go, Express |
| Experiments | `nebulas-experiments/` | A/B testing & feature flags | Node.js, MongoDB |
| VoIP | `nebulas-voip/` | Video conferencing + AI voice agent | Node.js, Python, WebRTC |
| Privacy | `nebulas-privacy/` | GDPR/CCPA/LGPD compliance suite | JavaScript |
| i18n | `nebulas-i18n/` | Multi-language + multi-currency framework | JavaScript |
| Infra | `nebulas-infra/` | Workflow orchestration and analytics | PostgreSQL, Docker |
| Dashboard | `nebulas-dashboard/` | Unified login portal with SSO + PWA | Express, Nginx |
| Plugins | `nebulas-plugins/` | Social CRM for 4 platforms | Next.js, TypeScript |
| Extensions | `nebulas-extensions/` | ERP & HR modules | Python, PHP |

## Docker Compose Profiles

| Profile | Services Added | Ports |
|---------|---------------|-------|
| (default) | Dashboard, FlowEngine, Analytics, CRM, PDF Generator, Email Parser | :80-83, :3002-3003 |
| `marketing` | Journey Builder, Mailer, Live Chat, Lead Scoring | :8080 |
| `contracts` | E-Signature + PostgreSQL | :84 |
| `payments` | Payment Router + Control Center + Web SDK | :85, :8180, :9050 |
| `experiments` | A/B Testing + Feature Flags + MongoDB | :86, :3100 |
| `voip` | Video Engine + AI Voice Agent | :87, :5001 |
| `all` | Everything above | All ports |

## Project Structure

```
nebulas-overseas-sales/
├── nebulas-leadgen/          # Lead generation & scraping
│   ├── core/                 #   Main async pipeline
│   ├── harvester/            #   OSINT intelligence engine
│   ├── maps-scraper/         #   Google Maps review parser
│   ├── web-scraper/          #   Playwright async web scraper
│   └── enricher/             #   LLM-powered data enrichment
├── nebulas-outreach/         # AI cold outreach
│   ├── core/                 #   Research → scoring → email pipeline
│   ├── sales-agent/          #   8-stage conversational AI agent
│   ├── email-automations/    #   Multi-agent collaboration (analyst + writer)
│   ├── email-manager/        #   Template management & scheduling
│   ├── email-generator/      #   Fast LLM inference email generation
│   └── workflow/             #   LangGraph state machine with routing
├── nebulas-contracts/        # E-signature platform
├── nebulas-payments/         # Payment gateway (50+ connectors)
├── nebulas-crm/              # Customer relationship management
│   ├── core/                 #   Docker deployment + extensions
│   ├── platform/             #   Full CRM system
│   ├── erp-extensions/       #   PDF invoice/quote generation
│   └── email-crm/            #   Inbound email parsing (Laravel)
├── nebulas-marketing/        # Marketing automation
│   ├── core/                 #   Unified API gateway
│   ├── journey/              #   Customer journey builder
│   ├── mailer/               #   High-performance email engine (Go)
│   ├── chat/                 #   Omnichannel live chat
│   ├── scoring/              #   Lead scoring engine
│   └── page-builder/         #   Drag-and-drop landing pages
├── nebulas-experiments/      # A/B testing + feature flags
├── nebulas-voip/             # Video + AI voice
├── nebulas-privacy/          # GDPR/CCPA compliance
├── nebulas-i18n/             # 50+ languages + 135 currencies
│   └── locales/              #   Language packs (en/zh/ja/es/ar/...)
├── nebulas-infra/            # Infrastructure
│   ├── core/                 #   Docker Compose + auto-setup scripts
│   ├── workflow-engine/      #   Visual workflow builder
│   └── analytics/            #   BI dashboards
├── nebulas-dashboard/        # Unified login portal + PWA
├── nebulas-plugins/          # Social CRM plugins
│   ├── whatsapp-crm/         #   WhatsApp Business integration
│   ├── instagram-crm/        #   Instagram DM management
│   ├── telegram-crm/         #   Telegram bot CRM
│   └── line-crm/             #   LINE Official Account CRM
├── nebulas-extensions/       # ERP & HR modules
└── docker-compose.yml        # Unified orchestration (profiles)
```

## License

MIT
