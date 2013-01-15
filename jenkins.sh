#!/usr/bin/env bash
set -e

export PYTHONPATH=$PYTHONPATH:$(pwd)
python uptime/test.py
