#MAIN := 01-coming-soon 02-sponsors 03-keynotes
#MAIN += 03.1-talks 03.2-speakers 03.3-panel 03.4-workshops
#MAIN += 04-about 05-venue 06-team 07-contact

MAIN := 01-menu 02-callout 03-keynotes 04-talks 05-panels 06-venue 07-sponsors 08-about 09-board 10-contact

DATE = $(shell date +"%Y%m%d")

all: index.html blog.html jobs.html sponsorship.html

index.html: index_header $(MAIN) html_footer
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

blog.html: blog_header 01-menu 02-callout $(BLOG) 10-contact html_footer
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

jobs.html: jobs_header 01-menu 02-callout jobs 10-contact html_footer
	@if [ -f $@ ]; then \
		echo "Moving $@ to $@.$(DATE)"; \
		mv $@ $@.$(DATE); \
	fi
	@for block in $^; \
		do echo " $$block to $@ " ; \
	cat $$block >> $@ ; \
	done
	@echo "$@ has been generated"

sponsorship.html: sponsorship_header 01-menu 02-callout sponsorship 10-contact html_footer
		@if [ -f $@ ]; then \
			echo "Moving $@ to $@.$(DATE)"; \
			mv $@ $@.$(DATE); \
		fi
		@for block in $^; \
			do echo " $$block to $@ " ; \
		cat $$block >> $@ ; \
		done
		@echo "$@ has been generated"
