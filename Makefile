run-project:
			poetry run run-project

lint:
	poetry run flake8 test_coverage_project


build:
	poetry build


publish:
	 poetry publish --dry-run


package-install:
	 python3 -m pip install --user dist/*.whl



package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl


package-uninstall:
	python3 -m pip uninstall test-coverage-project

