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
