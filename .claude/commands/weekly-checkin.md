Perform a comprehensive weekly check-in by:

1. First, analyze the entire project context:
    - Read [CLAUDE.md](http://claude.md/) to understand the user and their projects
    - Read Goals.md
    - Look for existing metrics history to understand what's been
    tracked
    - Identify what type of work/business this is
2. Based on your analysis, determine the most relevant metrics to
3. Ask for current metrics using the specific metrics YOU
discovered from context
4. After receiving data:
    - Read previous week from `/metrics/metrics-history.md` if it
    exists
    - Update metrics history with new data
    - Launch metrics-analyst subagent for analysis
    - Save report to `/metrics/weekly-report-YYYY-MM-DD.md`
5. Suggest goals for the coming week
6. Write down this week's goals in goals/YYYY-MM-DD-weekly-goals.md
7. Breakdown the goals into individual tasks and calendar events for each goal if possible on the user's calendar to time-block those tasks. 

IMPORTANT: Do NOT use generic templates. Discover what's relevant
for THIS specific user.
