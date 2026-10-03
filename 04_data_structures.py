""" 
- Lists, 
- Tuples, 
- Sets, and 
- Dictionaries.
"""


from collections import defaultdict, deque

# Lists: Mutable Ordered Sequences

scores = [88, 92, 79, 93, 85]
scores.append(100)
scores.sort(reverse=True)
top_three = scores[:3]

print(f"Top 3 Scores: {top_three}")


# Tuples: Immutable Sequences & Unpacking

server_endpoint = ("127.0.0.1", 8080)
host, port = server_endpoint

print(f"Binding to {host}:{port}")