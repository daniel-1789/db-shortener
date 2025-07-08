Prompt
Build a minimal in-memory URL shortener.

Implement two functions:

shorten_url(long_url: str, user_id: str) -> str

resolve_url(short_url: str) -> Optional[str]

Requirements:

A user can shorten any URL.

You should return a shortened version like "http://short.ly/abc123".

You can generate the short code however you like.

Keep everything in memory — no external libraries or persistence.

You may define any helper functions, classes, or data structures you find useful.