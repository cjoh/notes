# /client-update

Interactive client status update system. Walks through active clients one by one, prompts for updates, and saves to their files.

## Usage
```
/client-update [--all] [--client name] [--type coaching|training|platform]
```

## Behavior

### Client Discovery
1. **Scan Client Directory** - Read all files in `business/clients/`
2. **Identify Active Clients** - Look for clients without "inactive" status
3. **Present One by One** - Go through each client systematically
4. **Interactive Prompts** - Ask for status updates, notes, changes

### Update Process
For each client, ask:
- **Session Notes** - "What's going on with the client?" 

### File Updates
- **LOG Section** - Add new entry with today's date and notes
- **INFO Section** - Update client context as needed
- **Preserve Format** - Maintain existing structure and content
- **Auto-save** - Save changes immediately after each client

## Interactive Flow
```
CLIENT UPDATE SESSION - [DATE]

Found 11 active clients. Starting updates...

--- CLIENT 1/11: Jonathan D ---
Current status: [Show last LOG entry]

UPDATE PROMPTS:
1. Recent session notes: [Wait for input]
2. How are they doing? (1-10 scale: 1=relapsed, 10=great): [Wait for input] 
3. Next session focus: [Wait for input]
4. Any INFO updates: [Wait for input]

[Save to jonathan-d.md]

Continue to next client? (y/n/skip/quit)

--- CLIENT 2/11: Ian M ---
[Repeat process...]
```

## Rating Scale Reference
- **10** - Thriving, strong recovery, meeting all goals
- **8-9** - Doing very well, stable progress
- **6-7** - Steady progress, manageable challenges
- **4-5** - Struggling but engaged, some setbacks
- **2-3** - Significant challenges, high risk
- **1** - Relapsed, crisis situation

## Options

**`--all`** - Update all clients without skipping
**`--client [name]`** - Update only specific client
**`--type [type]`** - Filter by client type (when we have mixed types)

## Examples

**Update All Clients:**
```
/client-update --all
```

**Update Specific Client:**
```
/client-update --client "jonathan-d"
```

**Standard Interactive Mode:**
```
/client-update
```

---

*Command installed: August 5, 2025*