# /business-dashboard

Generate comprehensive real-time business overview for Core Values Recovery across all three business areas.

## Usage
```
/business-dashboard [--period daily|weekly|monthly] [--focus coaching|training|platform|all] [--metrics-only]
```

## Dashboard Sections

### Revenue Overview
- **Total Revenue** - Current period vs. previous
- **Revenue by Stream** - Coaching, Training, Platform breakdown
- **Pipeline Value** - Potential deals and opportunities
- **Recurring vs. One-time** - Revenue stability metrics

### Client Metrics
- **Active Coaching Clients** - Current count and trends
- **Training Participants** - Enrolled, completed, pipeline
- **Platform Users** - Active licenses, usage patterns
- **Client Retention** - Renewal rates, churn analysis

### Operational Health
- **Session Utilization** - Coaching capacity vs. demand
- **Training Schedule** - Upcoming sessions, enrollment status
- **Platform Performance** - Uptime, user engagement, support tickets
- **Team Productivity** - Laura/David task completion

### Growth Indicators
- **New Client Acquisition** - Lead sources, conversion rates
- **Platform Expansion** - New licenses, feature adoption
- **Training Scale** - Coach certification pipeline
- **Market Opportunities** - Enterprise deals, partnerships

## Key Integrations
- **Google Calendar** - Session counts, utilization rates
- **Core Values Platform** - User analytics, license status
- **Financial Systems** - Revenue tracking, invoicing
- **CRM Data** - Client pipeline, communication history

## Alert System
- **Revenue Below Target** - Weekly/monthly goals
- **Client Churn Risk** - Missed sessions, low engagement
- **Platform Issues** - Technical problems, user complaints
- **Capacity Overload** - Too many sessions scheduled

## Output Format
```
📊 CORE VALUES RECOVERY DASHBOARD - [DATE]

💰 REVENUE (This Week)
   Total: $X,XXX (+/-XX% vs last week)
   Coaching: $XXX | Training: $XXX | Platform: $XXX

👥 CLIENTS 
   Active Coaching: XX clients (XX sessions this week)
   Training Pipeline: XX enrolled, XX graduated
   Platform Users: XX active (XX% utilization)

⚡ OPPORTUNITIES
   - [High-priority deals and next steps]
   - [Platform expansion opportunities]  
   - [Training program growth areas]

🚨 ATTENTION NEEDED
   - [Items requiring immediate action]
   - [Overdue follow-ups or critical issues]
```

## Examples

**Daily Quick Check:**
```
/business-dashboard --period daily
```

**Weekly Comprehensive Review:**
```
/business-dashboard --period weekly --focus all
```

**Coaching Business Focus:**
```
/business-dashboard --focus coaching --period monthly
```

---

*Command installed: August 5, 2025*