init:
	pip install -r requirements.txt
	python3 -m spacy download fr_core_news_sm

test:
	pytest --cov=src test/