curl -X GET "http://$1/service/rest/v1/components?repository=$2" -u $3 -H "accept: application/json"  | grep "continuationToken" | awk -F '"' '{print $4}' > token.txt
​
declare -i line=1;
​
while true
do
	x=$(sed -n "$line p" token.txt);
	echo $x;
	[ -z "$x" ] && break
	curl -X GET "http://$1/service/rest/v1/components?continuationToken=$x&repository=$2" -u $3 -H "accept: application/json"  | grep "continuationToken" | awk -F '"' '{print $4}' >> token.txt
	line=$((line+1));

done


echo "app,version,id" > id.txt
curl -X GET "http://$1/service/rest/v1/components?repository=$2" -u $3 -H "accept: application/json"  | jq -r '.items | keys[] as $k | "\(.[$k] | .name),\(.[$k] | .version),\(.[$k] | .id)" ' >> id.txt

declare -i line=1;

while true
do
	x=$(sed -n "$line p" token.txt);
	echo $x;
	[ -z "$x" ] && break
	curl -X GET "http://$1/service/rest/v1/components?continuationToken=$x&repository=$2" -u $3 -H "accept: application/json"  | jq -r '.items | keys[] as $k | "\(.[$k] | .name),\(.[$k] | .version),\(.[$k] | .id)" ' >> id.txt
	line=$((line+1));
done
