# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian notes vault used for goalsetting, checkins and personal notes and knowledgebase. **It also serves as an intelligent business assistant for Core Values Recovery**, managing three core business areas:

1. **Personal Coaching** - One-on-one client sessions
2. **Training Business** - Coach certification and curriculum delivery  
3. **Software Platform** - Professional collaboration and licensing

## Structure

- Markdown files (`.md`) are Obsidian notes
- `.obsidian/` contains Obsidian configuration
- Code examples are stored as standalone code files
- `Styles/` contains writing style guides for different content types

## Writing Styles

When creating content for this vault, reference the appropriate style guide in the `Styles/` directory:

- **Note-taking** (`Styles/note-taking.md`): For creating knowledge notes and documentation
- **Personal voice** (`Styles/personal-voice.md`): When writing in the user's natural voice
- **Outlines** (`Styles/outlines.md`): For structuring projects, articles, or complex topics
- **Ideas** (`Styles/ideas.md`): For capturing brainstorms, insights, and possibilities

Choose the appropriate style based on the content type and purpose.

## Working with This Vault

### Creating New Notes
- Use markdown format with `.md` extension
- Follow Obsidian conventions for internal links: `[[Note Name]]`
- Place in root directory unless organizing into subdirectories

### Code Examples
When creating code examples or demonstrations:
- Create standalone code files for examples
- Include clear comments explaining concepts
- Keep examples simple and dependency-free when possible

### File Naming
- Use descriptive names for code examples (e.g., `text_embeddings_example.py`)
- Date-based notes follow format: `YYYY-MM-DD.md`

**

# Business Assistant Commands

## Client Management
- `/generate-checkins` - Generate personalized client check-in messages
- `/schedule-session [client] [time]` - Book sessions with availability checks  
- `/business-dashboard` - Comprehensive business overview

## Calendar Intelligence
- **Always check current date/time** - Use calendar integration for scheduling
- **Verify availability** before booking any appointments
- **Respect protected time** - AA meetings, workouts, family time
- **HIPAA compliance** - All client communications must be secure
- When asked about today, look at Google Calendar and provide detailed schedule information

## Automation Rules
- Weekly client check-ins for active coaching clients
- Monthly follow-ups for training alumni
- Daily business metrics monitoring
- Team coordination and task delegation

## Sales Pipeline Management
- **Folk.app Integration** - Sales pipeline tracking via Zapier MCP service
- **Four Core Pipelines**:
  - **Client Pipeline** - Incoming coaching clients
  - **CVR Training** - Coaching curriculum training for recovery professionals
  - **Using AI Pipeline** - AI-enhanced coaching training program
  - **CV Platform** - Software platform prospects and licensing
- Track leads, opportunities, and client progression through sales stages
- Automated pipeline updates and reporting
- Integration with client management and scheduling systems

# Daily Check-In Protocol


The `/daily-checkin` command provides:

  

- Personal reflection prompts for well-being tracking

- Mood and energy pattern analysis

- Accomplishment tracking and momentum scoring

- Visual trends and insights over time

- Gentle, encouraging feedback for continuous growth

  

Daily entries are saved in journal/daily/ for long-term pattern

recognition.

  

HOW IT WORKS:

  

- Asks consistent personal development questions daily

- Tracks responses in journal format

- Analyzes patterns across multiple days

- Provides visual mood/energy trends

- Offers encouraging insights and gentle suggestions

- Builds a long-term record of personal growth

  

Unlike business metrics, these personal reflection questions work

universally for anyone focused on self-improvement and productivity

tracking.

**

# Workflow Automation

## File Logging
- When something is done, log it in a `THINGS_I_DID` file
- Format: `[yyyy-mm-dd] - {thing I did}`

## Client File Creation Guidelines
- When creating a new client file, match the format of other files in business/clients/
- Use the following structure:
  - `# LOG`
  - `[date] - item`
  - `# INFO`
  - `THING THAT HAPPENED`