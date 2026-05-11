PYTHON ?= python3
SRC_DIR := src
INPUT_DIR := input
OUTPUT_DIR := output
ENTRYPOINT := $(SRC_DIR)/main.py

.PHONY: all clean

all:
	$(PYTHON) $(ENTRYPOINT) --input $(INPUT_DIR) --output $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR)/*
