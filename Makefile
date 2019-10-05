MAIN := 01-coming-soon 02-sponsors 03-keynotes
MAIN += 03.1-talks 03.2-speakers 03.3-panel 03.4-workshops
MAIN += 04-about 05-venue 06-team 07-contact

DATE = $(shell date +"%Y%m%d")

all: index.html blog.html jobs.html sponsorship.html

index.html: header $(MAIN) footer
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

BLOG := blog_00 blog_02 blog_01

blog.html: header 01-coming-soon $(BLOG) footer
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

jobs.html: header 01-coming-soon jobs footer
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
	cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

sponsorship.html: header 01-coming-soon sponsorship footer
		@if [ -f $@ ]; then \
			echo "Moving $@ to $@.$(DATE)"; \
			mv $@ $@.$(DATE); \
		fi
		@for block in $^; \
			do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
		done
		@echo "$@ has been generated"
