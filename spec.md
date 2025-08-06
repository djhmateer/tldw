## Project: TLDW – Too Long Didn’t Write

1. Project Overview

**Tagline:** Shortform writing, supercharged by AI. Stay focused, write better

**Goal:** 

### Goal

- Minimalist, privacy-first writing environment  
- Real-time AI writing assistance  
- Distraction-free and keyboard-centric UX  
- Integration with developer tools  
- Templates and examples for high-quality technical writing  

TLDW is designed to support developers and technical professionals who need to write clearly and quickly without switching mental context. It offers real-time AI assistance—including spell check, grammar correction, clarity suggestions, and tone refinement—while staying out of the way.

The interface is deliberately minimal, enabling focus without visual clutter. Keyboard-driven controls (including Vim bindings) allow power users to move quickly, while integrations with tools like Cursor, Git, and GitHub make it easy to plug TLDW into existing workflows.

By providing best-in-class templates for common technical writing scenarios (e.g., commit messages, pull requests, changelogs, documentation, and blog posts), along with built-in examples of effective writing, TLDW helps raise the bar for communication across teams.

**Audience:** 

- Developers and engineers writing in high-velocity environments  
- Teams who care about readable, consistent, and correct technical writing  
- Users of Git, GitHub, GitBook, Cursor, and command-line tools  
- Technical writers, DevOps engineers, open-source maintainers, and indie hackers  
- Anyone who wants a clean writing space with real-time spell/grammar checks, style feedback, and strong templates—without distractions


2. Core Features

### 2. Core Features Checklist

#### 🔐 Authentication
- [ ] Login with email and password

#### 📝 Writing Environment
- [ ] Minimalist, distraction-free interface (no toolbars, no chrome)
- [ ] Fullscreen mode with light/dark toggle
- [ ] Markdown-first editing with syntax highlighting
- [ ] Real-time rendering of Markdown preview (toggleable)

#### ⌨️ Keyboard-Centric Controls
- [ ] Vim bindings for modal editing
- [ ] Command palette (Cmd/Ctrl + P) for all actions
- [ ] Customizable keyboard shortcuts
- [ ] Hotkeys to toggle:
  - [ ] AI suggestions
  - [ ] Spell check
  - [ ] Grammar check

#### 🧠 AI Writing Assistance
- [ ] Inline spell check with smart suggestions
- [ ] Grammar and tone feedback
- [ ] Tab-to-accept suggestions (GitHub Copilot-style UX)
- [ ] Configurable: local LLM or remote API-based LLM
- [ ] All AI features opt-in and fully toggleable

#### 📚 Templates & Writing Starters
- [ ] Built-in templates for:
  - [ ] Commit messages
  - [ ] Pull requests
  - [ ] Changelogs
  - [ ] Documentation
  - [ ] Blog posts
- [ ] “Insert Template” keyboard shortcut
- [ ] In-editor guidance on tone and structure
- [ ] Custom/user-defined templates

#### 🕒 Versioning & History
- [ ] Automatic version saves every 5 seconds of user inactivity
- [ ] Infinite version history with timestamped entries
- [ ] View two versions side by side with diff highlighting
- [ ] Copy content from any version to create a new document or overwrite current
- [ ] Version browsing accessible via command palette or shortcut (e.g., `Cmd/Ctrl + Shift + V`)



## 3. User Flow

This section outlines how users interact with TLDW, emphasizing speed, clarity, and minimalism with keyboard-first controls.

---

### 3.1. First-Time Use

**Entry Point:**  
User lands on homepage or shared link.

**Flow:**
1. Clean welcome screen with tagline and feature highlights  
2. Prompted to log in or sign up with email/password  
3. Optional 1-minute onboarding (keyboard-first tips)  
4. Redirected to writing interface with placeholder (“Start writing…”)

---

### 3.2. Returning User

**Entry Point:**  
Direct visit or bookmark to editor URL.

**Flow:**
1. Auto-login (if session exists) or email/password prompt  
2. Redirected to last open or new document  
3. AI suggestions, spell check, grammar are off by default  
4. Cursor focuses into editor; user can immediately type

---

### 3.3. Writing & Editing Flow

**Flow:**
1. Write in Markdown with syntax highlighting  
2. Inline feedback for spelling, grammar, and tone (if toggled on)  
3. Use keyboard to:  
   - Toggle AI assist, spell/grammar checks  
   - Open command palette (Cmd/Ctrl + P)  
   - Insert template or style guidance  
4. Accept suggestion with Tab  
5. Dismiss with Esc or Caps Lock  
3. Every x seconds triggers an autosave version snapshot
6. Optional: toggle dark mode or fullscreen view

---

### 3.4. Using Templates

**Flow:**
1. Press shortcut to open "Insert Template" menu  
2. Choose from:  
   - Commit messages  
   - Pull requests  
   - Changelogs  
   - Documentation  
   - Blog posts  
   - CLI tool help messages  
   - README.md snippets  
   - Onboarding or setup instructions  
   - Dev journal/log templates  
   - API changelog or version notes  
   - “What’s new” product update notes  
