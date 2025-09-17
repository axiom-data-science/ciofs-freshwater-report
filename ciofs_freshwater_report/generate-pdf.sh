#!/bin/bash

cd "$(dirname $0)"
export USERID=$(id -u)
export GROUPID=$(id -g)
docker compose build #--no-cache
docker compose run --rm pdf "$@"
# docker run -it --rm ciofs_freshwater_report-pdf /bin/bash
# docker run -it --rm ciofs_freshwater_report-pdf /bin/bash
