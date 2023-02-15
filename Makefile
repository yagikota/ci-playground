generate/migration/file:
	$(eval DATE:=$(shell TZ=JST-9 date "+%Y%m%d%H%M%S"))
	touch migrations/${DATE}-${FILE_NAME}.sql
