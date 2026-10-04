"""

- String manipulation, 
- regex basics, and 
- datetime handling.

"""

from datetime import datetime, timedelta, timezone
import re

# 1) String cleaning and splitting
raw_log = "  [ERROR] 2026-10-03: Connection timed out to remote host.  "
cleaned_log = raw_log.strip()  # remove leading/trailing spaces

# Split into log level and message by the first ': ' after the date
parts = cleaned_log.split(": ", 1)
tag = parts[0]
log_body = parts[1] if len(parts) > 1 else ""
print(f"Tag: {tag} | Message: {log_body}")

# 2) Email validation using regex
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
test_email = "engineer@example.com"
is_valid_email = bool(re.match(email_pattern, test_email))
print(f"Email '{test_email}' valid: {is_valid_email}")

# 3) Current UTC timestamp and formatting
current_utc = datetime.now(timezone.utc)
formatted_now = current_utc.strftime("%Y-%m-%d %H:%M:%S %Z")
print(f"Timestamp: {formatted_now}")

# 4) Date arithmetic and parsing
# Add 14 days and 6 hours to current time
future_deadline = current_utc + timedelta(days=14, hours=6)

# Parse a date string and attach UTC timezone information
parsed_date = datetime.strptime("2026-12-31 23:59:59", "%Y-%m-%d %H:%M:%S").replace(
    tzinfo=timezone.utc
)

# Calculate time remaining until the end of the year
# .days gives number of full days between the datetimes
# (ignoring the remaining hours/minutes/seconds)
time_to_end_of_year = parsed_date - current_utc

print(f"Deadline in: {future_deadline.isoformat()}")
print(f"Days left in year: {time_to_end_of_year.days} days")