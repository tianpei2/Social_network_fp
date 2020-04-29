#!/bin/bash

if [ ! $# -eq 2 ]
then
	echo "Usage: ./countSingleDay.sh yyyy-mm-dd(start date) yyyy-mm-dd(end date)"
	echo "Check out.date to get the results"
	exit 0
fi

format_start_date=$1
format_end_date=$2

prefix=${format_start_date:0:8}

start_month=${format_start_date:5:2}
end_month=${format_end_date:5:2}

start_date=${format_start_date:8}
end_date=${format_end_date:8}

first_of_start_date=${start_date:0:1}
first_of_end_date=${end_date:0:1}

if [ x$first_of_start_date == x"0" ]
then
	start_date=${start_date:1}
fi

if [ x$first_of_end_date == x"0" ]
then
	end_date=${end_date:1}
fi

if [ ! x$start_month == x$end_month ]
then
	end_date=32
fi

echo "Date,Count" > out.date

cnt=0
while true
do
	if [ x$start_date == x$end_date ]
	then
		break
	fi

	next_date=$((start_date+1))

	format_start_date=$start_date
	if [ $start_date -lt 10 ]
	then
		format_start_date=0$start_date
	fi

	format_next_date=$next_date
	if [ $next_date -lt 10 ]
	then
		format_next_date=0$next_date
	fi

	echo "Start processing $prefix$format_start_date..."

	times=0
	while true
	do
		python Exporter.py --querysearch "Coronaoutbreak" --since $prefix$format_start_date --until $prefix$format_next_date
		tmp=`cat output_got.csv | wc -l`
		if [ $tmp -ge 1 ] || [ $times -gt 10 ]
		then
			break
		fi
		times=$((times+1))
		sleep 10
	done
	cnt=$((cnt+tmp))
	echo "Successfully computed #Coronaoutbreak of $prefix$format_start_date..."

	times=0
	while true
	do
		python Exporter.py --querysearch "COVID" --since $prefix$format_start_date --until $prefix$format_next_date
		tmp=`cat output_got.csv | wc -l`
		if [ $tmp -ge 1 ] || [ $times -gt 10 ]
		then
			break
		fi
		times=$((times+1))
		sleep 10
	done
	cnt=$((cnt+tmp))
	echo "Successfully computed #COVID of $prefix$format_start_date..."

	times=0
	while true
	do
		python Exporter.py --querysearch "Coronavirus" --since $prefix$format_start_date --until $prefix$format_next_date
		tmp=`cat output_got.csv | wc -l`
		if [ $tmp -ge 1 ] || [ $times -gt 10 ]
		then
			break
		fi
		times=$((times+1))
		sleep 10
	done
	cnt=$((cnt+tmp))
	echo "Successfully computed #Coronavirus of $prefix$format_start_date..."

	echo "$prefix$format_start_date,$cnt" >> out.date
	
	echo $start_date
	start_date=$next_date
	cnt=0
done

echo "Done"
