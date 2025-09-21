#!/bin/bash
# wait-for-postgres.sh
set -e
host=&quot;$1&quot;
shift
cmd=&quot;$@&quot;
until PGPASSWORD=mypassword psql -h &quot;$host&quot; -U &quot;myuser&quot; -d &quot;mydb&quot; -c &#39;\q&#39;; do
&gt;&amp;2 echo &quot;Postgres is unavailable - sleeping&quot;
sleep 1
done
&gt;&amp;2 echo &quot;Postgres is up - executing command&quot;
exec $cmd