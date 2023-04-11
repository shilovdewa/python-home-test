# python-home-test

Requirements: Python 3, Flask (https://flask.palletsprojects.com/en/2.2.x/installation/)

## Run

flask --app main run

## Environments

DATA_PATH=./dataset/salary_survey.csv

## Query parameters

Query string example: /compensation_data?salary[gte]=120000&primary_location=Portland&sort=salary&fields=first_name,last_name,salary

## Possible Filtering operations
gt, lt, gte, lte - works only for the float64 fields \
timestamp fields should use YYYY-MM-DDThh:mm:ss format

## List of fields

|CSV Name|API name|Type|
|---|---|---|
|Timestamp|ts|datetime|
|Employment Type|employment_type|string|
|Company Name|company_name|string|
|Company Size - # Employees|company_size|string|
|Primary Location (Country)|primary_location_country|string|
|Primary Location (City)|primary_location_city|string|
|Industry in Company|industry|string|
|Public or Private Company|company_type|string|
|Years Experience in Industry|experience_industry|string|
|Years of Experience in Current Company|experience_company|string|
|Job Title In Company|company_job_title|string|
|Job Ladder|job_ladder|string|
|Job Level|job_level|string|
|Required Hours Per Week|required_hours|string|
|Actual Hours Per Week|actual_hours|string|
|Highest Level of Formal Education Completed|education|string|
|Total Base Salary in 2018 (in USD)|salary|float64|
|Total Bonus in 2018 (cumulative annual value in USD)|bonus|float64|
|Total Stock Options/Equity in 2018 (cumulative annual value in USD)|stock|float64|
|Health Insurance Offered|insurance|string|
|Annual Vacation (in Weeks)|vacation|string|
|Are you happy at your current position?|happy|string|
|Do you plan to resign in the next 12 months?|resign|string|
|What are your thoughts about the direction of your industry?|direction_thoughts|string|
|Gender|gender|string|
|Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?|top_skills|string|
|Have you ever done a bootcamp? If so was it worth it?|bootcamp|string|
