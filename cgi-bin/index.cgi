#!/bin/bash

OUTPUT=""
if [ ! -z "$QUERY_STRING" ] ; then
  KEY=$(echo $QUERY_STRING | cut -d'=' -f 1)
  VAL=$(echo $QUERY_STRING | cut -d'=' -f 2)
  KEY=$(echo $KEY | tr % = | nkf -WwmQ )
  VAL=$(echo $VAL | tr % = | nkf -WwmQ )
  #### make mojibake
  VAL=$(echo $VAL | nkf -Sw | nkf -Ws)
fi


cat << EOF
Content-type:application/json; charset=utf-8

{
  "key": "$KEY",
  "value": "$VAL"
}
EOF

exit 0
