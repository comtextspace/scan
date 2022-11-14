build:
	poetry run python main.py

clear:
	del .\template\scans.json

check:
	poetry run python check.py