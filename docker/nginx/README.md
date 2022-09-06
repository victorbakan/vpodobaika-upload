This Nginx is used as a public frontend proxy with fixed rate limit by default with 5r/s per 1 IP address + burst up to 10r/s for short term
Please change configuratoin in:
- nginx.conf - here is main configuration + rate limit
- api-service.conf - here is main configuration for api-service where nginx forwards its traffic
