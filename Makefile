run-tests:
	pytest -v tests

create-test-report:
	pytest --html=report.html --self-contained-html tests
