from fluidasserts.proto import http
from fluidasserts.proto import ssl

ssl.has_heartbleed('gazzetta.gr')
ssl.has_heartbleed('fluidattacks.com')
http.has_host_header_injection('https://fluidattacks.com')
