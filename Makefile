up:
	docker compose up -d && serverless deploy --stage local

clean:
	docker compose down && rm -rf .serverless

.PHONY: \
	up \
	clean \
