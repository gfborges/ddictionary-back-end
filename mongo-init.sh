# /bin/sh
for collection_file in /test/data/*.json; do
    mongoimport --jsonArray --db ddictDB --collection "${collection_file%%.*}" --file "${collection_file}"
done
