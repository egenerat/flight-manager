ARCHIVE_NAME=archive.tar
tar cvf $ARCHIVE_NAME app/common/constants.py app/common/constants_strategy.py app/common/target_urls.py app/common/target_strings.py app/common/target_parse_strings.py app/test/parsers/resources_planes_html.py tests_util/test_pages/*
travis encrypt-file $ARCHIVE_NAME --add -f
# git add ${ARCHIVE_NAME}.enc