.PHONY: dependencies
pip-install:
	pip install -r requirements.txt
aws-configure:
	bash aws_configure.sh
.PHONY: docker
start:
	docker-compose up -d
stop:
	docker-compose down --remove-orphans
clean:
	docker system prune -f

.PHONY: python
etl:
	python ETL_main.py --e http://localhost:4566 --q login-queue --m 25
