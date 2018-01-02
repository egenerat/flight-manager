ARCHIVE_NAME=archive.tar
tar cvf $ARCHIVE_NAME app.yml settings.py app/common/constants.py app/common/constants_strategy.py app/common/target_urls.py app/common/target_strings.py app/common/target_parse_strings.py app/test/parsers/resources_planes_html.py tests_util/test_pages/* app/analyzer/data/**/*.{py,txt,csv}
tar -vf $ARCHIVE_NAME --delete app/analyzer/data/input/airports.csv
cat ../gpg_key |gpg --batch --yes --passphrase-fd 0 -c $ARCHIVE_NAME
rm $ARCHIVE_NAME
# git add $ARCHIVE_NAME.enc
