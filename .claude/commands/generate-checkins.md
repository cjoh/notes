# /generate-checkins

Automatically select random clients and generate personalized AI check-in messages for Core Values Recovery business.

## Usage
```
/generate-checkins [--count N] [--type coaching|training|platform] [--priority high|medium|low] [--overdue] [--dry-run]
```

## Behavior

### Client Selection
1. **Smart Randomization** - Prioritize clients based on last contact date and status
2. **Business Logic** - Weight selection toward high-priority and overdue clients  
3. **Variety Enforcement** - Ensure mix across coaching/training/platform clients
4. **Duplicate Prevention** - Never select same client within 48 hours

### Message Generation
- **Context-Aware** - Use client history, recent sessions, current status
- **Authentic Voice** - Match Clay's supportive, professional but warm tone
- **Personalized Content** - Reference specific goals, progress, or challenges
- **Actionable** - Include specific questions or next steps

### Integration Points
- **Calendar Check** - Review recent session history from Google Calendar
- **Platform Data** - Pull usage stats from Core Values platform  
- **Contact History** - Track previous check-ins to avoid duplicates
- **HIPAA Compliance** - Ensure all messages meet privacy requirements

## Command Flow

1. **Analyze Client Pool** - Review all active clients across three business areas
2. **Apply Selection Criteria** - Use priority weighting and recency rules
3. **Generate Personalized Messages** - Create unique, contextual check-ins
4. **Format for Delivery** - Prepare for text/email/platform messaging
5. **Log & Track** - Record all check-ins for follow-up and analytics

## Output Format
```json
{
  "selected_clients": [
    {
      "name": "Client Name",
      "type": "coaching|training|platform", 
      "priority": "high|medium|low",
      "message": "Generated personalized check-in text",
      "delivery_method": "text|email|platform",
      "last_contact": "days_ago",
      "context": "Selection reasoning"
    }
  ],
  "summary": {
    "total_generated": 3,
    "next_run_suggested": "2025-08-07"
  }
}
```

## Examples

**Daily Check-ins:**
```
/generate-checkins --count 3
```

**Focus on Coaching Clients:**
```
/generate-checkins --type coaching --priority high
```

**Overdue Contact Campaign:**
```
/generate-checkins --overdue --count 5
```

**Test Run (No Sending):**
```
/generate-checkins --dry-run
```

---

*Command installed: August 5, 2025*