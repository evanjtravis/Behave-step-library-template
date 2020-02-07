MODNAME     := XXXXXXXXXX
PKG         := sdg/test/behave/$(MODNAME)
TPKG        := sdg/test/behave/$(MODNAME)/tests
export TSTS := $(wildcard $(TPKG)/*.py $(TPKG)/*/*.py)
export SRCS := $(wildcard $(PKG)/*.py)

.PHONY: test all clean perms

all: build .drone.yml.sig

build: setup.py $(SRCS)
	pip install -r requirements.txt
	python3 setup.py test
	@touch .test
	python3 setup.py bdist_wheel

clean:
	rm -rf build dist *.egg-info .test
	find . -name "__pycache__" | xargs --no-run-if-empty rm -rf

coverage:
	coverage run setup.py test
	coverage combine
	coverage report -m

.drone.yml.sig: .drone.yml
	drone sign techservicesillinois/test-behave-$(MODNAME)

perms:
	# make sure files and directories are world-readable
	find . -type f | xargs --no-run-if-empty chmod go+r
	find . -type d | xargs --no-run-if-empty chmod 755

.test: $(SRCS) $(TSTS)
	python3 setup.py test
	@rm -rf build dist *.egg-info .test
	@touch .test

test: .test