3. Inserted template includes structure and tone/style notes inline  
4. Begin editing with keyboard

---

### 3.5. AI Assistance Flow

**Flow:**
1. Toggle AI suggestions on via keyboard or command palette  
2. Inline suggestions for clarity, tone, grammar, spelling  
3. Accept with Tab  
4. Dismiss with Esc or Caps Lock  
5. User can configure which AI tools to show (all optional and off by default)  
6. No local LLM; all suggestions powered by secure remote API

---

### 3.6. Export / Save Flow

**Flow:**
1. Autosave enabled every x seconds during writing  
2. Version history saved locally (maybe) and/or to account
3. User can open history and view:
   - Timestamps of autosaves  
   - Side-by-side diffs  
   - Option to restore or duplicate versions  


## 4. Technical Stack


TLDW is designed with simplicity, performance, and full-stack control in mind. The stack is minimal yet powerful, optimized for fast keyboard-driven editing and real-time AI assistance.

- **Backend Framework:**  
  [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13.5) – modern async Python framework with high performance and clean developer ergonomics.

- **Database:**  
  [PostgreSQL](https://www.postgresql.org/) – self-hosted, reliable relational database with strong consistency and extensibility.

- **Frontend Stack:**  
  - **HTML + Tailwind CSS v4** – utility-first CSS framework for rapid, consistent UI styling  
  - **TypeScript** – type-safe scripting for UI interactions and logic  
  - **shadcn/ui** – component library built on Radix UI and Tailwind, used for dropdowns, modals, command palette, and other primitives

- **Authentication:**  
  - Username and password login  
  - Auth implemented using session cookies or JWT (TBD)

- **AI Integration:**  
  - Inline AI suggestions via remote API (e.g., OpenAI or hosted model endpoint)  
  - Ghost-text style feedback (clarity, grammar, tone), triggered via keyboard shortcuts

- **Deployment Environment:**  
  - Hosted on self-managed **Proxmox VM** (Ubuntu)  
  - Reverse proxy via **Nginx**  
  - Process control with **systemd**  
  - HTTPS managed by **Certbot / Let’s Encrypt**

- **Editor Engine (Pluggable / TBD):**  
  Evaluation is ongoing for the best editor setup that balances speed, Markdown fidelity, and ease of AI integration. Options under consideration include:

  - **Custom-built Markdown editor**  
    - Lightweight, keyboard-centric  
    - Syntax highlighting via `highlight.js` or `Prism.js`  
    - AI ghost text rendered inline using spans or overlays  

  - **`textarea` + syntax highlighter overlay**  
    - Minimal dependencies, fully controllable  
    - Easier to debug and extend  
    - Great for power-user control and Vim bindings  

  - **Monaco Editor (used in VS Code)**  
    - Powerful, feature-rich  
    - Native support for Markdown, Vim mode, and inline decorations  
    - Heavier dependency, larger JS bundle  

  - **CodeMirror 6**  
    - Modular, performant, and modern  
    - Excellent keyboard support and syntax highlighting  
    - Supports inline suggestions and ghost text  
    - Medium complexity and learning curve

  Final selection will depend on performance benchmarks and integration complexity with AI suggestion overlays and keyboard shortcuts.


5.Data Models

```sql
-- Stores user credentials and editor preferences
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,

  dark_mode BOOLEAN DEFAULT FALSE,
  vim_mode BOOLEAN DEFAULT FALSE,
  autosave_interval INTEGER DEFAULT 5,
  ai_suggestions_enabled BOOLEAN DEFAULT FALSE,
  spellcheck_enabled BOOLEAN DEFAULT FALSE,
  grammarcheck_enabled BOOLEAN DEFAULT FALSE,
  tonecheck_enabled BOOLEAN DEFAULT FALSE,

  last_active_doc_id INTEGER REFERENCES documents(id),

  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Top-level documents (one per writing project)
CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  current_version_id INTEGER REFERENCES document_versions(id),
  user_id INTEGER REFERENCES users(id),
  is_deleted BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Full history of edits (title and content per version)
CREATE TABLE document_versions (
  id SERIAL PRIMARY KEY,
  document_id INTEGER REFERENCES documents(id),
  title TEXT,
  content TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Built-in templates for writing assistance
CREATE TABLE templates (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  content TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Authentication sessions (optional if using JWT)
CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  token TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  expires_at TIMESTAMP NOT NULL
);
```

6.API Endpoints

These endpoints support the core features of the TLDW writing environment. All responses are in JSON format. Authentication is required for most routes and can be implemented via session cookies or JWT.

---

### Authentication

#### `POST /auth/login`  
Authenticate a user with email and password.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "hunter2"
}
```

**Response:**
```json
{
  "token": "jwt-or-session-token",
  "user_id": 1,
  "preferences": {
    "dark_mode": true,
    "vim_mode": false,
    "ai_suggestions_enabled": false
  }
}
```

---

### Documents

#### `GET /documents`  
Return a list of documents for the authenticated user.

**Query Parameters (optional):**
- `limit`
- `offset`

**Response:**
```json
[
  {
    "id": 12,
    "title": "My Project Docs",
    "updated_at": "2025-08-04T09:13:55Z"
  }
]
```

#### `POST /documents`  
Create a new document (optionally from a template).

**Request Body:**
```json
{
  "title": "New Doc",
  "template_id": 3  // optional
}
```

**Response:**
```json
{
  "document_id": 42,
  "version_id": 113,
  "content": "# Start writing..."
}
```

#### `GET /documents/{id}`  
Retrieve a specific document and its current content.

**Response:**
```json
{
  "id": 42,
  "title": "New Doc",
  "content": "# Start writing...",
  "updated_at": "2025-08-04T09:14:00Z"
}
```

---

### Version History

#### `POST /documents/{id}/versions`  
Save a new version of a document (autosave or manual).

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "## New content here..."
}
```

