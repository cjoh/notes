# /schedule-session

Schedule coaching sessions with automatic availability checking and calendar integration for Core Values Recovery.

## Usage
```
/schedule-session [client-name] [date/time] [--type coaching|training] [--duration 60|90|120] [--check-only]
```

## Behavior

### Availability Verification
1. **Calendar Check** - Verify Google Calendar for conflicts
2. **Buffer Rules** - Ensure 15-minute buffer between sessions
3. **Protected Time** - Respect AA meetings, workouts, family time
4. **Business Hours** - Default 9 AM - 5 PM MT for coaching sessions

### Session Types
- **Personal Coaching** - 60 min standard, 90 min intensive
- **Training Sessions** - 2-4 hours, requires morning blocks
- **Platform Demos** - 30 min, flexible timing
- **Team Meetings** - 30-60 min, business hours

### Booking Rules
- **Maximum 4 coaching sessions per day**
- **No back-to-back sessions without 15-min buffer**
- **Training sessions require 4-hour blocks**
- **Emergency sessions can override most rules**

## Integration
- **Google Calendar** - Primary scheduling system
- **Client Database** - Verify client status and history
- **Text/Email** - Send confirmation to client
- **Team Coordination** - Notify Laura/David if relevant

## Examples

**Standard Coaching Session:**
```
/schedule-session "John Smith" "tomorrow 2pm" --type coaching
```

**Training Workshop:**
```
/schedule-session "Recovery Coach Certification" "Friday 9am" --type training --duration 240
```

**Check Availability Only:**
```
/schedule-session --check-only "Wednesday 3pm"
```

---

*Command installed: August 5, 2025*