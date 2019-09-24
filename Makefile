MAIN := 01-coming-soon 02-sponsors 03-keynotes 03.1-talks 03.2-speakers 04-about 05-venue 06-team 07-contact

DATE = $(shell date +"%Y%m%d")

all: index.html blog.html jobs.html

index.html: head $(MAIN) tail
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"


blog.html: head 01-coming-soon blog tail
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

jobs.html: head 01-coming-soon jobs tail
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
	cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"