**Response:**
```json
{
  "version_id": 114,
  "created_at": "2025-08-04T09:16:00Z"
}
```

#### `GET /documents/{id}/versions`  
Get all saved versions of a document.

**Response:**
```json
[
  {
    "version_id": 110,
    "title": "Initial Draft",
    "created_at": "2025-08-03T15:22:17Z"
  },
  {
    "version_id": 111,
    "title": "Added Section 2",
    "created_at": "2025-08-03T15:30:20Z"
  }
]
```

---

### Templates

#### `GET /templates`  
Return all built-in templates grouped by category.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Commit Message",
    "category": "git",
    "content": "feat(scope): short summary\n\nLonger explanation..."
  },
  {
    "id": 4,
    "name": "Blog Post Outline",
    "category": "blog",
    "content": "# Title\n\n## Intro\n\n## Sections..."
  }
]
```

7.UI Layout

The TLDW interface is built using **Tailwind CSS v4** and the **shadcn/ui** component library (Radix UI primitives). The goal is to create a **minimal, fast, keyboard-centric** writing experience with consistent design and responsive behavior.

---

### Pages

- **Landing**
  - Tagline, feature highlights, login/signup call-to-action
- **Editor**
  - Core writing environment with Markdown, AI suggestions, templates, version history
- **Login / Signup**
  - Clean, minimal authentication forms with animated transitions
- **Modals / Overlays**
  - Used for command palette, template browser, version diff viewer

---

### Shared Components (via `shadcn/ui`)

- `<Dialog>` – Login/signup, templates, version history overlays
- `<Popover>` – Export and settings menus
- `<Command>` – Global command palette (keyboard-invoked)
- `<Toggle>` – AI assist, spell check, and grammar toggles
- `<Tooltip>` – Button descriptions on hover or focus
- `<DropdownMenu>` – User account menu (logout, preferences)
- `<Tabs>` – Optional layout for version comparisons
- `<Textarea>` – Markdown editor with syntax highlighting and ghost text overlay
- `<Button>` – Used for actions like save, export, insert template

---

### Layout System

**Grid & Responsiveness**

- Tailwind Grid or Flexbox layout
- `lg:` screens: two-column layout (sidebar/palette + editor)
- `sm` / `md`: single-column stacked layout

**Responsive Breakpoints**

- `sm` – 640px: phones
- `md` – 768px: tablets
- `lg` – 1024px: laptops (default 2-column)
- `xl` – 1280px and up: large displays, split views

**Spacing & Consistency**

- Use Tailwind spacing scale: `gap-4`, `px-6`, `space-y-4`
- Components should use `rounded-2xl`, `shadow-md`, or `shadow-none`
- Animations via `transition-all duration-150 ease-in-out`

---

### Editor UI Guidelines

- **Dark Mode**
  - Implemented via `shadcn/ui` `<ThemeProvider>` and Tailwind `dark:` classes
- **Fullscreen Mode**
  - Triggered via keyboard shortcut, hides all chrome
- **Ghost Text for AI Suggestions**
  - Rendered inline as spans or overlays on `<Textarea>`
- **Command Palette**
  - Powered by `<Command>`, invoked via `Cmd/Ctrl + P`
- **Templates Menu**
  - Appears as `<Dialog>` with optional `<Tabs>` for categories
- **Version Diff Viewer**
  - Rendered in overlay modal using `<Tabs>` or 2-column `<Grid>`
- **Keyboard Shortcuts**
  - All features accessible via keyboard; bindings shown in command palette
- **Autosave Feedback**
  - Use `<Toast>` or non-blocking snackbar for saved status

---

### Accessibility & UX

- Use semantic HTML elements: `<main>`, `<nav>`, `<section>`, etc.
- All `shadcn/ui` components are accessible (Radix compliance)
- Keyboard-first support built into modals, menus, and command palette
- Use `aria-live` for dynamic content like autosaves or AI feedback
- Theme switching should support high-contrast and `dark:` variants

---

### Component Layout Example (Editor Page)

```txt
lg:grid lg:grid-cols-[minmax(0,1fr)_3fr] gap-6 px-6 py-8

[ Sidebar / Palette ]  |  [ Editor + AI Suggestions + Command Palette ]
