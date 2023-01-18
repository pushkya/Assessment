.PHONY: dependencies
pip-install:
	pip install -r requirements.txt

.PHONY: docker
start:
	docker-compose up -d
stop:
	docker-compose down --remove-orphans
clean:
	docker system prune -f

.PHONY: python
perform-etl:
	python ETL.py --e http://localhost:4566 --q login-queue --m 25