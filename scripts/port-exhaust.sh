#!/bin/bash

/root/dns64perfpp-a/dns64perf++v4 192.0.2.2 53 0.0.0.0/5 60000 1 1 60000 550000 0.1


# Syntax
# Usage: dns64perf++ <server> <port> <subnet>
#  <number of requests> <burst size> <number of threads> <number of ports per thread> <delay between bursts in ns> <timeout in s>
