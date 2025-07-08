#!/bin/bash

wc -l seasonal/*.csv | grep - v total | sort -n | head -n 1