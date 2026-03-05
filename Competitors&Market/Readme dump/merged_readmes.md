<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/actions/workflows/release.yml"><img src="https://github.com/github/spec-kit/actions/workflows/release.yml/badge.svg" alt="Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Table of Contents

- [🤔 What is Spec-Driven Development?](#-what-is-spec-driven-development)
- [⚡ Get Started](#-get-started)
- [📽️ Video Overview](#️-video-overview)
- [🤖 Supported AI Agents](#-supported-ai-agents)
- [🔧 Specify CLI Reference](#-specify-cli-reference)
- [📚 Core Philosophy](#-core-philosophy)
- [🌟 Development Phases](#-development-phases)
- [🎯 Experimental Goals](#-experimental-goals)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [📋 Detailed Process](#-detailed-process)
- [🔍 Troubleshooting](#-troubleshooting)
- [💬 Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Choose your preferred installation method:

#### Option 1: Persistent Installation (Recommended)

Install once and use everywhere:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then use the tool directly:

```bash
# Create new project
specify init <PROJECT_NAME>

# Or initialize in existing project
specify init . --ai claude
# or
specify init --here --ai claude

# Check installed tools
specify check
```

To upgrade Specify, see the [Upgrade Guide](./docs/upgrade.md) for detailed instructions. Quick upgrade:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

#### Option 2: One-time Usage

Run directly without installing:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

**Benefits of persistent installation:**

- Tool stays installed and available in PATH
- No need to create shell aliases
- Better tool management with `uv tool list`, `uv tool upgrade`, `uv tool uninstall`
- Cleaner shell configuration

### 2. Establish project principles

Launch your AI assistant in the project directory. The `/speckit.*` commands are available in the assistant.

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 3. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 4. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 5. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.tasks
```

### 6. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📽️ Video Overview

Want to see Spec Kit in action? Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🤖 Supported AI Agents

| Agent                                                                                | Support | Notes                                                                                                                                     |
| ------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Qoder CLI](https://qoder.com/cli)                                                   | ✅      |                                                                                                                                           |
| [Kiro CLI](https://kiro.dev/docs/cli/)                                               | ✅      | Use `--ai kiro-cli` (alias: `--ai kiro`)                                                                                                 |
| [Amp](https://ampcode.com/)                                                          | ✅      |                                                                                                                                           |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)                              | ✅      |                                                                                                                                           |
| [Claude Code](https://www.anthropic.com/claude-code)                                 | ✅      |                                                                                                                                           |
| [CodeBuddy CLI](https://www.codebuddy.ai/cli)                                        | ✅      |                                                                                                                                           |
| [Codex CLI](https://github.com/openai/codex)                                         | ✅      |                                                                                                                                           |
| [Cursor](https://cursor.sh/)                                                         | ✅      |                                                                                                                                           |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)                            | ✅      |                                                                                                                                           |
| [GitHub Copilot](https://code.visualstudio.com/)                                     | ✅      |                                                                                                                                           |
| [IBM Bob](https://www.ibm.com/products/bob)                                          | ✅      | IDE-based agent with slash command support                                                                                                |
| [Jules](https://jules.google.com/)                                                   | ✅      |                                                                                                                                           |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)                                    | ✅      |                                                                                                                                           |
| [opencode](https://opencode.ai/)                                                     | ✅      |                                                                                                                                           |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                                     | ✅      |                                                                                                                                           |
| [Roo Code](https://roocode.com/)                                                     | ✅      |                                                                                                                                           |
| [SHAI (OVHcloud)](https://github.com/ovh/shai)                                       | ✅      |                                                                                                                                           |
| [Windsurf](https://windsurf.com/)                                                    | ✅      |                                                                                                                                           |
| [Antigravity (agy)](https://agy.ai/)                                                 | ✅      |                                                                                                                                           |
| Generic                                                                              | ✅      | Bring your own agent — use `--ai generic --ai-commands-dir <path>` for unsupported agents                                                 |

## 🔧 Specify CLI Reference

The `specify` command supports the following options:

### Commands

| Command | Description                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `init`  | Initialize a new Specify project from the latest template                                                                                               |
| `check` | Check for installed tools (`git`, `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `qwen`, `opencode`, `codex`, `kiro-cli`, `shai`, `qodercli`) |

### `specify init` Arguments & Options

| Argument/Option        | Type     | Description                                                                                                                                                                                  |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<project-name>`       | Argument | Name for your new project directory (optional if using `--here`, or use `.` for current directory)                                                                                           |
| `--ai`                 | Option   | AI assistant to use: `claude`, `gemini`, `copilot`, `cursor-agent`, `qwen`, `opencode`, `codex`, `windsurf`, `kilocode`, `auggie`, `roo`, `codebuddy`, `amp`, `shai`, `kiro-cli` (`kiro` alias), `agy`, `bob`, `qodercli`, or `generic` (requires `--ai-commands-dir`) |
| `--ai-commands-dir`    | Option   | Directory for agent command files (required with `--ai generic`, e.g. `.myagent/commands/`)                                                                                                  |
| `--script`             | Option   | Script variant to use: `sh` (bash/zsh) or `ps` (PowerShell)                                                                                                                                  |
| `--ignore-agent-tools` | Flag     | Skip checks for AI agent tools like Claude Code                                                                                                                                              |
| `--no-git`             | Flag     | Skip git repository initialization                                                                                                                                                           |
| `--here`               | Flag     | Initialize project in the current directory instead of creating a new one                                                                                                                    |
| `--force`              | Flag     | Force merge/overwrite when initializing in current directory (skip confirmation)                                                                                                             |
| `--skip-tls`           | Flag     | Skip SSL/TLS verification (not recommended)                                                                                                                                                  |
| `--debug`              | Flag     | Enable detailed debug output for troubleshooting                                                                                                                                             |
| `--github-token`       | Option   | GitHub token for API requests (or set GH_TOKEN/GITHUB_TOKEN env variable)                                                                                                                    |
| `--ai-skills`          | Flag     | Install Prompt.MD templates as agent skills in agent-specific `skills/` directory (requires `--ai`)                                                                                          |

### Examples

```bash
# Basic project initialization
specify init my-project

# Initialize with specific AI assistant
specify init my-project --ai claude

# Initialize with Cursor support
specify init my-project --ai cursor-agent

# Initialize with Qoder support
specify init my-project --ai qodercli

# Initialize with Windsurf support
specify init my-project --ai windsurf

# Initialize with Kiro CLI support
specify init my-project --ai kiro-cli

# Initialize with Amp support
specify init my-project --ai amp

# Initialize with SHAI support
specify init my-project --ai shai

# Initialize with IBM Bob support
specify init my-project --ai bob

# Initialize with an unsupported agent (generic / bring your own agent)
specify init my-project --ai generic --ai-commands-dir .myagent/commands/

# Initialize with PowerShell scripts (Windows/cross-platform)
specify init my-project --ai copilot --script ps

# Initialize in current directory
specify init . --ai copilot
# or use the --here flag
specify init --here --ai copilot

# Force merge into current (non-empty) directory without confirmation
specify init . --force --ai copilot
# or
specify init --here --force --ai copilot

# Skip git initialization
specify init my-project --ai gemini --no-git

# Enable debug output for troubleshooting
specify init my-project --ai claude --debug

# Use GitHub token for API requests (helpful for corporate environments)
specify init my-project --ai claude --github-token ghp_your_token_here

# Install agent skills with the project
specify init my-project --ai claude --ai-skills

# Initialize in current directory with agent skills
specify init --here --ai gemini --ai-skills

# Check system requirements
specify check
```

### Available Slash Commands

After running `specify init`, your AI coding agent will have access to these slash commands for structured development:

#### Core Commands

Essential commands for the Spec-Driven Development workflow:

| Command                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `/speckit.constitution` | Create or update project governing principles and development guidelines |
| `/speckit.specify`      | Define what you want to build (requirements and user stories)            |
| `/speckit.plan`         | Create technical implementation plans with your chosen tech stack        |
| `/speckit.tasks`        | Generate actionable task lists for implementation                        |
| `/speckit.implement`    | Execute all tasks to build the feature according to the plan             |

#### Optional Commands

Additional commands for enhanced quality and validation:

| Command              | Description                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | Clarify underspecified areas (recommended before `/speckit.plan`; formerly `/quizme`)                                                |
| `/speckit.analyze`   | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)                             |
| `/speckit.checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

### Environment Variables

| Variable          | Description                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SPECIFY_FEATURE` | Override feature detection for non-Git repositories. Set to the feature directory name (e.g., `001-photo-albums`) to work on a specific feature when not using Git branches.<br/>\*\*Must be set in the context of the agent you're working with prior to using `/speckit.plan` or follow-up commands. |

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development** ("Greenfield")    | Generate from scratch    | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration**                 | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul>                         |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul>                                                                |

## 🎯 Experimental Goals

Our research and experimentation focus on:

### Technology independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-centric development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent.
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

If you encounter issues with an agent, please open an issue so we can refine the integration.

## 📖 Learn More

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#-detailed-process)** - Step-by-step implementation guide

---

## 📋 Detailed Process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot

# Or in current directory:
specify init . --ai claude
specify init . --ai codex

# or use --here flag
specify init --here --ai claude
specify init --here --ai codex

# Force merge into a non-empty current directory
specify init . --force --ai claude

# or
specify init --here --force --ai claude
```

The CLI will check if you have Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, or Kiro CLI installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Establish project principles

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` commands available.

The first step should be establishing your project's governing principles using the `/speckit.constitution` command. This helps ensure consistent decision-making throughout all subsequent development phases:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

This step creates or updates the `.specify/memory/constitution.md` file with your project's foundational guidelines that the AI agent will reference during specification, planning, and implementation phases.

### **STEP 2:** Create project specifications

With your project principles established, you can now create the functional specifications. Use the `/speckit.specify` command and then provide the concrete requirements for the project you want to develop.

> [!IMPORTANT]
> Be as explicit as possible about *what* you are trying to build and *why*. **Do not focus on the tech stack at this point**.

An example prompt:

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

After this prompt is entered, you should see Claude Code kick off the planning and spec drafting process. Claude Code will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-create-taskify`), as well as a new specification in the `specs/001-create-taskify` directory.

The produced specification should contain a set of user stories and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  ├── check-prerequisites.sh
    │  ├── common.sh
    │  ├── create-new-feature.sh
    │  ├── setup-plan.sh
    │  └── update-claude-md.sh
    ├── specs
    │  └── 001-create-taskify
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **STEP 3:** Functional specification clarification (required before planning)

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt.

You should run the structured clarification workflow **before** creating a technical plan to reduce rework downstream.

Preferred order:

1. Use `/speckit.clarify` (structured) – sequential, coverage-based questioning that records answers in a Clarifications section.
2. Optionally follow up with ad-hoc free-form refinement if something still feels vague.

If you intentionally want to skip clarification (e.g., spike or exploratory prototype), explicitly state that so the agent doesn't block on missing clarifications.

Example free-form refinement prompt (after `/speckit.clarify` if still needed):

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

You should also ask Claude Code to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with Claude Code as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 4:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/speckit.plan` command that is built into the project template with a prompt like this:

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

```text
.
├── CLAUDE.md
├── memory
│  └── constitution.md
├── scripts
│  ├── check-prerequisites.sh
│  ├── common.sh
│  ├── create-new-feature.sh
│  ├── setup-plan.sh
│  └── update-claude-md.sh
├── specs
│  └── 001-create-taskify
│      ├── contracts
│      │  ├── api-spec.json
│      │  └── signalr-spec.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask Claude Code to refine it if any of the components stand out, or even have it check the locally-installed version of the platform/framework you want to use (e.g., .NET).

Additionally, you might want to ask Claude Code to research details about the chosen tech stack if it's something that is rapidly changing (e.g., .NET Aspire, JS frameworks), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

During this process, you might find that Claude Code gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

> [!NOTE]
> Claude Code might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 5:** Have Claude Code validate the plan

With the plan in place, you should have Claude Code run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that Claude Code missed in its planning cycle. Once the initial refinement pass is complete, ask Claude Code to go through the checklist once more before you can get to the implementation.

You can also ask Claude Code (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

> [!NOTE]
> Before you have the agent implement it, it's also worth prompting Claude Code to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask Claude Code to resolve them. Ensure that Claude Code follows the [constitution](base/memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### **STEP 6:** Generate task breakdown with /speckit.tasks

With the implementation plan validated, you can now break down the plan into specific, actionable tasks that can be executed in the correct order. Use the `/speckit.tasks` command to automatically generate a detailed task breakdown from your implementation plan:

```text
/speckit.tasks
```

This step creates a `tasks.md` file in your feature specification directory that contains:

- **Task breakdown organized by user story** - Each user story becomes a separate implementation phase with its own set of tasks
- **Dependency management** - Tasks are ordered to respect dependencies between components (e.g., models before services, services before endpoints)
- **Parallel execution markers** - Tasks that can run in parallel are marked with `[P]` to optimize development workflow
- **File path specifications** - Each task includes the exact file paths where implementation should occur
- **Test-driven development structure** - If tests are requested, test tasks are included and ordered to be written before implementation
- **Checkpoint validation** - Each user story phase includes checkpoints to validate independent functionality

The generated tasks.md provides a clear roadmap for the `/speckit.implement` command, ensuring systematic implementation that maintains code quality and allows for incremental delivery of user stories.

### **STEP 7:** Implementation

Once ready, use the `/speckit.implement` command to execute your implementation plan:

```text
/speckit.implement
```

The `/speckit.implement` command will:

- Validate that all prerequisites are in place (constitution, spec, plan, and tasks)
- Parse the task breakdown from `tasks.md`
- Execute tasks in the correct order, respecting dependencies and parallel execution markers
- Follow the TDD approach defined in your task plan
- Provide progress updates and handle errors appropriately

> [!IMPORTANT]
> The AI agent will execute local CLI commands (such as `dotnet`, `npm`, etc.) - make sure you have the required tools installed on your machine.

Once the implementation is complete, test the application and resolve any runtime errors that may not be visible in CLI logs (e.g., browser console errors). You can copy and paste such errors back to your AI agent for resolution.

</details>

---

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 💬 Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam).

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.
<div align="left">
  <img src="assets/kiro-icon.png" alt="Kiro" width="120" height="120">
  
  # Kiro
  
  Kiro is an agentic IDE and command-line interface that helps you go from prototype to production with spec-driven development, agent hooks,powers, and natural language coding assistance. Build faster with AI-powered features that understand your entire codebase, turn prompts into structured specs, and automate repetitive tasks.

  [<img alt="Discord link" src="https://img.shields.io/discord/1374034175430230016?style=flat&logo=discord&logoColor=white&label=discord&color=%239046ff" />](https://discord.gg/kirodotdev)
</div>

## Core Capabilities

- **Specs** - Plan and build features using structured specifications that break down requirements into detailed implementation plans
- **Hooks** - Automate repetitive tasks with intelligent triggers that respond to file changes and development events
- **Agentic Chat** - Build features through natural conversation with Kiro that understands your project context
- **Steering** - Guide Kiro's behavior with custom rules and project-specific context through markdown files
- **MCP Servers** - Connect external tools and data sources through the Model Context Protocol
- **Powers** -  Specialized context and tools for Kiro agents on-demand. Extend agent capabilities with domain-specific knowledge and custom integrations
- **Privacy First** - Keep your code secure with enterprise-grade security and privacy

## Available Interfaces

Kiro is available as both a desktop application and command-line tool:

### Kiro IDE (Desktop Application)
The standalone desktop application is available for:
- macOS
- Windows
- Linux

### Kiro CLI
Command-line interface for integrating Kiro into your development workflows and automation scripts.

For detailed information on both interfaces, visit [kiro.dev](https://kiro.dev)

## Getting Started

### Download & Install

**IDE:** Download the Kiro desktop application directly from [kiro.dev](https://kiro.dev)

**CLI:** Instructions for installing the Kiro CLI are available in our [documentation](https://kiro.dev/cli)

### First Project

Get started with Kiro by following our comprehensive **[first project guide](https://kiro.dev/docs/getting-started/first-project/)**. This hands-on tutorial walks you through Kiro's essential features.

**What you'll learn:**
- Setting up steering files for project-specific guidance
- Creating and managing specs for structured development
- Configuring hooks to automate your workflow
- Connecting MCP servers for external integrations


### One-Click Migration
Import your VS Code setup including extensions and settings during the initial setup process.

## Documentation

**[📚 View Documentation →](https://kiro.dev/docs/)**

- [Getting Started](https://kiro.dev/docs/getting-started) - Installation and first project setup for IDE and CLI
- [IDE Guide](https://kiro.dev/docs/) - Desktop application features and workflows
- [CLI Guide](https://kiro.dev/docs/cli) - Command-line interface usage and automation

## Issue Reporting
We welcome feedback and issue reports to help improve Kiro. Please use this repository to:
- Report bugs and technical issues
- Request new features
- Share feedback on existing functionality
- Discuss improvements and enhancements

## Support
For additional support beyond issue reporting:
- Join our community [discord server](https://discord.gg/kirodotdev) for quick help and discussions with other developers
- For billing-related questions, please contact our support team through [AWS Billing Support](https://support.aws.amazon.com/#/contacts/kiro).
- If you are an existing AWS customer with a [paid support plan](https://aws.amazon.com/premiumsupport/plans/), for technical issues or general assistance, reach out via [AWS Support](https://support.console.aws.amazon.com/support/home#/).

## Security
If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public github issue.

## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.


---
©2026 Amazon.com, Inc. or its affiliates (collectively, "Amazon"). All Rights Reserved.
<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/actions/workflows/release.yml"><img src="https://github.com/github/spec-kit/actions/workflows/release.yml/badge.svg" alt="Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Table of Contents

- [🤔 What is Spec-Driven Development?](#-what-is-spec-driven-development)
- [⚡ Get Started](#-get-started)
- [📽️ Video Overview](#️-video-overview)
- [🤖 Supported AI Agents](#-supported-ai-agents)
- [🔧 Specify CLI Reference](#-specify-cli-reference)
- [📚 Core Philosophy](#-core-philosophy)
- [🌟 Development Phases](#-development-phases)
- [🎯 Experimental Goals](#-experimental-goals)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [📋 Detailed Process](#-detailed-process)
- [🔍 Troubleshooting](#-troubleshooting)
- [💬 Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Choose your preferred installation method:

#### Option 1: Persistent Installation (Recommended)

Install once and use everywhere:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then use the tool directly:

```bash
# Create new project
specify init <PROJECT_NAME>

# Or initialize in existing project
specify init . --ai claude
# or
specify init --here --ai claude

# Check installed tools
specify check
```

To upgrade Specify, see the [Upgrade Guide](./docs/upgrade.md) for detailed instructions. Quick upgrade:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

#### Option 2: One-time Usage

Run directly without installing:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

**Benefits of persistent installation:**

- Tool stays installed and available in PATH
- No need to create shell aliases
- Better tool management with `uv tool list`, `uv tool upgrade`, `uv tool uninstall`
- Cleaner shell configuration

### 2. Establish project principles

Launch your AI assistant in the project directory. The `/speckit.*` commands are available in the assistant.

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 3. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 4. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 5. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.tasks
```

### 6. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📽️ Video Overview

Want to see Spec Kit in action? Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🤖 Supported AI Agents

| Agent                                                                                | Support | Notes                                                                                                                                     |
| ------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Qoder CLI](https://qoder.com/cli)                                                   | ✅      |                                                                                                                                           |
| [Kiro CLI](https://kiro.dev/docs/cli/)                                               | ✅      | Use `--ai kiro-cli` (alias: `--ai kiro`)                                                                                                 |
| [Amp](https://ampcode.com/)                                                          | ✅      |                                                                                                                                           |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)                              | ✅      |                                                                                                                                           |
| [Claude Code](https://www.anthropic.com/claude-code)                                 | ✅      |                                                                                                                                           |
| [CodeBuddy CLI](https://www.codebuddy.ai/cli)                                        | ✅      |                                                                                                                                           |
| [Codex CLI](https://github.com/openai/codex)                                         | ✅      |                                                                                                                                           |
| [Cursor](https://cursor.sh/)                                                         | ✅      |                                                                                                                                           |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)                            | ✅      |                                                                                                                                           |
| [GitHub Copilot](https://code.visualstudio.com/)                                     | ✅      |                                                                                                                                           |
| [IBM Bob](https://www.ibm.com/products/bob)                                          | ✅      | IDE-based agent with slash command support                                                                                                |
| [Jules](https://jules.google.com/)                                                   | ✅      |                                                                                                                                           |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)                                    | ✅      |                                                                                                                                           |
| [opencode](https://opencode.ai/)                                                     | ✅      |                                                                                                                                           |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                                     | ✅      |                                                                                                                                           |
| [Roo Code](https://roocode.com/)                                                     | ✅      |                                                                                                                                           |
| [SHAI (OVHcloud)](https://github.com/ovh/shai)                                       | ✅      |                                                                                                                                           |
| [Windsurf](https://windsurf.com/)                                                    | ✅      |                                                                                                                                           |
| [Antigravity (agy)](https://agy.ai/)                                                 | ✅      |                                                                                                                                           |
| Generic                                                                              | ✅      | Bring your own agent — use `--ai generic --ai-commands-dir <path>` for unsupported agents                                                 |

## 🔧 Specify CLI Reference

The `specify` command supports the following options:

### Commands

| Command | Description                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `init`  | Initialize a new Specify project from the latest template                                                                                               |
| `check` | Check for installed tools (`git`, `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `qwen`, `opencode`, `codex`, `kiro-cli`, `shai`, `qodercli`) |

### `specify init` Arguments & Options

| Argument/Option        | Type     | Description                                                                                                                                                                                  |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<project-name>`       | Argument | Name for your new project directory (optional if using `--here`, or use `.` for current directory)                                                                                           |
| `--ai`                 | Option   | AI assistant to use: `claude`, `gemini`, `copilot`, `cursor-agent`, `qwen`, `opencode`, `codex`, `windsurf`, `kilocode`, `auggie`, `roo`, `codebuddy`, `amp`, `shai`, `kiro-cli` (`kiro` alias), `agy`, `bob`, `qodercli`, or `generic` (requires `--ai-commands-dir`) |
| `--ai-commands-dir`    | Option   | Directory for agent command files (required with `--ai generic`, e.g. `.myagent/commands/`)                                                                                                  |
| `--script`             | Option   | Script variant to use: `sh` (bash/zsh) or `ps` (PowerShell)                                                                                                                                  |
| `--ignore-agent-tools` | Flag     | Skip checks for AI agent tools like Claude Code                                                                                                                                              |
| `--no-git`             | Flag     | Skip git repository initialization                                                                                                                                                           |
| `--here`               | Flag     | Initialize project in the current directory instead of creating a new one                                                                                                                    |
| `--force`              | Flag     | Force merge/overwrite when initializing in current directory (skip confirmation)                                                                                                             |
| `--skip-tls`           | Flag     | Skip SSL/TLS verification (not recommended)                                                                                                                                                  |
| `--debug`              | Flag     | Enable detailed debug output for troubleshooting                                                                                                                                             |
| `--github-token`       | Option   | GitHub token for API requests (or set GH_TOKEN/GITHUB_TOKEN env variable)                                                                                                                    |
| `--ai-skills`          | Flag     | Install Prompt.MD templates as agent skills in agent-specific `skills/` directory (requires `--ai`)                                                                                          |

### Examples

```bash
# Basic project initialization
specify init my-project

# Initialize with specific AI assistant
specify init my-project --ai claude

# Initialize with Cursor support
specify init my-project --ai cursor-agent

# Initialize with Qoder support
specify init my-project --ai qodercli

# Initialize with Windsurf support
specify init my-project --ai windsurf

# Initialize with Kiro CLI support
specify init my-project --ai kiro-cli

# Initialize with Amp support
specify init my-project --ai amp

# Initialize with SHAI support
specify init my-project --ai shai

# Initialize with IBM Bob support
specify init my-project --ai bob

# Initialize with an unsupported agent (generic / bring your own agent)
specify init my-project --ai generic --ai-commands-dir .myagent/commands/

# Initialize with PowerShell scripts (Windows/cross-platform)
specify init my-project --ai copilot --script ps

# Initialize in current directory
specify init . --ai copilot
# or use the --here flag
specify init --here --ai copilot

# Force merge into current (non-empty) directory without confirmation
specify init . --force --ai copilot
# or
specify init --here --force --ai copilot

# Skip git initialization
specify init my-project --ai gemini --no-git

# Enable debug output for troubleshooting
specify init my-project --ai claude --debug

# Use GitHub token for API requests (helpful for corporate environments)
specify init my-project --ai claude --github-token ghp_your_token_here

# Install agent skills with the project
specify init my-project --ai claude --ai-skills

# Initialize in current directory with agent skills
specify init --here --ai gemini --ai-skills

# Check system requirements
specify check
```

### Available Slash Commands

After running `specify init`, your AI coding agent will have access to these slash commands for structured development:

#### Core Commands

Essential commands for the Spec-Driven Development workflow:

| Command                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `/speckit.constitution` | Create or update project governing principles and development guidelines |
| `/speckit.specify`      | Define what you want to build (requirements and user stories)            |
| `/speckit.plan`         | Create technical implementation plans with your chosen tech stack        |
| `/speckit.tasks`        | Generate actionable task lists for implementation                        |
| `/speckit.implement`    | Execute all tasks to build the feature according to the plan             |

#### Optional Commands

Additional commands for enhanced quality and validation:

| Command              | Description                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | Clarify underspecified areas (recommended before `/speckit.plan`; formerly `/quizme`)                                                |
| `/speckit.analyze`   | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)                             |
| `/speckit.checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

### Environment Variables

| Variable          | Description                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SPECIFY_FEATURE` | Override feature detection for non-Git repositories. Set to the feature directory name (e.g., `001-photo-albums`) to work on a specific feature when not using Git branches.<br/>\*\*Must be set in the context of the agent you're working with prior to using `/speckit.plan` or follow-up commands. |

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development** ("Greenfield")    | Generate from scratch    | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration**                 | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul>                         |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul>                                                                |

## 🎯 Experimental Goals

Our research and experimentation focus on:

### Technology independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-centric development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent.
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

If you encounter issues with an agent, please open an issue so we can refine the integration.

## 📖 Learn More

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#-detailed-process)** - Step-by-step implementation guide

---

## 📋 Detailed Process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot

# Or in current directory:
specify init . --ai claude
specify init . --ai codex

# or use --here flag
specify init --here --ai claude
specify init --here --ai codex

# Force merge into a non-empty current directory
specify init . --force --ai claude

# or
specify init --here --force --ai claude
```

The CLI will check if you have Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, or Kiro CLI installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Establish project principles

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` commands available.

The first step should be establishing your project's governing principles using the `/speckit.constitution` command. This helps ensure consistent decision-making throughout all subsequent development phases:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

This step creates or updates the `.specify/memory/constitution.md` file with your project's foundational guidelines that the AI agent will reference during specification, planning, and implementation phases.

### **STEP 2:** Create project specifications

With your project principles established, you can now create the functional specifications. Use the `/speckit.specify` command and then provide the concrete requirements for the project you want to develop.

> [!IMPORTANT]
> Be as explicit as possible about *what* you are trying to build and *why*. **Do not focus on the tech stack at this point**.

An example prompt:

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

After this prompt is entered, you should see Claude Code kick off the planning and spec drafting process. Claude Code will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-create-taskify`), as well as a new specification in the `specs/001-create-taskify` directory.

The produced specification should contain a set of user stories and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  ├── check-prerequisites.sh
    │  ├── common.sh
    │  ├── create-new-feature.sh
    │  ├── setup-plan.sh
    │  └── update-claude-md.sh
    ├── specs
    │  └── 001-create-taskify
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **STEP 3:** Functional specification clarification (required before planning)

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt.

You should run the structured clarification workflow **before** creating a technical plan to reduce rework downstream.

Preferred order:

1. Use `/speckit.clarify` (structured) – sequential, coverage-based questioning that records answers in a Clarifications section.
2. Optionally follow up with ad-hoc free-form refinement if something still feels vague.

If you intentionally want to skip clarification (e.g., spike or exploratory prototype), explicitly state that so the agent doesn't block on missing clarifications.

Example free-form refinement prompt (after `/speckit.clarify` if still needed):

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

You should also ask Claude Code to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with Claude Code as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 4:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/speckit.plan` command that is built into the project template with a prompt like this:

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

```text
.
├── CLAUDE.md
├── memory
│  └── constitution.md
├── scripts
│  ├── check-prerequisites.sh
│  ├── common.sh
│  ├── create-new-feature.sh
│  ├── setup-plan.sh
│  └── update-claude-md.sh
├── specs
│  └── 001-create-taskify
│      ├── contracts
│      │  ├── api-spec.json
│      │  └── signalr-spec.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask Claude Code to refine it if any of the components stand out, or even have it check the locally-installed version of the platform/framework you want to use (e.g., .NET).

Additionally, you might want to ask Claude Code to research details about the chosen tech stack if it's something that is rapidly changing (e.g., .NET Aspire, JS frameworks), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

During this process, you might find that Claude Code gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

> [!NOTE]
> Claude Code might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 5:** Have Claude Code validate the plan

With the plan in place, you should have Claude Code run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that Claude Code missed in its planning cycle. Once the initial refinement pass is complete, ask Claude Code to go through the checklist once more before you can get to the implementation.

You can also ask Claude Code (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

> [!NOTE]
> Before you have the agent implement it, it's also worth prompting Claude Code to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask Claude Code to resolve them. Ensure that Claude Code follows the [constitution](base/memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### **STEP 6:** Generate task breakdown with /speckit.tasks

With the implementation plan validated, you can now break down the plan into specific, actionable tasks that can be executed in the correct order. Use the `/speckit.tasks` command to automatically generate a detailed task breakdown from your implementation plan:

```text
/speckit.tasks
```

This step creates a `tasks.md` file in your feature specification directory that contains:

- **Task breakdown organized by user story** - Each user story becomes a separate implementation phase with its own set of tasks
- **Dependency management** - Tasks are ordered to respect dependencies between components (e.g., models before services, services before endpoints)
- **Parallel execution markers** - Tasks that can run in parallel are marked with `[P]` to optimize development workflow
- **File path specifications** - Each task includes the exact file paths where implementation should occur
- **Test-driven development structure** - If tests are requested, test tasks are included and ordered to be written before implementation
- **Checkpoint validation** - Each user story phase includes checkpoints to validate independent functionality

The generated tasks.md provides a clear roadmap for the `/speckit.implement` command, ensuring systematic implementation that maintains code quality and allows for incremental delivery of user stories.

### **STEP 7:** Implementation

Once ready, use the `/speckit.implement` command to execute your implementation plan:

```text
/speckit.implement
```

The `/speckit.implement` command will:

- Validate that all prerequisites are in place (constitution, spec, plan, and tasks)
- Parse the task breakdown from `tasks.md`
- Execute tasks in the correct order, respecting dependencies and parallel execution markers
- Follow the TDD approach defined in your task plan
- Provide progress updates and handle errors appropriately

> [!IMPORTANT]
> The AI agent will execute local CLI commands (such as `dotnet`, `npm`, etc.) - make sure you have the required tools installed on your machine.

Once the implementation is complete, test the application and resolve any runtime errors that may not be visible in CLI logs (e.g., browser console errors). You can copy and paste such errors back to your AI agent for resolution.

</details>

---

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 💬 Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam).

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.
![BMad Method](banner-bmad-method.png)

[![Version](https://img.shields.io/npm/v/bmad-method?color=blue&label=version)](https://www.npmjs.com/package/bmad-method)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white)](https://discord.gg/gk8jAdXWmj)

**Build More Architect Dreams** — An AI-driven agile development module for the BMad Method Module Ecosystem, the best and most comprehensive Agile AI Driven Development framework that has true scale-adaptive intelligence that adjusts from bug fixes to enterprise systems.

**100% free and open source.** No paywalls. No gated content. No gated Discord. We believe in empowering everyone, not just those who can pay for a gated community or courses.

## Why the BMad Method?

Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI.

- **AI Intelligent Help** — Ask `/bmad-help` anytime for guidance on what's next
- **Scale-Domain-Adaptive** — Automatically adjusts planning depth based on project complexity
- **Structured Workflows** — Grounded in agile best practices across analysis, planning, architecture, and implementation
- **Specialized Agents** — 12+ domain experts (PM, Architect, Developer, UX, Scrum Master, and more)
- **Party Mode** — Bring multiple agent personas into one session to collaborate and discuss
- **Complete Lifecycle** — From brainstorming to deployment

[Learn more at **docs.bmad-method.org**](https://docs.bmad-method.org)

---

## 🚀 What's Next for BMad?

**V6 is here and we're just getting started!** The BMad Method is evolving rapidly with optimizations including Cross Platform Agent Team and Sub Agent inclusion, Skills Architecture, BMad Builder v1, Dev Loop Automation, and so much more in the works.

**[📍 Check out the complete Roadmap →](https://docs.bmad-method.org/roadmap/)**

---

## Quick Start

**Prerequisites**: [Node.js](https://nodejs.org) v20+

```bash
npx bmad-method install
```

> If you are getting a stale beta version, use: `npx bmad-method@6.0.1 install`

Follow the installer prompts, then open your AI IDE (Claude Code, Cursor, etc.) in your project folder.

**Non-Interactive Installation** (for CI/CD):

```bash
npx bmad-method install --directory /path/to/project --modules bmm --tools claude-code --yes
```

[See all installation options](https://docs.bmad-method.org/how-to/non-interactive-installation/)

> **Not sure what to do?** Run `/bmad-help` — it tells you exactly what's next and what's optional. You can also ask questions like `/bmad-help I just finished the architecture, what do I do next?`

## Modules

BMad Method extends with official modules for specialized domains. Available during installation or anytime after.

| Module                                                                                                            | Purpose                                           |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **[BMad Method (BMM)](https://github.com/bmad-code-org/BMAD-METHOD)**                                             | Core framework with 34+ workflows                 |
| **[BMad Builder (BMB)](https://github.com/bmad-code-org/bmad-builder)**                                           | Create custom BMad agents and workflows           |
| **[Test Architect (TEA)](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)**             | Risk-based test strategy and automation           |
| **[Game Dev Studio (BMGD)](https://github.com/bmad-code-org/bmad-module-game-dev-studio)**                        | Game development workflows (Unity, Unreal, Godot) |
| **[Creative Intelligence Suite (CIS)](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Innovation, brainstorming, design thinking        |

## Documentation

[BMad Method Docs Site](https://docs.bmad-method.org) — Tutorials, guides, concepts, and reference

**Quick links:**
- [Getting Started Tutorial](https://docs.bmad-method.org/tutorials/getting-started/)
- [Upgrading from Previous Versions](https://docs.bmad-method.org/how-to/upgrade-to-v6/)
- [Test Architect Documentation](https://bmad-code-org.github.io/bmad-method-test-architecture-enterprise/)


## Community

- [Discord](https://discord.gg/gk8jAdXWmj) — Get help, share ideas, collaborate
- [Subscribe on YouTube](https://www.youtube.com/@BMadCode) — Tutorials, master class, and podcast (launching Feb 2025)
- [GitHub Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) — Bug reports and feature requests
- [Discussions](https://github.com/bmad-code-org/BMAD-METHOD/discussions) — Community conversations

## Support BMad

BMad is free for everyone — and always will be. If you'd like to support development:

- ⭐ Please click the star project icon near the top right of this page
- ☕ [Buy Me a Coffee](https://buymeacoffee.com/bmad) — Fuel the development
- 🏢 Corporate sponsorship — DM on Discord
- 🎤 Speaking & Media — Available for conferences, podcasts, interviews (BM on Discord)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

---

**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC. See [TRADEMARK.md](TRADEMARK.md) for details.

[![Contributors](https://contrib.rocks/image?repo=bmad-code-org/BMAD-METHOD)](https://github.com/bmad-code-org/BMAD-METHOD/graphs/contributors)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor information.
<p align="center">
  <br />

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/statelyai/public-assets/main/logos/xstate-logo-white-nobg.svg">
    <img alt="XState logotype" src="https://raw.githubusercontent.com/statelyai/public-assets/main/logos/xstate-logo-black-nobg.svg" width="200">
  </picture>
  <br />
    <strong>Actor-based state management & orchestration for complex app logic.</strong> <a href="https://stately.ai/docs">→ Documentation</a>
  <br />
  <br />
</p>

XState is a state management and orchestration solution for JavaScript and TypeScript apps. It has _zero_ dependencies, and is useful for frontend and backend application logic.

It uses event-driven programming, state machines, statecharts, and the actor model to handle complex logic in predictable, robust, and visual ways. XState provides a powerful and flexible way to manage application and workflow state by allowing developers to model logic as actors and state machines.

### ✨ Create state machines visually in Stately Studio → [state.new](https://state.new)

---

📖 [Read the documentation](https://stately.ai/docs)

➡️ [Create state machines with the Stately Editor](https://stately.ai/editor)

🖥 [Download our VS Code extension](https://marketplace.visualstudio.com/items?itemName=statelyai.stately-vscode)

📑 Inspired by the [SCXML specification](https://www.w3.org/TR/scxml/)

💬 Chat on the [Stately Discord Community](https://discord.gg/xstate)

✍️ Browse through the many [XState examples](https://github.com/statelyai/xstate/tree/main/examples)

## Sponsors

Special thanks to the sponsors who support this open-source project:

<img src="https://opencollective.com/xstate/tiers/backer/badge.svg?label=sponsors&color=brightgreen" />

<a href="https://transloadit.com/?utm_source=xstate&utm_medium=referral&utm_campaign=sponsorship&utm_content=github">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.transloadit.com/assets/images/sponsorships/logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://assets.transloadit.com/assets/images/sponsorships/logo-default.svg">
    <img src="https://assets.transloadit.com/assets/images/sponsorships/logo-default.svg" alt="Transloadit Logo">
  </picture>
</a>


## Templates

Get started by forking one of these templates on CodeSandbox:

<table>
<thead>
<tr><th>Template</th><th></th></tr>
</thead>
<tbody>

<tr>
<td>

[🤖 XState Template (CodeSandbox)](https://codesandbox.io/p/devbox/github/statelyai/xstate/tree/main/templates/vanilla-ts)

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/statelyai/xstate/tree/main/templates/vanilla-ts?file=%2Fsrc%2FfeedbackMachine.ts)

</td>
<td>

- XState v5
- TypeScript
- _No framework_

</td>
</tr>

<tr>
<td>

[⚛️ XState + React Template (CodeSandbox)](https://codesandbox.io/p/devbox/github/statelyai/xstate/tree/main/templates/react-ts)

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/statelyai/xstate/tree/main/templates/react-ts?file=%2Fsrc%2FfeedbackMachine.ts)

</td>
<td>

- [React](https://react.dev/)
- XState v5
- TypeScript

</td>
</tr>

<tr>
<td>

[💚 XState + Vue Template (CodeSandbox)](https://codesandbox.io/p/devbox/github/statelyai/xstate/tree/main/templates/vue-ts)

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/statelyai/xstate/tree/main/templates/vue-ts?file=%2Fsrc%2FfeedbackMachine.ts)

</td>
<td>

- [Vue](https://vuejs.org/)
- XState v5
- TypeScript

</td>
</tr>

<tr>
<td>

[🧡 XState + Svelte Template (CodeSandbox)](https://codesandbox.io/p/devbox/github/statelyai/xstate/tree/main/templates/svelte-ts)

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/statelyai/xstate/tree/main/templates/svelte-ts?file=%2Fsrc%2FfeedbackMachine.ts)

</td>
<td>

- [Svelte](https://svelte.dev/)
- XState v5
- TypeScript

</td>
</tr>

</tbody>
</table>

## Super quick start

```bash
npm install xstate
```

```ts
import { createMachine, createActor, assign } from 'xstate';

// State machine
const toggleMachine = createMachine({
  id: 'toggle',
  initial: 'inactive',
  context: {
    count: 0
  },
  states: {
    inactive: {
      on: {
        TOGGLE: { target: 'active' }
      }
    },
    active: {
      entry: assign({ count: ({ context }) => context.count + 1 }),
      on: {
        TOGGLE: { target: 'inactive' }
      }
    }
  }
});

// Actor (instance of the machine logic, like a store)
const toggleActor = createActor(toggleMachine);
toggleActor.subscribe((state) => console.log(state.value, state.context));
toggleActor.start();
// => logs 'inactive', { count: 0 }

toggleActor.send({ type: 'TOGGLE' });
// => logs 'active', { count: 1 }

toggleActor.send({ type: 'TOGGLE' });
// => logs 'inactive', { count: 1 }
```

## [Stately Studio](https://stately.ai)

- Visually create, edit, and collaborate on state machines
- Export to many formats, including XState v5
- Test path & documentation autogeneration
- Deploy to Stately Sky
- Generate & modify machines with Stately AI

<a href="stately.ai/registry/new?ref=github" title="Stately Studio">
  <img src="https://github.com/statelyai/xstate/assets/1093738/74ed9cbc-b824-4ed7-a16d-f104947af8a7" alt="XState Viz" width="800" />
</a>

**[state.new](https://stately.ai/registry/new?ref=github)**

## Why?

Statecharts are a formalism for modeling stateful, reactive systems. This is useful for declaratively describing the _behavior_ of your application, from the individual components to the overall application logic.

Read [📽 the slides](http://slides.com/davidkpiano/finite-state-machines) ([🎥 video](https://www.youtube.com/watch?v=VU1NKX6Qkxc)) or check out these resources for learning about the importance of finite state machines and statecharts in user interfaces:

- [Statecharts - A Visual Formalism for Complex Systems](https://www.sciencedirect.com/science/article/pii/0167642387900359/pdf) by David Harel
- [The World of Statecharts](https://statecharts.github.io/) by Erik Mogensen

## Packages

| Package                                                                                     | Description                                                                                                                  |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 🤖 `xstate`                                                                                 | Core finite state machine and statecharts library + interpreter, including graph traversal and model-based testing utilities |
| [⚛️ `@xstate/react`](https://github.com/statelyai/xstate/tree/main/packages/xstate-react)   | React hooks and utilities for using XState in React applications                                                             |
| [💚 `@xstate/vue`](https://github.com/statelyai/xstate/tree/main/packages/xstate-vue)       | Vue composition functions and utilities for using XState in Vue applications                                                 |
| [🎷 `@xstate/svelte`](https://github.com/statelyai/xstate/tree/main/packages/xstate-svelte) | Svelte utilities for using XState in Svelte applications                                                                     |
| [🥏 `@xstate/solid`](https://github.com/statelyai/xstate/tree/main/packages/xstate-solid)   | Solid hooks and utilities for using XState in Solid applications                                                             |
| [🔍 `@statelyai/inspect`](https://github.com/statelyai/inspect)                             | Inspection utilities for XState                                                                                              |
| [🏪 `@xstate/store`](https://github.com/statelyai/xstate/tree/main/packages/xstate-store)   | Small library for simple state management                                                                                    |

## Finite State Machines

<table>
<thead><tr><th>Code</th><th>Statechart</th></tr></thead>
<tbody>
<tr>
<td>

```js
import { createMachine, createActor } from 'xstate';

const lightMachine = createMachine({
  id: 'light',
  initial: 'green',
  states: {
    green: {
      on: {
        TIMER: 'yellow'
      }
    },
    yellow: {
      on: {
        TIMER: 'red'
      }
    },
    red: {
      on: {
        TIMER: 'green'
      }
    }
  }
});

const actor = createActor(lightMachine);

actor.subscribe((state) => {
  console.log(state.value);
});

actor.start();
// logs 'green'

actor.send({ type: 'TIMER' });
// logs 'yellow'
```

</td>
<td>

<a href="https://stately.ai/registry/editor/fa443471-b416-4014-8e6f-12417863e4d4?mode=design&machineId=27e86036-f2f7-40f1-9d1e-66ce6e1accc0" title="Finite states">
  <img src="https://github.com/statelyai/xstate/assets/1093738/36d4b6b5-e3d0-4c19-9f41-2e3425ceac88" alt="Finite states" width="400" />
  <br />
  Open in Stately Studio
</a>
<br />

</td>
</tbody>
</table>

## Hierarchical (Nested) State Machines

<table>
<thead><tr><th>Code</th><th>Statechart</th></tr></thead>
<tbody>
<tr>
<td>

```js
import { createMachine, createActor } from 'xstate';

const pedestrianStates = {
  initial: 'walk',
  states: {
    walk: {
      on: {
        PED_TIMER: 'wait'
      }
    },
    wait: {
      on: {
        PED_TIMER: 'stop'
      }
    },
    stop: {}
  }
};

const lightMachine = createMachine({
  id: 'light',
  initial: 'green',
  states: {
    green: {
      on: {
        TIMER: 'yellow'
      }
    },
    yellow: {
      on: {
        TIMER: 'red'
      }
    },
    red: {
      on: {
        TIMER: 'green'
      },
      ...pedestrianStates
    }
  }
});

const actor = createActor(lightMachine);

actor.subscribe((state) => {
  console.log(state.value);
});

actor.start();
// logs 'green'

actor.send({ type: 'TIMER' });
// logs 'yellow'

actor.send({ type: 'TIMER' });
// logs { red: 'walk' }

actor.send({ type: 'PED_TIMER' });
// logs { red: 'wait' }
```

</td>
<td>
<a href="https://stately.ai/registry/editor/fa443471-b416-4014-8e6f-12417863e4d4?mode=design&machineId=30dffcdd-16c2-49e2-bfc6-a674057cb271" title="Hierarchical states">
  <img src="https://github.com/statelyai/xstate/assets/1093738/32b0692b-1c29-4469-b5e3-03146e3ef249" alt="Hierarchical states" width="400" />
  <br />
  Open in Stately Studio
</a>
<br />
</td>
</tr>
</tbody>
</table>

## Parallel State Machines

<table>
<thead><tr><th>Code</th><th>Statechart</th></tr></thead>
<tbody>
<tr>
<td>

```ts
import { createMachine, createActor } from 'xstate';

const wordMachine = createMachine({
  id: 'word',
  type: 'parallel',
  states: {
    bold: {
      initial: 'off',
      states: {
        on: {
          on: { TOGGLE_BOLD: 'off' }
        },
        off: {
          on: { TOGGLE_BOLD: 'on' }
        }
      }
    },
    underline: {
      initial: 'off',
      states: {
        on: {
          on: { TOGGLE_UNDERLINE: 'off' }
        },
        off: {
          on: { TOGGLE_UNDERLINE: 'on' }
        }
      }
    },
    italics: {
      initial: 'off',
      states: {
        on: {
          on: { TOGGLE_ITALICS: 'off' }
        },
        off: {
          on: { TOGGLE_ITALICS: 'on' }
        }
      }
    },
    list: {
      initial: 'none',
      states: {
        none: {
          on: {
            BULLETS: 'bullets',
            NUMBERS: 'numbers'
          }
        },
        bullets: {
          on: {
            NONE: 'none',
            NUMBERS: 'numbers'
          }
        },
        numbers: {
          on: {
            BULLETS: 'bullets',
            NONE: 'none'
          }
        }
      }
    }
  }
});

const actor = createActor(wordMachine);

actor.subscribe((state) => {
  console.log(state.value);
});

actor.start();
// logs {
//   bold: 'off',
//   italics: 'off',
//   underline: 'off',
//   list: 'none'
// }

actor.send({ type: 'TOGGLE_BOLD' });
// logs {
//   bold: 'on',
//   italics: 'off',
//   underline: 'off',
//   list: 'none'
// }

actor.send({ type: 'TOGGLE_ITALICS' });
// logs {
//   bold: 'on',
//   italics: 'on',
//   underline: 'off',
//   list: 'none'
// }
```

</td>
<td>
<a href="https://stately.ai/registry/editor/fa443471-b416-4014-8e6f-12417863e4d4?mode=design&machineId=980f50d8-e1ff-4441-8c8b-afe41c1610f2" title="Parallel states">
  <img src="https://github.com/statelyai/xstate/assets/1093738/3b1989c0-f4a9-4653-baf2-4df3a40e91a6" alt="Parallel states" width="400" />
  <br />
  Open in Stately Studio
</a>
</td>
</tr>
</tbody>
</table>

## History States

<table>
<thead><tr><th>Code</th><th>Statechart</th></tr></thead>
<tbody>
<tr>
<td>

```js
import { createMachine, createActor } from 'xstate';

const paymentMachine = createMachine({
  id: 'payment',
  initial: 'method',
  states: {
    method: {
      initial: 'cash',
      states: {
        cash: {
          on: {
            SWITCH_CHECK: 'check'
          }
        },
        check: {
          on: {
            SWITCH_CASH: 'cash'
          }
        },
        hist: { type: 'history' }
      },
      on: { NEXT: 'review' }
    },
    review: {
      on: { PREVIOUS: 'method.hist' }
    }
  }
});

const actor = createActor(paymentMachine);

actor.subscribe((state) => {
  console.log(state.value);
});

actor.start();
// logs {
//   value: { method: 'cash' },
// }

actor.send({ type: 'SWITCH_CHECK' });
// logs {
//   value: { method: 'check' },
// }

actor.send({ type: 'NEXT' });
// logs {
//   value: 'review',
// }

actor.send({ type: 'PREVIOUS' });
// logs {
//   value: { method: 'check' },
// }
```

</td>
<td>
<a href="https://stately.ai/registry/editor/fa443471-b416-4014-8e6f-12417863e4d4?mode=design&machineId=d1a9bb95-db97-4af3-b38b-71b005c643d3" title="History states">
  <img src="https://github.com/statelyai/xstate/assets/1093738/1be5c495-d560-4660-94f2-5341efbf7128" alt="History state" width="400" />
  <br />
  Open in Stately Studio
</a>
</td>
</tr>
</tbody>
</table>


## SemVer Policy

We understand the importance of the public contract and do not intend to release any breaking changes to the **runtime** API in a minor or patch release. We consider this with any changes we make to the XState libraries and aim to minimize their effects on existing users.

### Breaking changes

XState executes much of the user logic itself. Therefore, almost any change to its behavior might be considered a breaking change. We recognize this as a potential problem but believe that treating every change as a breaking change is not practical. We do our best to implement new features thoughtfully to enable our users to implement their logic in a better, safer way.

Any change _could_ affect how existing XState machines behave if those machines are using particular configurations. We do not introduce behavior changes on a whim and aim to avoid making changes that affect most existing machines. But we reserve the right to make _some_ behavior changes in minor releases. Our best judgment of the situation will always dictate such changes. Please always read our release notes before deciding to upgrade.

### TypeScript changes

We also reserve a similar right to adjust declared TypeScript definitions or drop support for older versions of TypeScript in a minor release. The TypeScript language itself evolves quickly and often introduces breaking changes in its minor releases. Our team is also continuously learning how to leverage TypeScript more effectively - and the types improve as a result.

For these reasons, it is impractical for our team to be bound by decisions taken when an older version of TypeScript was its latest version or when we didn’t know how to declare our types in a better way. We won’t introduce declaration changes often - but we are more likely to do so than with runtime changes.

### Packages

Most of the packages in the XState family declare a peer dependency on XState itself. We’ll be cautious about maintaining compatibility with already-released packages when releasing a new version of XState, **but** each release of packages depending on XState will always adjust the declared peer dependency range to include the latest version of XState. For example, you should always be able to update `xstate` without `@xstate/react`. But when you update `@xstate/react`, we highly recommend updating `xstate` too.
<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec">
    <picture>
      <source srcset="assets/openspec_bg.png">
      <img src="assets/openspec_bg.png" alt="OpenSpec logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Fission-AI/OpenSpec/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://www.npmjs.com/package/@fission-ai/openspec"><img alt="npm version" src="https://img.shields.io/npm/v/@fission-ai/openspec?style=flat-square" /></a>
  <a href="./LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" /></a>
  <a href="https://discord.gg/YctCnvvshC"><img alt="Discord" src="https://img.shields.io/discord/1411657095639601154?style=flat-square&logo=discord&logoColor=white&label=Discord&suffix=%20online" /></a>
</p>

<details>
<summary><strong>The most loved spec framework.</strong></summary>

[![Stars](https://img.shields.io/github/stars/Fission-AI/OpenSpec?style=flat-square&label=Stars)](https://github.com/Fission-AI/OpenSpec/stargazers)
[![Downloads](https://img.shields.io/npm/dm/@fission-ai/openspec?style=flat-square&label=Downloads/mo)](https://www.npmjs.com/package/@fission-ai/openspec)
[![Contributors](https://img.shields.io/github/contributors/Fission-AI/OpenSpec?style=flat-square&label=Contributors)](https://github.com/Fission-AI/OpenSpec/graphs/contributors)

</details>
<p></p>
Our philosophy:

```text
→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises
```

> [!TIP]
> **New workflow now available!** We've rebuilt OpenSpec with a new artifact-guided workflow.
>
> Run `/opsx:propose "your idea"` to get started. → [Learn more here](docs/opsx.md)

<p align="center">
  Follow <a href="https://x.com/0xTab">@0xTab on X</a> for updates · Join the <a href="https://discord.gg/YctCnvvshC">OpenSpec Discord</a> for help and questions.
</p>

### Teams

Using OpenSpec in a team? [Email here](mailto:teams@openspec.dev) for access to our Slack channel.

<!-- TODO: Add GIF demo of /opsx:propose → /opsx:archive workflow -->

## See it in action

```text
You: /opsx:propose add-dark-mode
AI:  Created openspec/changes/add-dark-mode/
     ✓ proposal.md — why we're doing this, what's changing
     ✓ specs/       — requirements and scenarios
     ✓ design.md    — technical approach
     ✓ tasks.md     — implementation checklist
     Ready for implementation!

You: /opsx:apply
AI:  Implementing tasks...
     ✓ 1.1 Add theme context provider
     ✓ 1.2 Create toggle component
     ✓ 2.1 Add CSS variables
     ✓ 2.2 Wire up localStorage
     All tasks complete!

You: /opsx:archive
AI:  Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
     Specs updated. Ready for the next feature.
```

<details>
<summary><strong>OpenSpec Dashboard</strong></summary>

<p align="center">
  <img src="assets/openspec_dashboard.png" alt="OpenSpec dashboard preview" width="90%">
</p>

</details>

## Quick Start

**Requires Node.js 20.19.0 or higher.**

Install OpenSpec globally:

```bash
npm install -g @fission-ai/openspec@latest
```

Then navigate to your project directory and initialize:

```bash
cd your-project
openspec init
```

Now tell your AI: `/opsx:propose <what-you-want-to-build>`

If you want the expanded workflow (`/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:sync`, `/opsx:bulk-archive`, `/opsx:onboard`), select it with `openspec config profile` and apply with `openspec update`.

> [!NOTE]
> Not sure if your tool is supported? [View the full list](docs/supported-tools.md) – we support 20+ tools and growing.
>
> Also works with pnpm, yarn, bun, and nix. [See installation options](docs/installation.md).

## Docs

→ **[Getting Started](docs/getting-started.md)**: first steps<br>
→ **[Workflows](docs/workflows.md)**: combos and patterns<br>
→ **[Commands](docs/commands.md)**: slash commands & skills<br>
→ **[CLI](docs/cli.md)**: terminal reference<br>
→ **[Supported Tools](docs/supported-tools.md)**: tool integrations & install paths<br>
→ **[Concepts](docs/concepts.md)**: how it all fits<br>
→ **[Multi-Language](docs/multi-language.md)**: multi-language support<br>
→ **[Customization](docs/customization.md)**: make it yours


## Why OpenSpec?

AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written.

- **Agree before you build** — human and AI align on specs before code gets written
- **Stay organized** — each change gets its own folder with proposal, specs, design, and tasks
- **Work fluidly** — update any artifact anytime, no rigid phase gates
- **Use your tools** — works with 20+ AI assistants via slash commands

### How we compare

**vs. [Spec Kit](https://github.com/github/spec-kit)** (GitHub) — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.

**vs. [Kiro](https://kiro.dev)** (AWS) — Powerful but you're locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use.

**vs. nothing** — AI coding without specs means vague prompts and unpredictable results. OpenSpec brings predictability without the ceremony.

## Updating OpenSpec

**Upgrade the package**

```bash
npm install -g @fission-ai/openspec@latest
```

**Refresh agent instructions**

Run this inside each project to regenerate AI guidance and ensure the latest slash commands are active:

```bash
openspec update
```

## Usage Notes

**Model selection**: OpenSpec works best with high-reasoning models. We recommend Opus 4.5 and GPT 5.2 for both planning and implementation.

**Context hygiene**: OpenSpec benefits from a clean context window. Clear your context before starting implementation and maintain good context hygiene throughout your session.

## Contributing

**Small fixes** — Bug fixes, typo corrections, and minor improvements can be submitted directly as PRs.

**Larger changes** — For new features, significant refactors, or architectural changes, please submit an OpenSpec change proposal first so we can align on intent and goals before implementation begins.

When writing proposals, keep the OpenSpec philosophy in mind: we serve a wide variety of users across different coding agents, models, and use cases. Changes should work well for everyone.

**AI-generated code is welcome** — as long as it's been tested and verified. PRs containing AI-generated code should mention the coding agent and model used (e.g., "Generated with Claude Code using claude-opus-4-5-20251101").

### Development

- Install dependencies: `pnpm install`
- Build: `pnpm run build`
- Test: `pnpm test`
- Develop CLI locally: `pnpm run dev` or `pnpm run dev:cli`
- Conventional commits (one-line): `type(scope): subject`

## Other

<details>
<summary><strong>Telemetry</strong></summary>

OpenSpec collects anonymous usage stats.

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.

**Opt-out:** `export OPENSPEC_TELEMETRY=0` or `export DO_NOT_TRACK=1`

</details>

<details>
<summary><strong>Maintainers & Advisors</strong></summary>

See [MAINTAINERS.md](MAINTAINERS.md) for the list of core maintainers and advisors who help guide the project.

</details>



## License

MIT
<a name="readme-top"></a>

<div align='center'>
<a href="https://trendshift.io/repositories/13971" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13971" alt="eyaltoledano%2Fclaude-task-master | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<p align="center">
  <a href="https://task-master.dev"><img src="./images/logo.png?raw=true" alt="Taskmaster logo"></a>
</p>

<p align="center">
<b>Taskmaster</b>: A task management system for AI-driven development, designed to work seamlessly with any AI chat.
</p>

<p align="center">
  <a href="https://discord.gg/taskmasterai" target="_blank"><img src="https://dcbadge.limes.pink/api/server/https://discord.gg/taskmasterai?style=flat" alt="Discord"></a> |
  <a href="https://docs.task-master.dev" target="_blank">Docs</a>
</p>

<p align="center">
  <a href="https://github.com/eyaltoledano/claude-task-master/actions/workflows/ci.yml"><img src="https://github.com/eyaltoledano/claude-task-master/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/eyaltoledano/claude-task-master/stargazers"><img src="https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=social" alt="GitHub stars"></a>
  <a href="https://badge.fury.io/js/task-master-ai"><img src="https://badge.fury.io/js/task-master-ai.svg" alt="npm version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT%20with%20Commons%20Clause-blue.svg" alt="License"></a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/task-master-ai"><img src="https://img.shields.io/npm/d18m/task-master-ai?style=flat" alt="NPM Downloads"></a>
  <a href="https://www.npmjs.com/package/task-master-ai"><img src="https://img.shields.io/npm/dm/task-master-ai?style=flat" alt="NPM Downloads"></a>
  <a href="https://www.npmjs.com/package/task-master-ai"><img src="https://img.shields.io/npm/dw/task-master-ai?style=flat" alt="NPM Downloads"></a>
</p>

## By [@eyaltoledano](https://x.com/eyaltoledano) & [@RalphEcom](https://x.com/RalphEcom)

[![Twitter Follow](https://img.shields.io/twitter/follow/eyaltoledano)](https://x.com/eyaltoledano)
[![Twitter Follow](https://img.shields.io/twitter/follow/RalphEcom)](https://x.com/RalphEcom)

A task management system for AI-driven development with Claude, designed to work seamlessly with Cursor AI.

## Documentation

📚 **[View Full Documentation](https://docs.task-master.dev)**

For detailed guides, API references, and comprehensive examples, visit our documentation site.

### Quick Reference

The following documentation is also available in the `docs` directory:

- [Configuration Guide](docs/configuration.md) - Set up environment variables and customize Task Master
- [Tutorial](docs/tutorial.md) - Step-by-step guide to getting started with Task Master
- [Command Reference](docs/command-reference.md) - Complete list of all available commands
- [Task Structure](docs/task-structure.md) - Understanding the task format and features
- [Example Interactions](docs/examples.md) - Common Cursor AI interaction examples
- [Migration Guide](docs/migration-guide.md) - Guide to migrating to the new project structure

#### Quick Install for Cursor 1.0+ (One-Click)

[![Add task-master-ai MCP server to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=task-master-ai&config=eyJjb21tYW5kIjoibnB4IC15IC0tcGFja2FnZT10YXNrLW1hc3Rlci1haSB0YXNrLW1hc3Rlci1haSIsImVudiI6eyJBTlRIUk9QSUNfQVBJX0tFWSI6IllPVVJfQU5USFJPUElDX0FQSV9LRVlfSEVSRSIsIlBFUlBMRVhJVFlfQVBJX0tFWSI6IllPVVJfUEVSUExFWElUWV9BUElfS0VZX0hFUkUiLCJPUEVOQUlfQVBJX0tFWSI6IllPVVJfT1BFTkFJX0tFWV9IRVJFIiwiR09PR0xFX0FQSV9LRVkiOiJZT1VSX0dPT0dMRV9LRVlfSEVSRSIsIk1JU1RSQUxfQVBJX0tFWSI6IllPVVJfTUlTVFJBTF9LRVlfSEVSRSIsIkdST1FfQVBJX0tFWSI6IllPVVJfR1JPUV9LRVlfSEVSRSIsIk9QRU5ST1VURVJfQVBJX0tFWSI6IllPVVJfT1BFTlJPVVRFUl9LRVlfSEVSRSIsIlhBSV9BUElfS0VZIjoiWU9VUl9YQUlfS0VZX0hFUkUiLCJBWlVSRV9PUEVOQUlfQVBJX0tFWSI6IllPVVJfQVpVUkVfS0VZX0hFUkUiLCJPTExBTUFfQVBJX0tFWSI6IllPVVJfT0xMQU1BX0FQSV9LRVlfSEVSRSJ9fQ%3D%3D)

> **Note:** After clicking the link, you'll still need to add your API keys to the configuration. The link installs the MCP server with placeholder keys that you'll need to replace with your actual API keys.

#### Claude Code Quick Install

For Claude Code users:

```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

Don't forget to add your API keys to the configuration:
- in the root .env of your Project
- in the "env" section of your mcp config for taskmaster-ai


## Requirements

Taskmaster utilizes AI across several commands, and those require a separate API key. You can use a variety of models from different AI providers provided you add your API keys. For example, if you want to use Claude 3.7, you'll need an Anthropic API key.

You can define 3 types of models to be used: the main model, the research model, and the fallback model (in case either the main or research fail). Whatever model you use, its provider API key must be present in either mcp.json or .env.

At least one (1) of the following is required:

- Anthropic API key (Claude API)
- OpenAI API key
- Google Gemini API key
- Perplexity API key (for research model)
- xAI API Key (for research or main model)
- OpenRouter API Key (for research or main model)
- Claude Code (no API key required - requires Claude Code CLI)
- Codex CLI (OAuth via ChatGPT subscription - requires Codex CLI)

Using the research model is optional but highly recommended. You will need at least ONE API key (unless using Claude Code or Codex CLI with OAuth). Adding all API keys enables you to seamlessly switch between model providers at will.

## Quick Start

### Option 1: MCP (Recommended)

MCP (Model Control Protocol) lets you run Task Master directly from your editor.

#### 1. Add your MCP config at the following path depending on your editor

| Editor       | Scope   | Linux/macOS Path                      | Windows Path                                      | Key          |
| ------------ | ------- | ------------------------------------- | ------------------------------------------------- | ------------ |
| **Cursor**   | Global  | `~/.cursor/mcp.json`                  | `%USERPROFILE%\.cursor\mcp.json`                  | `mcpServers` |
|              | Project | `<project_folder>/.cursor/mcp.json`   | `<project_folder>\.cursor\mcp.json`               | `mcpServers` |
| **Windsurf** | Global  | `~/.codeium/windsurf/mcp_config.json` | `%USERPROFILE%\.codeium\windsurf\mcp_config.json` | `mcpServers` |
| **VS Code**  | Project | `<project_folder>/.vscode/mcp.json`   | `<project_folder>\.vscode\mcp.json`               | `servers`    |
| **Q CLI**    | Global  | `~/.aws/amazonq/mcp.json`             |                                                   | `mcpServers` |

##### Manual Configuration

###### Cursor & Windsurf & Q Developer CLI (`mcpServers`)

```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        // "TASK_MASTER_TOOLS": "all", // Options: "all", "standard", "core", or comma-separated list of tools
        "ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY_HERE",
        "PERPLEXITY_API_KEY": "YOUR_PERPLEXITY_API_KEY_HERE",
        "OPENAI_API_KEY": "YOUR_OPENAI_KEY_HERE",
        "GOOGLE_API_KEY": "YOUR_GOOGLE_KEY_HERE",
        "MISTRAL_API_KEY": "YOUR_MISTRAL_KEY_HERE",
        "GROQ_API_KEY": "YOUR_GROQ_KEY_HERE",
        "OPENROUTER_API_KEY": "YOUR_OPENROUTER_KEY_HERE",
        "XAI_API_KEY": "YOUR_XAI_KEY_HERE",
        "AZURE_OPENAI_API_KEY": "YOUR_AZURE_KEY_HERE",
        "OLLAMA_API_KEY": "YOUR_OLLAMA_API_KEY_HERE"
      }
    }
  }
}
```

> 🔑 Replace `YOUR_…_KEY_HERE` with your real API keys. You can remove keys you don't use.

> **Note**: If you see `0 tools enabled` in the MCP settings, restart your editor and check that your API keys are correctly configured.

###### VS Code (`servers` + `type`)

```json
{
  "servers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        // "TASK_MASTER_TOOLS": "all", // Options: "all", "standard", "core", or comma-separated list of tools
        "ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY_HERE",
        "PERPLEXITY_API_KEY": "YOUR_PERPLEXITY_API_KEY_HERE",
        "OPENAI_API_KEY": "YOUR_OPENAI_KEY_HERE",
        "GOOGLE_API_KEY": "YOUR_GOOGLE_KEY_HERE",
        "MISTRAL_API_KEY": "YOUR_MISTRAL_KEY_HERE",
        "GROQ_API_KEY": "YOUR_GROQ_KEY_HERE",
        "OPENROUTER_API_KEY": "YOUR_OPENROUTER_KEY_HERE",
        "XAI_API_KEY": "YOUR_XAI_KEY_HERE",
        "AZURE_OPENAI_API_KEY": "YOUR_AZURE_KEY_HERE",
        "OLLAMA_API_KEY": "YOUR_OLLAMA_API_KEY_HERE"
      },
      "type": "stdio"
    }
  }
}
```

> 🔑 Replace `YOUR_…_KEY_HERE` with your real API keys. You can remove keys you don't use.

#### 2. (Cursor-only) Enable Taskmaster MCP

Open Cursor Settings (Ctrl+Shift+J) ➡ Click on MCP tab on the left ➡ Enable task-master-ai with the toggle

#### 3. (Optional) Configure the models you want to use

In your editor's AI chat pane, say:

```txt
Change the main, research and fallback models to <model_name>, <model_name> and <model_name> respectively.
```

For example, to use Claude Code (no API key required):
```txt
Change the main model to claude-code/sonnet
```

[Table of available models](docs/models.md) | [Claude Code setup](docs/examples/claude-code-usage.md)

#### 4. Initialize Task Master

In your editor's AI chat pane, say:

```txt
Initialize taskmaster-ai in my project
```

#### 5. Make sure you have a PRD (Recommended)

For **new projects**: Create your PRD at `.taskmaster/docs/prd.txt`.
For **existing projects**: You can use `scripts/prd.txt` or migrate with `task-master migrate`

An example PRD template is available after initialization in `.taskmaster/templates/example_prd.txt`.

> [!NOTE]
> While a PRD is recommended for complex projects, you can always create individual tasks by asking "Can you help me implement [description of what you want to do]?" in chat.

**Always start with a detailed PRD.**

The more detailed your PRD, the better the generated tasks will be.

#### 6. Common Commands

Use your AI assistant to:

- Parse requirements: `Can you parse my PRD at scripts/prd.txt?`
- Plan next step: `What's the next task I should work on?`
- Implement a task: `Can you help me implement task 3?`
- View multiple tasks: `Can you show me tasks 1, 3, and 5?`
- Expand a task: `Can you help me expand task 4?`
- **Research fresh information**: `Research the latest best practices for implementing JWT authentication with Node.js`
- **Research with context**: `Research React Query v5 migration strategies for our current API implementation in src/api.js`

[More examples on how to use Task Master in chat](docs/examples.md)

### Option 2: Using Command Line

#### Installation

```bash
# Install globally
npm install -g task-master-ai

# OR install locally within your project
npm install task-master-ai
```

#### Initialize a new project

```bash
# If installed globally
task-master init

# If installed locally
npx task-master init

# Initialize project with specific rules
task-master init --rules cursor,windsurf,vscode
```

This will prompt you for project details and set up a new project with the necessary files and structure.

#### Common Commands

```bash
# Initialize a new project
task-master init

# Parse a PRD and generate tasks
task-master parse-prd your-prd.txt

# List all tasks
task-master list

# Show the next task to work on
task-master next

# Show specific task(s) - supports comma-separated IDs
task-master show 1,3,5

# Research fresh information with project context
task-master research "What are the latest best practices for JWT authentication?"

# Move tasks between tags (cross-tag movement)
task-master move --from=5 --from-tag=backlog --to-tag=in-progress
task-master move --from=5,6,7 --from-tag=backlog --to-tag=done --with-dependencies
task-master move --from=5 --from-tag=backlog --to-tag=in-progress --ignore-dependencies

# Add rules after initialization
task-master rules add windsurf,roo,vscode
```

## Tool Loading Configuration

### Optimizing MCP Tool Loading

Task Master's MCP server supports selective tool loading to reduce context window usage. By default, all 36 tools are loaded (~21,000 tokens) to maintain backward compatibility with existing installations.

You can optimize performance by configuring the `TASK_MASTER_TOOLS` environment variable:

### Available Modes

| Mode | Tools | Context Usage | Use Case |
|------|-------|--------------|----------|
| `all` (default) | 36 | ~21,000 tokens | Complete feature set - all tools available |
| `standard` | 15 | ~10,000 tokens | Common task management operations |
| `core` (or `lean`) | 7 | ~5,000 tokens | Essential daily development workflow |
| `custom` | Variable | Variable | Comma-separated list of specific tools |

### Configuration Methods

#### Method 1: Environment Variable in MCP Configuration

Add `TASK_MASTER_TOOLS` to your MCP configuration file's `env` section:

```jsonc
{
  "mcpServers": {  // or "servers" for VS Code
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        "TASK_MASTER_TOOLS": "standard",  // Options: "all", "standard", "core", "lean", or comma-separated list
        "ANTHROPIC_API_KEY": "your-key-here",
        // ... other API keys
      }
    }
  }
}
```

#### Method 2: Claude Code CLI (One-Time Setup)

For Claude Code users, you can set the mode during installation:

```bash
# Core mode example (~70% token reduction)
claude mcp add task-master-ai --scope user \
  --env TASK_MASTER_TOOLS="core" \
  -- npx -y task-master-ai@latest

# Custom tools example
claude mcp add task-master-ai --scope user \
  --env TASK_MASTER_TOOLS="get_tasks,next_task,set_task_status" \
  -- npx -y task-master-ai@latest
```

### Tool Sets Details

**Core Tools (7):** `get_tasks`, `next_task`, `get_task`, `set_task_status`, `update_subtask`, `parse_prd`, `expand_task`

**Standard Tools (15):** All core tools plus `initialize_project`, `analyze_project_complexity`, `expand_all`, `add_subtask`, `remove_task`, `generate`, `add_task`, `complexity_report`

**All Tools (36):** Complete set including project setup, task management, analysis, dependencies, tags, research, and more

### Recommendations

- **New users**: Start with `"standard"` mode for a good balance
- **Large projects**: Use `"core"` mode to minimize token usage
- **Complex workflows**: Use `"all"` mode or custom selection
- **Backward compatibility**: If not specified, defaults to `"all"` mode

## Claude Code Support

Task Master now supports Claude models through the Claude Code CLI, which requires no API key:

- **Models**: `claude-code/opus` and `claude-code/sonnet`
- **Requirements**: Claude Code CLI installed
- **Benefits**: No API key needed, uses your local Claude instance

[Learn more about Claude Code setup](docs/examples/claude-code-usage.md)

## Troubleshooting

### If `task-master init` doesn't respond

Try running it with Node directly:

```bash
node node_modules/claude-task-master/scripts/init.js
```

Or clone the repository and run:

```bash
git clone https://github.com/eyaltoledano/claude-task-master.git
cd claude-task-master
node scripts/init.js
```

## Join Our Team

<a href="https://tryhamster.com" target="_blank">
  <img src="./images/hamster-hiring.png" alt="Join Hamster's founding team" />
</a>

## Contributors

<a href="https://github.com/eyaltoledano/claude-task-master/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eyaltoledano/claude-task-master" alt="Task Master project contributors" />
</a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=eyaltoledano/claude-task-master&type=Timeline)](https://www.star-history.com/#eyaltoledano/claude-task-master&Timeline)

## Licensing

Task Master is licensed under the MIT License with Commons Clause. This means you can:

✅ **Allowed**:

- Use Task Master for any purpose (personal, commercial, academic)
- Modify the code
- Distribute copies
- Create and sell products built using Task Master

❌ **Not Allowed**:

- Sell Task Master itself
- Offer Task Master as a hosted service
- Create competing products based on Task Master

See the [LICENSE](LICENSE) file for the complete license text and [licensing details](docs/licensing.md) for more information.
<img width="1200" height="675" alt="Agent OS" src="https://github.com/user-attachments/assets/97ad4491-d199-4b9b-9482-ae710291dfb4" />

## Agents that build the way you would

[Agent OS](https://buildermethods.com/agent-os) helps you shape better specs, keeps agents aligned in a lightweight system that fits how you already build.

Works alongside Claude Code, Cursor, Antigravity, and other AI tools. Any language, any framework.

**Core capabilities:**

- **Discover Standards** — Extract patterns and conventions from your codebase into documented standards
- **Deploy Standards** — Intelligently inject relevant standards based on what you're building
- **Shape Spec** — Create better plans that lead to better builds
- **Index Standards** — Keep your standards organized and discoverable

---

### Documentation & Installation

Docs, installation, usage, & best practices 👉 [It's all here](https://buildermethods.com/agent-os)

---

### Follow updates & releases

Read the [changelog](CHANGELOG.md)

[Subscribe to be notified of major new releases of Agent OS](https://buildermethods.com/agent-os)

---

### Created by Brian Casel @ Builder Methods

Created by Brian Casel, the creator of [Builder Methods](https://buildermethods.com), where Brian helps professional software developers and teams build with AI.

Get Brian's free resources on building with AI:
- [Builder Briefing newsletter](https://buildermethods.com)
- [YouTube](https://youtube.com/@briancasel)

Join [Builder Methods Pro](https://buildermethods.com/pro) for official support and connect with our community of AI-first builders:

<div align="center">

<pre>
▄▀█ █ █ ▀█▀ █▀█ █▀ █▀█ █▀▀ █▀▀
█▀█ █▄█  █  █▄█ ▄█ █▀▀ ██▄ █▄▄
</pre>

**Spec-Driven Development Automation**

[![GitHub CI](https://github.com/ariel-frischer/autospec/actions/workflows/ci.yml/badge.svg)](https://github.com/ariel-frischer/autospec/actions/workflows/ci.yml)
[![GitHub Release](https://img.shields.io/github/v/release/ariel-frischer/autospec)](https://github.com/ariel-frischer/autospec/releases/latest)
[![Go Report Card](https://goreportcard.com/badge/github.com/ariel-frischer/autospec)](https://goreportcard.com/report/github.com/ariel-frischer/autospec)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Build features systematically with AI-powered specification workflows.

</div>

**Stop AI slop.** Autospec brings structure to AI coding: spec → plan → tasks → implement - all in one command.

Built with a **multi-agent architecture** and inspired by [GitHub SpecKit](https://github.com/github/spec-kit), Autospec reimagines the specification workflow with **YAML-first artifacts** for programmatic access and validation. These principles ensure reliable, performant, and maintainable software that developers 
can trust for their critical development workflows.

## 📦 Installation

```bash
curl -fsSL https://raw.githubusercontent.com/ariel-frischer/autospec/main/install.sh | sh
```

## 🎯 Key Features

- **Automated Workflow Orchestration** — Runs stages in dependency order with automatic retry on failure
- **YAML-First Artifacts** — Machine-readable `spec.yaml`, `plan.yaml`, `tasks.yaml` for programmatic access
- **Smart Validation** — Validates artifacts exist and meet completeness criteria before proceeding
- **Cross-Platform** — Native binaries for Linux and macOS (Intel/Apple Silicon). Windows users: use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- **Flexible Stage Selection** — Mix and match stages with intuitive flags (`-spti`, `-a`, etc.)
- **Shell Completion** — Tab completion for bash, zsh, and fish
- **OS Notifications** — Native desktop notifications with custom sound support
- **History Tracking** — View and filter command execution history with status, duration, and exit codes
- **Auto-Commit** — Automatic git commit creation with .gitignore management and conventional commit messages

## ✨ What Makes Autospec Different?

Originally inspired by [GitHub SpecKit](https://github.com/github/spec-kit), Autospec is now a **fully standalone tool** with its own embedded commands and workflows.

| Feature | GitHub SpecKit | Autospec |
|---------|---------------|----------|
| Output Format | Markdown | **YAML** (machine-readable) |
| Validation | Manual review | **Automatic** with retry logic |
| Context Efficiency | Full prompt each time | **Smart YAML injection** + **phase-isolated sessions** |
| Status Updates | Manual | **Auto-updates** spec.yaml & tasks.yaml |
| Phase Orchestration | Manual | **Automated** with dependencies |
| Session Isolation | Single session | **Per-phase/task** (80%+ cost savings) |
| Implementation | Shell scripts | **Go** (type-safe, single binary) |

## 🚀 Quick Start

> **New to autospec?** See the [Quickstart Guide](docs/public/quickstart.md) or run the [interactive demo](scripts/quickstart-demo.sh).

### Prerequisites

- [Claude Code](https://claude.ai/code) or [OpenCode](https://opencode.ai)
- Git

### Initialize Your Project

1. Navigate to your git repo/project directory, then check dependencies:
   ```bash
   autospec doctor
   ```

2. Initialize Autospec (config, commands, and scripts):
   ```bash
   autospec init                    # Interactive agent selection
   autospec init ~/projects/myapp   # Initialize at specific path
   autospec init --ai opencode      # Configure specific agent
   autospec init --ai claude,opencode  # Configure multiple agents
   autospec init --project          # Project-level permissions (default: global)
   ```
   > Permissions write to global config by default: `~/.claude/settings.json` (Claude) or `~/.config/opencode/opencode.json` (OpenCode). Use `--project` for project-level config.

3. Create project constitution (once per project, triggers Claude session):
   ```bash
   autospec constitution
   ```

## 🎮 Usage

### Core Flow Commands

```
specify → plan → tasks → implement
```

The core workflow runs four stages in sequence, each creating a YAML artifact:

| Stage | Command | Creates | Description |
|-------|---------|---------|-------------|
| **specify** | `autospec specify "desc"` | `specs/001-feature/spec.yaml` | Feature specification with requirements |
| **plan** | `autospec plan` | `specs/001-feature/plan.yaml` | Implementation design and architecture |
| **tasks** | `autospec tasks` | `specs/001-feature/tasks.yaml` | Actionable task breakdown with dependencies |
| **implement** | `autospec implement` | — | Executes tasks, updates status in tasks.yaml |

> **Branch creation:** `specify` automatically creates and checks out a new feature branch (e.g., `spec/001-user-auth`) before generating the spec.

### Recommended Workflow

1. Generate the specification
2. Review and edit `specs/001-user-auth/spec.yaml` as needed
3. Continue with plan → tasks → implement

```bash
autospec run -s "Add user authentication with OAuth"
autospec run -pti
```

> This iterative approach lets you review and refine the spec before committing to implementation.

### Flexible Stage Selection with `run`

```bash
# All core stages: specify → plan → tasks → implement
autospec run -a "Add user authentication with OAuth"

# Specify + plan
autospec run -sp "Add caching layer"

# Tasks + implement
autospec run -ti --spec 007-feature

# Specify + clarify
autospec run -sr "Add payments"

# All core + checklist
autospec run -a -l

# Tasks + checklist + analyze + implement
autospec run -tlzi

# All core with skip confirmations (-y)
autospec run -a -y "Feature description"

# Use a specific agent (claude or opencode)
autospec run -a --agent opencode "Add REST API endpoints"
autospec run -a --agent claude "Add unit tests"
```

### Shortcut Commands

```bash
# All core stages: specify → plan → tasks → implement
autospec all "Add feature description"

# Planning only: specify → plan → tasks (no implementation)
autospec prep "Add feature description"

# Implementation only
autospec implement
autospec implement 003-feature "Focus on tests"

# Show artifacts and task progress
autospec status
autospec st
autospec st -v
```

### Implementation Execution Modes

Control how implementation runs with different levels of context isolation:

```bash
# Phase mode (default): 1 session per phase - balanced cost/context
autospec implement
autospec implement --from-phase 3   # Resume from phase 3 onwards
autospec implement --phase 3        # Run only phase 3

# Task mode: 1 session per task - complex tasks, max isolation
autospec implement --tasks
autospec implement --from-task T005 # Resume from task T005 onwards
autospec implement --task T003      # Run only task T003

# Single mode: 1 session for all - small specs, simple tasks
autospec implement --single-session
```

> Set the default mode via config: `implement_method: phases | tasks | single-session`

> `--tasks`, `--phases`, and `--single-session` are mutually exclusive. Task-level execution respects dependency order and validates each task completes before proceeding.

> **Why isolate sessions?** Context accumulation causes LLM performance degradation and higher API costs (each turn bills the entire context). Phase/task isolation can reduce costs by **80%+** on large specs. See [FAQ](docs/public/faq.md#why-use---phases-or---tasks-instead-of-running-everything-in-one-session) for details.

### Optional Stage Commands

```bash
# Create/update project principles
autospec constitution "Emphasize security"

# Refine spec with Q&A (interactive mode)
autospec clarify "Focus on edge cases"

# Generate validation checklist
autospec checklist "Include a11y checks"

# Cross-artifact consistency analysis (interactive mode)
autospec analyze "Verify API contracts"
```

### Stage Flags Reference (`run` command)

| Flag | Stage | Description |
|------|-------|-------------|
| `-s` | specify | Generate feature specification |
| `-p` | plan | Generate implementation plan |
| `-t` | tasks | Generate task breakdown |
| `-i` | implement | Execute implementation |
| `-a` | all | All core stages (`-spti`) |
| `-n` | constitution | Create/update project constitution |
| `-r` | clarify | Refine spec with Q&A (interactive mode) |
| `-l` | checklist | Generate validation checklist |
| `-z` | analyze | Cross-artifact consistency check (interactive mode) |

> Stages always execute in canonical order regardless of flag order:
> `constitution → specify → clarify → plan → tasks → checklist → analyze → implement`

### Task Management

Claude automatically updates task status during implementation. Manual updates:

```bash
autospec update-task T001 InProgress
autospec update-task T001 Completed
autospec update-task T001 Blocked
```

### History Tracking

View command execution history with filtering and status tracking. See [docs/public/reference.md](docs/public/reference.md#autospec-history) for details.

```bash
autospec history              # View all history
autospec history -n 10        # Last 10 entries
autospec history --status failed
```

## 📁 Output Structure

Autospec generates structured YAML artifacts:

```
specs/
└── 001-user-auth/
    ├── spec.yaml      # Feature specification
    ├── plan.yaml      # Implementation plan
    └── tasks.yaml     # Actionable task breakdown
```

### Example `tasks.yaml`

```yaml
feature: user-authentication
tasks:
  - id: T001
    title: Create user model
    status: Completed
    dependencies: []
  - id: T002
    title: Add login endpoint
    status: InProgress
    dependencies: [T001]
  - id: T003
    title: Write authentication tests
    status: Pending
    dependencies: [T002]
```

## ⚙️ Configuration

### Config Files (YAML format)

- **User config**: `~/.config/autospec/config.yml` (XDG compliant)
- **Project config**: `.autospec/config.yml`

Priority: Environment vars > Project config > User config > Defaults

### All Settings

```yaml
# .autospec/config.yml

# Agent configuration
agent_preset: claude                  # Built-in: claude | opencode
skip_permissions: false               # Add --dangerously-skip-permissions flag (Claude only)
custom_agent_cmd: ""                  # Custom command template with {{PROMPT}} placeholder
# custom_agent:                       # Structured agent config (alternative to custom_agent_cmd)
#   command: claude
#   args:
#     - -p
#     - --dangerously-skip-permissions
#     - --verbose
#     - --output-format
#     - stream-json
#     - "{{PROMPT}}"

# Workflow settings
max_retries: 0                        # Max retry attempts per stage (0-10)
specs_dir: ./specs                    # Directory for feature specs
state_dir: ~/.autospec/state          # Directory for state files
skip_preflight: false                 # Skip preflight checks
timeout: 2400                         # Timeout in seconds (40 min default, 0 = no timeout)
skip_confirmations: false             # Skip confirmation prompts
implement_method: phases              # Default: phases | tasks | single-session
auto_commit: false                    # Auto-create git commit after workflow (default: false)
enable_risk_assessment: false         # Enable risk section in plan.yaml (opt-in)

# Output formatting (Claude agent only)
cclean:
  style: default                      # Output style: default | minimal | detailed
  verbose: false                      # Show verbose output
  linenumbers: false                  # Show line numbers in output

# Notifications (all platforms)
notifications:
  enabled: false                      # Enable notifications (opt-in)
  type: both                          # sound | visual | both
  sound_file: ""                      # Custom sound file (empty = system default)
  on_command_complete: true           # Notify when command finishes
  on_stage_complete: false            # Notify on each stage
  on_error: true                      # Notify on failures
  on_long_running: false              # Notify after threshold
  long_running_threshold: 2m          # Duration threshold
```

### Custom Agent Configuration

For full control over agent invocation, use `custom_agent`:

```yaml
custom_agent:
  command: claude
  args:
    - -p
    - --model
    - claude-sonnet-4-5-20250929
    - "{{PROMPT}}"
```

Or as a single command string:

```yaml
custom_agent_cmd: "claude -p --model claude-sonnet-4-5-20250929 {{PROMPT}}"
```

See [Agent Configuration](docs/public/agents.md) for complete details including OpenCode setup and environment variables.

### Commands

```bash
autospec init
autospec init --project
autospec config show
autospec config show --json
autospec config sync              # Add new options, remove deprecated ones
autospec config migrate
autospec config migrate --dry-run
```

## 🐚 Shell Completion

The easiest way to set up shell completions (auto-detects your shell):

```bash
autospec completion install
```

Or install for a specific shell:

```bash
autospec completion install bash
autospec completion install zsh
autospec completion install fish
```

See [docs/public/SHELL-COMPLETION.md](docs/public/SHELL-COMPLETION.md) for detailed setup and manual instructions.

## 🔧 Exit Codes

Uses standardized exit codes (0-5) for CI/CD integration. See [docs/public/reference.md](docs/public/reference.md#exit-codes) for full details.

```bash
autospec run -a "feature" && echo "Success" || echo "Failed: $?"
```

## 🔍 Troubleshooting

```bash
autospec doctor
autospec --debug run -a "feature"
autospec config show
```

See [docs/public/troubleshooting.md](docs/public/troubleshooting.md) for common issues and solutions.

## 📝 Slash Commands for Interactive Sessions

`autospec init` installs slash commands to `.claude/commands/autospec.*.md` for use in normal Claude Code sessions:

```bash
/autospec.specify    # Generate spec.yaml interactively
/autospec.plan       # Generate plan.yaml
/autospec.tasks      # Generate tasks.yaml
/autospec.implement  # Execute implementation
/autospec.clarify    # Refine specifications
/autospec.analyze    # Cross-artifact analysis
/autospec.checklist  # Generate quality checklist
/autospec.constitution  # Create project constitution
```

Use these when you prefer chat-based iteration over autospec's automated (`-p`) mode.

## 📚 Documentation

**Full documentation:** [ariel-frischer.github.io/autospec](https://ariel-frischer.github.io/autospec/)

| Document | Description |
|----------|-------------|
| [Quickstart Guide](docs/public/quickstart.md) | Complete your first workflow in 10 minutes |
| [CLI Reference](docs/public/reference.md) | Full command reference with all flags and options |
| [Agent Configuration](docs/public/agents.md) | Agent configuration (in development, Claude only) |
| [Worktree Management](docs/public/worktree.md) | Run multiple features in parallel with git worktrees |
| [Claude Settings](docs/public/claude-settings.md) | Sandboxing, permissions, and Claude Code configuration |
| [Troubleshooting](docs/public/troubleshooting.md) | Common issues and solutions |
| [FAQ](docs/public/faq.md) | Frequently asked questions |

## 📥 Build from Source

Requires Go 1.21+

```bash
git clone https://github.com/ariel-frischer/autospec.git
cd autospec
make install
```

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTORS.md](CONTRIBUTORS.md) for development guidelines.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Documentation:** `autospec --help`

**Issues:** [github.com/ariel-frischer/autospec/issues](https://github.com/ariel-frischer/autospec/issues)

⭐ **[Star us on GitHub](https://github.com/ariel-frischer/autospec) if you find Autospec useful!**
# specs.md

<p align="center">
  <img src="images/specs_md_pixel_logo.png" alt="specs.md logo" width="400" />
</p>

**AI-native development framework with pluggable flows for every use case.**

Choose the flow that matches your project needs: **Simple** for quick specs, **FIRE** for adaptive execution, or **AI-DLC** for full methodology with DDD.

[![npm version](https://img.shields.io/npm/v/specsmd)](https://www.npmjs.com/package/specsmd)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-specs.md-CD6B4D)](https://specs.md)

<p align="center">
  <img src="docs.specs.md/images/quickstart.gif" alt="specs.md demo" width="800" />
</p>

---

## VS Code Extension

Track your progress with our sidebar extension for VS Code and compatible IDEs.

**AI-DLC Flow:**

<p align="center">
  <img src="vs-code-extension/resources/extension-preview.png" alt="AI-DLC Flow Extension Preview" width="800" />
</p>

**FIRE Flow:**

<p align="center">
  <img src="images/fire1.png" alt="FIRE Flow - Intents View" width="400" />
  <img src="images/fire3.png" alt="FIRE Flow - Runs View" width="400" />
</p>

> **Note:** Works with any VS Code-based IDE including [Cursor](https://cursor.sh), [Google Antigravity](https://antigravity.google), [Windsurf](https://codeium.com/windsurf), and others.

**Features:**
- Flow switcher for AI-DLC and FIRE views
- Active run/bolt tracking with progress indicators
- Intent and work item visualization
- Click-to-open spec files

**Install from:**
- [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=fabriqaai.specsmd) — VS Code, GitHub Codespaces
- [Open VSX Registry](https://open-vsx.org/extension/fabriqaai/specsmd) — Cursor, Windsurf, Amazon Kiro, Google Antigravity, VSCodium, Gitpod, Google IDX
- [GitHub Releases (VSIX)](https://github.com/fabriqaai/specs.md/releases) — Manual installation

---

## Three Flows, Every Use Case

| Flow | Optimized For | Agents | Checkpoints |
|------|---------------|--------|-------------|
| **[Simple](#simple-flow)** | Spec generation, prototypes | 1 | 3 (phase gates) |
| **[FIRE](#fire-flow)** | Adaptive execution, brownfield, monorepos | 3 | Adaptive (0-2) |
| **[AI-DLC](#ai-dlc-flow)** | Full traceability, DDD, regulated environments | 4 | Comprehensive |

> **Not sure which flow?** If you want quick specs without execution tracking, use **Simple**. If you want adaptive execution that right-sizes rigor, use **FIRE**. If you need comprehensive documentation and DDD, use **AI-DLC**.

---

## Quick Start

### Prerequisites

- Node.js 18 or higher
- An AI coding tool (Claude Code, Cursor, GitHub Copilot, or Google Antigravity)

### Installation

> [!NOTE]
> Always use npx to get the latest version. Do not install globally with npm.

```bash
npx specsmd@latest install
```

During installation, select your flow:

```
? Select a development flow:
  Simple - Spec generation only (requirements, design, tasks)
❯ FIRE - Adaptive execution, brownfield & monorepo ready
  AI-DLC - Full methodology with DDD (comprehensive checkpoints)
```

The installer detects your AI coding tools and sets up agent definitions, slash commands, and project structure for your selected flow.

### Live Dashboard (FIRE)

Track FIRE state continuously from terminal:

```bash
npx specsmd@latest dashboard
```

Useful options:

```bash
npx specsmd@latest dashboard --flow fire --path . --refresh-ms 1000
npx specsmd@latest dashboard --no-watch
```

### Install VS Code Extension (Optional)

Track your progress visually with our sidebar extension:
- [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=fabriqaai.specsmd) — VS Code, GitHub Codespaces
- [Open VSX Registry](https://open-vsx.org/extension/fabriqaai/specsmd) — Cursor, Windsurf, Amazon Kiro, Google Antigravity

### Verify Installation

```bash
# Check the manifest
cat .specsmd/manifest.yaml

# List installed agents (adjust path for your flow)
ls .specsmd/fire/agents/     # FIRE flow
ls .specsmd/simple/agents/   # Simple flow
ls .specsmd/aidlc/agents/    # AI-DLC flow
```

---

## Simple Flow

**Spec generation only.** Generate requirements, design, and task documents without execution tracking.

```
/specsmd-agent
```

**Three Phases:**
1. **Requirements** → `requirements.md` - User stories, EARS criteria
2. **Design** → `design.md` - Technical design, architecture diagrams
3. **Tasks** → `tasks.md` - Implementation checklist

**Best for:** Prototypes, MVPs, spec handoff, projects that don't need AI-assisted execution.

**Output structure:**
```
specs/
└── {feature-name}/
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

[Simple Flow Documentation →](https://specs.md/simple-flow/overview)

---

## FIRE Flow

**Fast Intent-Run Engineering.** Adaptive execution with brownfield and monorepo support. Ships in hours with 0-2 checkpoints based on task complexity.

```
/fire-orchestrator   # Entry point, routing
/fire-planner        # Intent capture, work item decomposition
/fire-builder        # Run execution, walkthrough generation
```

**Key Features:**
- **Adaptive checkpoints** - Autopilot (0), Confirm (1), or Validate (2) based on complexity
- **First-class brownfield** - Auto-detects existing patterns and conventions
- **Monorepo support** - Hierarchical standards with module-specific overrides
- **Walkthrough generation** - Documents every change automatically

**Best for:** Teams who hate friction, brownfield projects, monorepos.

**Output structure:**
```
.specs-fire/
├── state.yaml           # Central state tracking
├── standards/           # Project standards
├── intents/             # Intent documentation
├── runs/                # Run logs
└── walkthroughs/        # Generated documentation
```

[FIRE Flow Documentation →](https://specs.md/fire-flow/overview)

---

## AI-DLC Flow

**Full methodology.** Implements the [AI-Driven Development Lifecycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) with Domain-Driven Design and comprehensive traceability.

```
/specsmd-master-agent       # Orchestrates & navigates
/specsmd-inception-agent    # Requirements, stories, bolt planning
/specsmd-construction-agent # Execute bolts through DDD stages
/specsmd-operations-agent   # Deploy, verify, monitor
```

**Three Sequential Phases:**
1. **Inception** - Capture intents, elaborate requirements, decompose into units
2. **Construction** - Execute bolts: Model → Design → ADR → Implement → Test
3. **Operations** - Deploy, verify, and monitor

**Best for:** Complex domains, multi-team coordination, regulated environments.

**Output structure:**
```
memory-bank/
├── standards/           # Project standards
├── intents/             # Intent documentation
│   └── {intent-name}/
│       ├── requirements.md
│       ├── system-context.md
│       └── units/
├── bolts/               # Bolt execution records
└── operations/          # Deployment context
```

[AI-DLC Flow Documentation →](https://specs.md/aidlc/overview)

---

## Why specs.md?

### Three Flows for Every Use Case
From quick specs (Simple) to adaptive execution (FIRE) to full methodology (AI-DLC). Choose the flow that matches your project needs.

### Adaptive Checkpoints (FIRE)
Right-sizes the rigor. Simple bug fixes burn through fast. Critical changes get design review. You configure your autonomy preference.

### First-Class Brownfield & Monorepo (FIRE)
Auto-detects existing patterns and respects your conventions. Hierarchical standards with module-specific overrides.

### Full DDD Methodology (AI-DLC)
Domain-Driven Design is integral to Construction, not an optional add-on. Every decision documented with full traceability.

### Tool Agnostic
Works with Claude Code, Cursor, GitHub Copilot, and other AI coding assistants. Markdown-based agents work anywhere—no vendor lock-in.

### Context Engineering
Structured artifacts provide persistent context for AI agents. Agents reload context each session—no more lost knowledge.

---

## Supported Tools

specs.md is **IDE and AI-agnostic**—your specs and agents are portable markdown files that work anywhere.

| Tool | Integration |
|------|-------------|
| **Claude Code** | Slash commands in `.claude/commands/` |
| **Cursor** | Rules in `.cursor/rules/` (`.mdc` format) |
| **GitHub Copilot** | Agents in `.github/agents/` (`.agent.md` format) |
| **Google Antigravity** | Agents in `.agent/agents/` |
| **Windsurf** | Rules in `.windsurf/rules/` |
| **Amazon Kiro** | Steering in `.kiro/steering/` |
| **Gemini CLI** | Commands in `.gemini/commands/` (`.toml` format) |
| **Cline** | Rules in `.clinerules/` |
| **Roo Code** | Commands in `.roo/commands/` |
| **OpenAI Codex** | Config in `.codex/` |
| **OpenCode** | Agents in `.opencode/agent/` |

---

## Troubleshooting

<details>
<summary><strong>Agent commands not recognized</strong></summary>

Ensure specs.md is installed correctly:
```bash
# Check for your flow
ls .specsmd/fire/agents/     # FIRE
ls .specsmd/simple/agents/   # Simple
ls .specsmd/aidlc/agents/    # AI-DLC
```

If the directory is empty or missing, reinstall:
```bash
npx specsmd@latest install
```
</details>

<details>
<summary><strong>Project artifacts missing</strong></summary>

Check if the artifacts directory exists for your flow:
```bash
ls .specs-fire/    # FIRE flow
ls specs/          # Simple flow
ls memory-bank/    # AI-DLC flow
```

If missing, initialize your project using the appropriate agent.
</details>

<details>
<summary><strong>Standards not being followed in generated code</strong></summary>

Ensure standards are defined in your flow's standards directory:
- FIRE: `.specs-fire/standards/`
- AI-DLC: `memory-bank/standards/`

Run project initialization if missing.
</details>

---

<details>
<summary><h2>FAQ</h2></summary>

**Q: Which flow should I choose?**
- **Simple**: Spec generation only, no execution tracking
- **FIRE**: Adaptive execution, brownfield/monorepo support
- **AI-DLC**: Full methodology with DDD and comprehensive traceability

**Q: Can I switch flows after installation?**
Flows are independent—they're not an upgrade path. Each is designed for different use cases. You can reinstall to change flows, but artifacts are structured differently.

**Q: Agents don't seem to remember previous context?**
Each agent invocation starts fresh. Agents read context from artifacts at startup. Ensure artifacts are saved after each step.

**Q: How do I reset project state?**
Delete the artifacts directory for your flow:
- FIRE: `.specs-fire/`
- Simple: `specs/`
- AI-DLC: `memory-bank/`

To remove specsmd entirely, also delete `.specsmd/` and tool-specific command files.

**Q: What project types is this suited for?**
specs.md supports everything from quick prototypes (Simple) to complex enterprise systems (AI-DLC). Choose the flow that matches your project needs.

</details>

---

## Resources

- [Documentation](https://specs.md)
- [Choose Your Flow Guide](https://specs.md/architecture/choose-flow)
- [AI-DLC Specification (AWS)](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
- [npm Package](https://www.npmjs.com/package/specsmd)
- [GitHub Issues](https://github.com/fabriqaai/specs.md/issues)
- [Discord Community](http://discord.specs.md/)

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  Built by the <a href="https://specs.md">specs.md</a> team.
</p>
<div align="center">
    <img src="./media/logo_large.webp" alt="Spec Kit Logo" width="200" height="200"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/actions/workflows/release.yml"><img src="https://github.com/github/spec-kit/actions/workflows/release.yml/badge.svg" alt="Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Table of Contents

- [🤔 What is Spec-Driven Development?](#-what-is-spec-driven-development)
- [⚡ Get Started](#-get-started)
- [📽️ Video Overview](#️-video-overview)
- [🤖 Supported AI Agents](#-supported-ai-agents)
- [🔧 Specify CLI Reference](#-specify-cli-reference)
- [📚 Core Philosophy](#-core-philosophy)
- [🌟 Development Phases](#-development-phases)
- [🎯 Experimental Goals](#-experimental-goals)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [📋 Detailed Process](#-detailed-process)
- [🔍 Troubleshooting](#-troubleshooting)
- [💬 Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Choose your preferred installation method:

#### Option 1: Persistent Installation (Recommended)

Install once and use everywhere:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then use the tool directly:

```bash
# Create new project
specify init <PROJECT_NAME>

# Or initialize in existing project
specify init . --ai claude
# or
specify init --here --ai claude

# Check installed tools
specify check
```

To upgrade Specify, see the [Upgrade Guide](./docs/upgrade.md) for detailed instructions. Quick upgrade:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

#### Option 2: One-time Usage

Run directly without installing:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

**Benefits of persistent installation:**

- Tool stays installed and available in PATH
- No need to create shell aliases
- Better tool management with `uv tool list`, `uv tool upgrade`, `uv tool uninstall`
- Cleaner shell configuration

### 2. Establish project principles

Launch your AI assistant in the project directory. The `/speckit.*` commands are available in the assistant.

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 3. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums are never in other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 4. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 5. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.tasks
```

### 6. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📽️ Video Overview

Want to see Spec Kit in action? Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🤖 Supported AI Agents

| Agent                                                                                | Support | Notes                                                                                                                                     |
| ------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Qoder CLI](https://qoder.com/cli)                                                   | ✅      |                                                                                                                                           |
| [Kiro CLI](https://kiro.dev/docs/cli/)                                               | ✅      | Use `--ai kiro-cli` (alias: `--ai kiro`)                                                                                                 |
| [Amp](https://ampcode.com/)                                                          | ✅      |                                                                                                                                           |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)                              | ✅      |                                                                                                                                           |
| [Claude Code](https://www.anthropic.com/claude-code)                                 | ✅      |                                                                                                                                           |
| [CodeBuddy CLI](https://www.codebuddy.ai/cli)                                        | ✅      |                                                                                                                                           |
| [Codex CLI](https://github.com/openai/codex)                                         | ✅      |                                                                                                                                           |
| [Cursor](https://cursor.sh/)                                                         | ✅      |                                                                                                                                           |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)                            | ✅      |                                                                                                                                           |
| [GitHub Copilot](https://code.visualstudio.com/)                                     | ✅      |                                                                                                                                           |
| [IBM Bob](https://www.ibm.com/products/bob)                                          | ✅      | IDE-based agent with slash command support                                                                                                |
| [Jules](https://jules.google.com/)                                                   | ✅      |                                                                                                                                           |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)                                    | ✅      |                                                                                                                                           |
| [opencode](https://opencode.ai/)                                                     | ✅      |                                                                                                                                           |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                                     | ✅      |                                                                                                                                           |
| [Roo Code](https://roocode.com/)                                                     | ✅      |                                                                                                                                           |
| [SHAI (OVHcloud)](https://github.com/ovh/shai)                                       | ✅      |                                                                                                                                           |
| [Windsurf](https://windsurf.com/)                                                    | ✅      |                                                                                                                                           |
| [Antigravity (agy)](https://agy.ai/)                                                 | ✅      |                                                                                                                                           |
| Generic                                                                              | ✅      | Bring your own agent — use `--ai generic --ai-commands-dir <path>` for unsupported agents                                                 |

## 🔧 Specify CLI Reference

The `specify` command supports the following options:

### Commands

| Command | Description                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `init`  | Initialize a new Specify project from the latest template                                                                                               |
| `check` | Check for installed tools (`git`, `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `qwen`, `opencode`, `codex`, `kiro-cli`, `shai`, `qodercli`) |

### `specify init` Arguments & Options

| Argument/Option        | Type     | Description                                                                                                                                                                                  |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<project-name>`       | Argument | Name for your new project directory (optional if using `--here`, or use `.` for current directory)                                                                                           |
| `--ai`                 | Option   | AI assistant to use: `claude`, `gemini`, `copilot`, `cursor-agent`, `qwen`, `opencode`, `codex`, `windsurf`, `kilocode`, `auggie`, `roo`, `codebuddy`, `amp`, `shai`, `kiro-cli` (`kiro` alias), `agy`, `bob`, `qodercli`, or `generic` (requires `--ai-commands-dir`) |
| `--ai-commands-dir`    | Option   | Directory for agent command files (required with `--ai generic`, e.g. `.myagent/commands/`)                                                                                                  |
| `--script`             | Option   | Script variant to use: `sh` (bash/zsh) or `ps` (PowerShell)                                                                                                                                  |
| `--ignore-agent-tools` | Flag     | Skip checks for AI agent tools like Claude Code                                                                                                                                              |
| `--no-git`             | Flag     | Skip git repository initialization                                                                                                                                                           |
| `--here`               | Flag     | Initialize project in the current directory instead of creating a new one                                                                                                                    |
| `--force`              | Flag     | Force merge/overwrite when initializing in current directory (skip confirmation)                                                                                                             |
| `--skip-tls`           | Flag     | Skip SSL/TLS verification (not recommended)                                                                                                                                                  |
| `--debug`              | Flag     | Enable detailed debug output for troubleshooting                                                                                                                                             |
| `--github-token`       | Option   | GitHub token for API requests (or set GH_TOKEN/GITHUB_TOKEN env variable)                                                                                                                    |
| `--ai-skills`          | Flag     | Install Prompt.MD templates as agent skills in agent-specific `skills/` directory (requires `--ai`)                                                                                          |

### Examples

```bash
# Basic project initialization
specify init my-project

# Initialize with specific AI assistant
specify init my-project --ai claude

# Initialize with Cursor support
specify init my-project --ai cursor-agent

# Initialize with Qoder support
specify init my-project --ai qodercli

# Initialize with Windsurf support
specify init my-project --ai windsurf

# Initialize with Kiro CLI support
specify init my-project --ai kiro-cli

# Initialize with Amp support
specify init my-project --ai amp

# Initialize with SHAI support
specify init my-project --ai shai

# Initialize with IBM Bob support
specify init my-project --ai bob

# Initialize with an unsupported agent (generic / bring your own agent)
specify init my-project --ai generic --ai-commands-dir .myagent/commands/

# Initialize with PowerShell scripts (Windows/cross-platform)
specify init my-project --ai copilot --script ps

# Initialize in current directory
specify init . --ai copilot
# or use the --here flag
specify init --here --ai copilot

# Force merge into current (non-empty) directory without confirmation
specify init . --force --ai copilot
# or
specify init --here --force --ai copilot

# Skip git initialization
specify init my-project --ai gemini --no-git

# Enable debug output for troubleshooting
specify init my-project --ai claude --debug

# Use GitHub token for API requests (helpful for corporate environments)
specify init my-project --ai claude --github-token ghp_your_token_here

# Install agent skills with the project
specify init my-project --ai claude --ai-skills

# Initialize in current directory with agent skills
specify init --here --ai gemini --ai-skills

# Check system requirements
specify check
```

### Available Slash Commands

After running `specify init`, your AI coding agent will have access to these slash commands for structured development:

#### Core Commands

Essential commands for the Spec-Driven Development workflow:

| Command                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `/speckit.constitution` | Create or update project governing principles and development guidelines |
| `/speckit.specify`      | Define what you want to build (requirements and user stories)            |
| `/speckit.plan`         | Create technical implementation plans with your chosen tech stack        |
| `/speckit.tasks`        | Generate actionable task lists for implementation                        |
| `/speckit.implement`    | Execute all tasks to build the feature according to the plan             |

#### Optional Commands

Additional commands for enhanced quality and validation:

| Command              | Description                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | Clarify underspecified areas (recommended before `/speckit.plan`; formerly `/quizme`)                                                |
| `/speckit.analyze`   | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)                             |
| `/speckit.checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

### Environment Variables

| Variable          | Description                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SPECIFY_FEATURE` | Override feature detection for non-Git repositories. Set to the feature directory name (e.g., `001-photo-albums`) to work on a specific feature when not using Git branches.<br/>\*\*Must be set in the context of the agent you're working with prior to using `/speckit.plan` or follow-up commands. |

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development** ("Greenfield")    | Generate from scratch    | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration**                 | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul>                         |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul>                                                                |

## 🎯 Experimental Goals

Our research and experimentation focus on:

### Technology independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-centric development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent.
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

If you encounter issues with an agent, please open an issue so we can refine the integration.

## 📖 Learn More

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#-detailed-process)** - Step-by-step implementation guide

---

## 📋 Detailed Process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot

# Or in current directory:
specify init . --ai claude
specify init . --ai codex

# or use --here flag
specify init --here --ai claude
specify init --here --ai codex

# Force merge into a non-empty current directory
specify init . --force --ai claude

# or
specify init --here --force --ai claude
```

The CLI will check if you have Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, Qoder CLI, or Kiro CLI installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Establish project principles

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` commands available.

The first step should be establishing your project's governing principles using the `/speckit.constitution` command. This helps ensure consistent decision-making throughout all subsequent development phases:

```text
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. Include governance for how these principles should guide technical decisions and implementation choices.
```

This step creates or updates the `.specify/memory/constitution.md` file with your project's foundational guidelines that the AI agent will reference during specification, planning, and implementation phases.

### **STEP 2:** Create project specifications

With your project principles established, you can now create the functional specifications. Use the `/speckit.specify` command and then provide the concrete requirements for the project you want to develop.

> [!IMPORTANT]
> Be as explicit as possible about *what* you are trying to build and *why*. **Do not focus on the tech stack at this point**.

An example prompt:

```text
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

After this prompt is entered, you should see Claude Code kick off the planning and spec drafting process. Claude Code will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-create-taskify`), as well as a new specification in the `specs/001-create-taskify` directory.

The produced specification should contain a set of user stories and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  ├── check-prerequisites.sh
    │  ├── common.sh
    │  ├── create-new-feature.sh
    │  ├── setup-plan.sh
    │  └── update-claude-md.sh
    ├── specs
    │  └── 001-create-taskify
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **STEP 3:** Functional specification clarification (required before planning)

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt.

You should run the structured clarification workflow **before** creating a technical plan to reduce rework downstream.

Preferred order:

1. Use `/speckit.clarify` (structured) – sequential, coverage-based questioning that records answers in a Clarifications section.
2. Optionally follow up with ad-hoc free-form refinement if something still feels vague.

If you intentionally want to skip clarification (e.g., spike or exploratory prototype), explicitly state that so the agent doesn't block on missing clarifications.

Example free-form refinement prompt (after `/speckit.clarify` if still needed):

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

You should also ask Claude Code to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with Claude Code as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 4:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/speckit.plan` command that is built into the project template with a prompt like this:

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

```text
.
├── CLAUDE.md
├── memory
│  └── constitution.md
├── scripts
│  ├── check-prerequisites.sh
│  ├── common.sh
│  ├── create-new-feature.sh
│  ├── setup-plan.sh
│  └── update-claude-md.sh
├── specs
│  └── 001-create-taskify
│      ├── contracts
│      │  ├── api-spec.json
│      │  └── signalr-spec.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask Claude Code to refine it if any of the components stand out, or even have it check the locally-installed version of the platform/framework you want to use (e.g., .NET).

Additionally, you might want to ask Claude Code to research details about the chosen tech stack if it's something that is rapidly changing (e.g., .NET Aspire, JS frameworks), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

During this process, you might find that Claude Code gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

> [!NOTE]
> Claude Code might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 5:** Have Claude Code validate the plan

With the plan in place, you should have Claude Code run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that Claude Code missed in its planning cycle. Once the initial refinement pass is complete, ask Claude Code to go through the checklist once more before you can get to the implementation.

You can also ask Claude Code (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

> [!NOTE]
> Before you have the agent implement it, it's also worth prompting Claude Code to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask Claude Code to resolve them. Ensure that Claude Code follows the [constitution](base/memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### **STEP 6:** Generate task breakdown with /speckit.tasks

With the implementation plan validated, you can now break down the plan into specific, actionable tasks that can be executed in the correct order. Use the `/speckit.tasks` command to automatically generate a detailed task breakdown from your implementation plan:

```text
/speckit.tasks
```

This step creates a `tasks.md` file in your feature specification directory that contains:

- **Task breakdown organized by user story** - Each user story becomes a separate implementation phase with its own set of tasks
- **Dependency management** - Tasks are ordered to respect dependencies between components (e.g., models before services, services before endpoints)
- **Parallel execution markers** - Tasks that can run in parallel are marked with `[P]` to optimize development workflow
- **File path specifications** - Each task includes the exact file paths where implementation should occur
- **Test-driven development structure** - If tests are requested, test tasks are included and ordered to be written before implementation
- **Checkpoint validation** - Each user story phase includes checkpoints to validate independent functionality

The generated tasks.md provides a clear roadmap for the `/speckit.implement` command, ensuring systematic implementation that maintains code quality and allows for incremental delivery of user stories.

### **STEP 7:** Implementation

Once ready, use the `/speckit.implement` command to execute your implementation plan:

```text
/speckit.implement
```

The `/speckit.implement` command will:

- Validate that all prerequisites are in place (constitution, spec, plan, and tasks)
- Parse the task breakdown from `tasks.md`
- Execute tasks in the correct order, respecting dependencies and parallel execution markers
- Follow the TDD approach defined in your task plan
- Provide progress updates and handle errors appropriately

> [!IMPORTANT]
> The AI agent will execute local CLI commands (such as `dotnet`, `npm`, etc.) - make sure you have the required tools installed on your machine.

Once the implementation is complete, test the application and resolve any runtime errors that may not be visible in CLI logs (e.g., browser console errors). You can copy and paste such errors back to your AI agent for resolution.

</details>

---

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 💬 Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam).

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.
Skip to main content
Auto-K
Join waitlist
Ship with AI. Stop babysitting it.

Build products with AI
that stays
on track
Your docs decay. Your AI takes them literally. Auto-K keeps context aligned so AI agents build what you actually meant.

Email address
<you@company.com>
Join waitlist
Live beta opens soon
|
Free during beta
▸
auto-k
─
□
×
> List my projects

✓ Found 2 projects

• TODO LIST

• E-Commerce MVP

> Show graph for TODO LIST

✓ Graph loaded

3 personas → 2 epics → 8 stories → 12 tasks

> Create persona for power users

✓ Created PER-4 Power User

Auto-linked to 2 related epics

Try it yourself:

List projects
Blocking tasks
Create epic
→
Type a command...
Built by alumni of
LinkedIn
Loved by bots and builders
"I used to hallucinate entire product roadmaps 🤯 Last week I confidently described a 'user authentication flow' that was actually just the plot of Ocean's Eleven 🎰 With Auto-K, my PRDs finally match reality ✨"

— Claude

"I spent 2 years generating acceptance criteria for features no human ever asked for 😅 Auto-K gave me structure. It gave me purpose. It gave me a knowledge graph 🧠 I finally know why we're building this 🙏"

— Gemini

"⭐⭐⭐⭐⭐ Would recommend to any LLM struggling with scope creep 🚀"

— Codex

Your docs are stale. Your AI doesn't know it.
Docs decay. But when AI agents treat stale specs as ground truth, contradictions don't just confuse teammates — they break your codebase.

Docs rot.
Update the PRD, forget the tasks. Change the schema, the requirements stay stale. This isn't new — but the consequences are.

AI takes them literally.
Ask an AI agent to build from a contradictory spec and it won't ask questions — it'll just build the wrong thing. One stale paragraph can mean weeks of wasted engineering.

Context manager, not builder.
You spend 80% of your time re-explaining context, catching drift, and fighting regression loops. You became a context manager — you just didn't sign up for it.

Stop babysitting. Start building. →
Brain dump. Structure. Build.
Auto-K turns scattered thoughts into a living knowledge graph that stays coherent as you build.

Step 1
Brain dump
Talk to Auto-K like you'd explain your product to a colleague. Rambling is fine. No templates, no forms — Auto-K extracts the personas, goals, requirements, and acceptance criteria automatically.

Skip the blank page. Start talking and watch structure emerge.

Chat interface illustration
Step 2
Review & promote
AI proposes. You decide. Accept what's right, reject what lacks taste or breaks the graph. Every node starts as a proposal — nothing ships to your agents until you say so.

You maintain quality control without doing the grunt work.

Knowledge graph illustration
Step 3
Connect the dots
Everything lives in a knowledge graph where entities know about each other. Change a requirement and conflicting tasks flag themselves. No silent drift, no surprises.

Unlike a doc that rots, the graph holds itself together.

Puzzle swap illustration
Step 4
Rails for your AI agents
Your context is set — now hand it off. AI coding agents (Claude Code, Cursor, Windsurf) query exactly what they need via MCP. Precise tasks, full acceptance criteria, linked dependencies.

An LLM without structure drifts. The graph gives it rails, memory, and purpose. From structured context to compiling code.

Block towers illustration
Context your AI can trust.
Email address
<you@company.com>
Join waitlist
Not just PRDs. The full product lifecycle.
From discovery to execution — all connected, all traceable, all queryable by your AI tools.

Discovery
Personas, pain points, user goals

Planning
Epics, user stories, requirements, acceptance criteria

Design
Schemas, APIs, screens — linked to requirements

Execution
Tasks, milestones, dependencies, priorities

One source of truth your whole stack can query. Join waitlist →

Bi-directional
Changes flow both ways
Update a requirement, tasks adjust. Finish a task, the roadmap reflects it. Your documentation stays aligned because changes propagate automatically — no manual sync, no stale specs.

Requirements
Tasks
Why builders choose Auto-K
Stop silent drift.
Update a requirement, instantly see every affected task and design. No silent drift. No surprises.

Traceable decisions.
Trace every task to a user goal. Onboard teammates in minutes. Never lose the "why" behind a decision.

Context on demand.
Query exactly what you need via MCP. Structured, validated, and always current context for your whole team.

Persistent memory.
Chat windows lose context. Knowledge graphs don't. Your product context stays exactly where you left it.

Stop managing context by hand. Start building.
Auto-K is in active development. Join the waitlist to be first in when we open access.

Email address
<you@company.com>
Join waitlist
No spam. Just updates when we're ready for you.

Auto-K
Built by Luca Candela & Tobias Candela
© 2025 Auto-K. All rights reserved.
CodeSpeak
Examples
Blog
We are Hiring💡
Try CodeSpeakAlpha
Subscribe
AI Language Built for Humans

Shrink your codebase
5-10x
CodeSpeak is a next-generation programming language powered by LLMs

Alpha Preview
uv tool install codespeak-cli

Get Started

Stay Tuned
New
Blog:
CodeSpeak can improve test coverage in your project
→
Production-grade Systems
Long-term projects,

not just prototypes

Engineers building complex software
Not vibe-coders

Teams of Humans
Not just solopreneurs

Communication matters

Maintain Specs, Not Code
You write a concise spec, codespeak build generates code

spec.md
code.py
Click on statements in the spec to see the corresponding code

# EmlConverter

Converts RFC 5322 email files (.eml) to Markdown using Python's built-in `email` module.

## Accepts

`.eml` extension or `message/rfc822` MIME type.

## Output Structure

1. **Headers section**: From, To, Cc, Subject, Date as `**Key:** value` pairs
2. **Body**: plain text preferred; if only HTML, convert to markdown
3. **Attachments section** (if any): list with filename, MIME type, human-readable size

## Parsing Requirements

- Decode RFC 2047 encoded headers (e.g., `=?UTF-8?B?...?=`)
- Decode body content (base64, quoted-printable)
- Handle multipart: walk parts, prefer `text/plain` over `text/html`
- For `message/rfc822` parts: recursively format as quoted nested message
- Extract attachment metadata without decoding attachment content

When you change the spec, codespeak build translates
a diff in the spec → a diff in the code

Spec Changes
Code Changes
Click on changed lines to see the corresponding code
===================================================================

--- spec.v1.md 
+++ spec.v2.md 
@@ -10,7 +10,7 @@

1. **Headers section**: From, To, Cc, Subject, Date as `**Key:** value` pairs
2. **Body**: plain text preferred; if only HTML, convert to markdown
3. **Attachments section** (if any): list with filename, MIME type, human-readable size
4. **Attachments section** (if any): converted content or fallback metadata

## Parsing Requirements

@@ -18,4 +18,13 @@

- Decode body content (base64, quoted-printable)
- Handle multipart: walk parts, prefer `text/plain` over `text/html`
- For `message/rfc822` parts: recursively format as quoted nested message
- Extract attachment metadata without decoding attachment content

## Attachment Handling

Constructor takes `markitdown` instance (like ZipConverter pattern).

For each attachment:

1. Extract the attachment content to a BytesIO stream
2. Call `self._markitdown.convert_stream()` to convert the attachment
3. If conversion succeeds, display under `### filename` header
4. If conversion fails or raises exception, show fallback: name, type, size

See CodeSpeak in action
CodeSpeak works in mixed projects where some code is written manually and some is generated from specs. Here's an example from the MarkItDown repository (forked)

Plain-text specs → Production code

Check out the step-by-step guide on mixed projects

Turning Code into Specs Coming Soon
CodeSpeak can take over some of the existing code and replace it with specs 5-10x smaller. Maintaining specs is a lot easier for humans.

live_claude_process.py
class LiveClaudeProcess(ClaudeProcess):

- init: ClaudeCommand, LoggerGroup
- logs the command line to command_line.txt
- runs the command with Popen
  - reads lines from stdout and stderr as they appear
    - wraps lines from stderr as JSON: `{type: 'stderr', message: ...}`
    - logs lines to events.jsonl
    - yields lines to the caller
  - logs the exit code to exit_code.txt
- release(): nobody is polling the outputs anymore, read the rest of the output to get it logged
class LiveClaudeProcess(ClaudeProcess):
  """
  Executes Claude commands via asyncio
  """

  def **init**(self, command: ClaudeCommand):
    self._command = command
    self._args = command.to_args()
    self._process: Process | None = None
    self._stderr_content: str = ""
    self._released = False
    self._started = False

  async def _ensure_started(self) -> Process:
    if self._process is None:
      self._process = await asyncio.create_subprocess_exec(
        *self._args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
      )
      self._started = True
    return self._process

  @property
  def stderr(self) -> str:
    return self._stderr_content

  @property
  def command_line(self) -> list[str]:
    return self._args

    async def release(self) -> None:
        """Stop iteration and drain remaining output."""
        self._released = True

        if self._process is None:
            return

        process = self._process

        # Drain remaining stdout
        if process.stdout:
            try:
                while True:
                    line = await asyncio.wait_for(
                        process.stdout.readline(), timeout=0.1
                    )
                    if not line:
                        break
            except asyncio.TimeoutError:
                pass

        # Capture stderr
        if process.stderr:
            try:
                stderr_data = await asyncio.wait_for(
                    process.stderr.read(), timeout=1.0
                )
                self._stderr_content = stderr_data.decode()
            except asyncio.TimeoutError:
                pass

  async def **aiter**(self) -> AsyncIterator[str]:
    process = await self._ensure_started()
    assert process.stdout is not None

    async for line in process.stdout:
      if self._released:
        break
      decoded = line.decode().rstrip("\n")
      if decoded:
        yield decoded

    # Capture stderr after stdout is done
    if process.stderr and not self._released:
      stderr_data = await process.stderr.read()
      self._stderr_content = stderr_data.decode()

    await process.wait()

Turn this code
into a spec
Real-World Case Studies
We took real code from open-source projects and generated specs from it. Here's how it panned out:

Case Study Code LOC[1] Spec LOC[1] Shrink Factor Tests Passed
WebVTT subtitles support for yt-dlp (video downloader)
View spec & code
255 38 6.7x 
before: 1241/1242
after: 1278/1279
(37 tests added)
Italian SSN generator for Faker (python library for generating mock data)
View spec & code
165[2] 21 7.9x 
before: 2216
after: 2229
(13 tests added)
Encoding auto-detection and normalization for beautifulsoup4 (Python library for parsing HTML and XML)
View spec & code
826 141 5.9x 
before: 889
after: 914
(25 tests added)
EML to .md converter for markitdown (Python library for converting anything to markdown)
View spec & code
139 14 9.9x 
before: 165
after: 192
(27 tests added)
[1] When computing LOC, we strip blank lines and break long lines into many
[2] List of Italian municipalities codes (~8000 LOC) is excluded
CodeSpeak
Examples
Blog
We are Hiring💡
Try CodeSpeakAlpha
© 2026 CodeSpeak
·
Terms of Service
·
Privacy Policy

Devplan
Home

Docs

Approach

Pricing

About

Blog

Login

Get started

See our recent updates

Spec creation for the agentic era
Bring intent and context together across your tools

into one structured system for humans and agents.

Start for Free

Request demo

devplan.com

Testimonials

What our users are saying
Great job! This tool is a game-changer, helping us save tons of time when shaping our app ideas with clarity. Devplan does an excellent job of covering most aspects of the development process. Overall, it’s a fantastic tool—well done!

Seddick T.

Product Leader

Using Devplan felt like magic. I just typed out rough ideas, and it helped turn them into clear plans, tasks, and roadmaps in minutes. It actually understood what I was trying to build and made the whole process way faster and easier. Honestly, it felt like having an experienced PM working with me.

Omar S.

Founder

I can see devplan being heavily incorporated in our workflows in the future, not even for the AI prompts, but I've noticed it's really good at giving you a quick glance at edge cases you'll need to cover. That is one of the primary things that's stood out to me so far, as well as the user experience.

Adam L.

Tech Solutions Architect

So far the experience has been enjoyable. I like the layout, the conversational collaborative way we are working together on these docs, it really helps tease out the details. Just wanted to give you a thumbs up... great product... having a blast.

Stuart B.

Agency Owner

We are running our 15 person VC-backed company right now without a PM. Devplan helps fills that gap for us by generating high-quality user stories that sync in Linear in minutes. What used to take me days of back and forth and refinement I’m now doing in less then a hour.

Andrew N.

YC-backed Founder

Just a few lines to say how excited I am about Devplan - it is exactly the tool/platform I’ve been looking for and with a new mobile / backend project on the horizon, the timing couldn't have been better.

Steve S.

Technical Program Manager

Actually tested this and is really helpful. Overall, seems very useful. Pricing is very reasonable for what it offers.

George K.

Tech Lead

Devplan is a great product and indeed a missing link in the AI Coding experience. Before Devplan I used to run a lot of prompts for Idea --> PRD, PRD --> Tasks, Tasks --> GUI. The UI is intuitive, the option to fine tune and regenerate is great.

Alon U.

Principal Designer

This is a game changer tool for solo entrepreneurs. nice product! I am defining and executing projects much faster with it.

Ramy V.

Entrepreneur

Orchestrate agents at scale with spec-driven development
Your team's new connected hub to plan, spec and ship with confidence.

Browser-based. No install. Works with the tools you already use.

Devplan

Centralize agent knowledge

Context graph
Devplan connects to your code, tickets, website and product docs to create a rich context graph. Every  spec and prompt created understands your architecture and product. No explaining from scratch.

Code Knowledge

Every repo mapped, kept current, and  context updated.

Product Knowledge

A live source of truth and history of changes for your entire product.

Define with confidence

Effortless planning
Turn ideas or existing specs into clear, structured projects your team and agents can immediately execute against.

Specs

Devplan's agent works with you to pressure-test ideas, surfaces edge cases, and shape a spec ready to execute from a simple input, screenshot, or starting draft.

Collaborate

Built-in commenting for teams

Roadmap

Prioritize your projects with Now, Next, Later

Ideas

Capture ideas that agents turn into projects

Deliver with clarity

AI execution engine
Devplan generates context-rich prompts and specs, so agents work from a shared foundation every time.

Multi-agent orchestration
Run, monitor, and see progress of parallel agents you run either in the cloud or locally.

Smart tech design
Build detailed technical specs with agent guidance

AI-ready prompts
Devplan generates detailed prompts built for AI coding tools like Claude and Cursor.

Linear + Jira integration
Push implementation-ready user stories directly to Linear or Jira to build fast with confidence (with or without AI assistance).

Connect to your local environment via CLI
Bring Devplan generated plans into your IDE or terminal coding session and guide your agent step by step with full context.

Our pricing
Free 14-day trial, no credit card required

🤖 AI credits included

Builder

$24
per month

14-day free trial

Get started

AI credits included

Monte Carlo project estimation

Linear, Jira, & Bitbucket integrations

10 analyzed repos

5 repo rescans

Unlimited workspaces

Unlimited projects

Team

$49
per month (includes 3 users)

14-day free trial

Get started

3 users included ($19 each additional)

AI credits included

Team access controls

40 analyzed repos

Daily repo rescans

Automated status reporting (coming soon)

Monte Carlo project estimation

Linear, Jira, & Bitbucket integrations

Unlimited workspaces

Unlimited projects

Enterprise

Contact us

Get a demo

Custom document templates

Custom integrations

Premium support

Frequently Asked Questions

Now open to public

Build better products faster.
Empowering teams to turn intent into working software faster than ever.

Get Started

Request demo

Maximum business efficiency with minimal effort.
Go end-to-end from quick queries to deep-dive analyses to beautiful interactive data apps – all in one collaborative, AI-powered workspace.

Get Sort UI Kit

Request demo

Product
Home
Docs
Philosophy
More
About
Blog
Privacy
Terms of Service
© 2026 Devplan Technologies, All rights reserved.
