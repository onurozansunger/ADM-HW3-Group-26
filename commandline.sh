#!/bin/bash

# Define the directory containing the TSV files
DIR="/Users/onurozansunger/Desktop/ADM-HW3-Group-26/HW3/courses_tsv"

# Navigate to the directory
cd $DIR

# Initialize the merged file (it will be empty initially)
> merged_courses.tsv

# Append the first line (header) of each file
for i in {0..5999}
do
    FILE="course_$i.tsv"
    if [ -f "$FILE" ]; then
        head -n 1 "$FILE" >> merged_courses.tsv
    fi
done

# Adjusted Column numbers based on the provided file structure
degree_type_col=8
education_mode_col=4
city_col=10
country_col=11
course_name_col=1

# Find the country with the most Master's Degrees
most_masters_country=$(awk -F'\t' -v col="$degree_type_col" -v country="$country_col" \
    '$col=="MSc" {print $country}' merged_courses.tsv | sort | uniq -c | sort -nr | head -n 1)

# Find the city with the most Master's Degrees
most_masters_city=$(awk -F'\t' -v col="$degree_type_col" -v city="$city_col" \
    '$col=="MSc" {print $city}' merged_courses.tsv | sort | uniq -c | sort -nr | head -n 1)

# Count how many colleges offer Part-Time education
part_time_colleges=$(awk -F'\t' -v mode="$education_mode_col" \
    '$mode ~ /Part Time/' merged_courses.tsv | cut -f 2 | sort | uniq | wc -l)

# Calculate the percentage of Engineering courses
total_courses=$(wc -l < merged_courses.tsv)
engineering_courses=$(awk -F'\t' -v name="$course_name_col" \
    '$name ~ /Engineering|Engineer/' merged_courses.tsv | wc -l)
engineering_percentage=$((engineering_courses * 100 / total_courses))

# Output the results
echo "Country with the most Master's Degrees: $most_masters_country"
echo "City with the most Master's Degrees: $most_masters_city"
echo "Number of colleges offering Part-Time education: $part_time_colleges"
echo "Percentage of Engineering courses: $engineering_percentage%"

