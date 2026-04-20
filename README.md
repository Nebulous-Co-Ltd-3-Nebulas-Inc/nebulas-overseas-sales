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
    ├── nebulas-contracts/     → E-Signature (DocuSeal)
    ├── nebulas-payments/      → Payment Gateway (Hyperswitch)
    ├── nebulas-crm/core       → Customer Management (Twenty CRM)
    ├── nebulas-marketing/core → Omnichannel Marketing + Page Builder
    ├── nebulas-experiments/   → A/B Testing (GrowthBook)
    ├── nebulas-voip/          → Video Calls + AI Voice Agent
    ├── nebulas-privacy/       → GDPR/CCPA Compliance (Klaro)
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
| Frontend | Next.js 15, React 19, TypeScript, Tailwind CSS, GrapesJS |
| Database | PostgreSQL, MongoDB, Redis, ClickHouse |
| Infrastructure | Docker, Nginx, Temporal (workflow scheduling) |
| Workflow | Custom FlowEngine (n8n-based, 400+ integrations) |
| Analytics | Metabase (AI-powered BI dashboards) |
| CRM | Twenty CRM (full-featured, open-source) |
| Marketing | Dittofeed (journey), Listmonk (mailer), Chatwoot (chat), Mautic (scoring) |
| Payments | Hyperswitch (Rust-based, 50+ payment processors, 135+ currencies) |
| Contracts | DocuSeal (e-signature, multi-party signing, eIDAS compliant) |
| Experiments | GrowthBook (A/B testing, feature flags, Bayesian statistics) |
| VoIP | MiroTalk (WebRTC video, up to 8K) + Bolna (AI voice agent) |
| Privacy | Klaro.js (GDPR/CCPA/LGPD consent management) |
| i18n | i18next (50+ languages, RTL support, SSR-friendly) |
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
| i18n | `nebulas-i18n/` | Multi-language + multi-currency framework | JavaScript, i18next |
| Infra | `nebulas-infra/` | Workflow orchestration and analytics | PostgreSQL, Docker |
| Dashboard | `nebulas-dashboard/` | Unified login portal with SSO + PWA | Express, Nginx |
| Plugins | `nebulas-plugins/` | Social CRM for 4 platforms | Next.js, TypeScript |
| Extensions | `nebulas-extensions/` | ERP & HR modules (Dolibarr, ERPNext, Frappe) | Python, PHP |

## Docker Compose Profiles

| Profile | Services Added | Ports |
|---------|---------------|-------|
| (default) | Dashboard, FlowEngine, Analytics, CRM, PDF Generator, Email Parser | :80-83, :3002-3003 |
| `marketing` | Journey Builder, Mailer, Live Chat, Lead Scoring | :8080 |
| `contracts` | DocuSeal (e-signature) + PostgreSQL | :84 |
| `payments` | Hyperswitch (payment router + control center + web SDK) | :85, :8180, :9050 |
| `experiments` | GrowthBook (A/B testing + feature flags) + MongoDB | :86, :3100 |
| `voip` | MiroTalk (video) + Bolna (AI voice) | :87, :5001 |
| `all` | Everything above | All ports |

## Project Structure

```
nebulas-overseas-sales/
├── nebulas-leadgen/          # Lead generation & scraping
│   ├── core/                 #   Main async pipeline
│   ├── harvester/            #   OSINT intelligence engine (theHarvester)
│   ├── maps-scraper/         #   Google Maps review parser
│   ├── web-scraper/          #   Playwright async web scraper
│   └── enricher/             #   LLM-powered data enrichment
├── nebulas-outreach/         # AI cold outreach
│   ├── core/                 #   Research → scoring → email pipeline
│   ├── sales-agent/          #   8-stage conversational AI (SalesGPT)
│   ├── email-automations/    #   Multi-agent collaboration (analyst + writer)
│   ├── email-manager/        #   Template management & scheduling
│   ├── email-generator/      #   Fast LLM inference (Groq + ChromaDB)
│   └── workflow/             #   LangGraph state machine with routing
├── nebulas-contracts/        # E-signature platform (DocuSeal)
├── nebulas-payments/         # Payment gateway (Hyperswitch, 50+ connectors)
├── nebulas-crm/              # Customer relationship management
│   ├── core/                 #   Docker deployment + extensions
│   ├── platform/             #   Full CRM system (Twenty CRM)
│   ├── erp-extensions/       #   PDF invoice/quote generation
│   └── email-crm/            #   Inbound email parsing (Laravel)
├── nebulas-marketing/        # Marketing automation
│   ├── core/                 #   Unified API gateway
│   ├── journey/              #   Customer journey builder (Dittofeed)
│   ├── mailer/               #   High-performance email engine (Go, Listmonk)
│   ├── chat/                 #   Omnichannel live chat (Chatwoot)
│   ├── scoring/              #   Lead scoring engine (Mautic)
│   └── page-builder/         #   Drag-and-drop landing pages (GrapesJS)
├── nebulas-experiments/      # A/B testing (GrowthBook)
├── nebulas-voip/             # Video + AI voice
├── nebulas-privacy/          # GDPR/CCPA compliance (Klaro.js)
├── nebulas-i18n/             # 50+ languages + 135 currencies
│   └── locales/              #   Language packs (en/zh/ja/es/ar/...)
├── nebulas-infra/            # Infrastructure
│   ├── core/                 #   Docker Compose + auto-setup scripts
│   ├── workflow-engine/      #   Visual workflow builder (n8n-based)
│   └── analytics/            #   BI dashboards (Metabase)
├── nebulas-dashboard/        # Unified login portal + PWA
├── nebulas-plugins/          # Social CRM plugins
│   ├── whatsapp-crm/         #   WhatsApp Business integration
│   ├── instagram-crm/        #   Instagram DM management
│   ├── telegram-crm/         #   Telegram bot CRM
│   └── line-crm/             #   LINE Official Account CRM
├── nebulas-extensions/       # ERP & HR modules
│   ├── dolibarr/             #   Dolibarr ERP integration
│   ├── erpnext/              #   ERPNext modules
│   └── frappe/               #   Frappe framework
└── docker-compose.yml        # Unified orchestration (profiles)
```

## License

MIT
