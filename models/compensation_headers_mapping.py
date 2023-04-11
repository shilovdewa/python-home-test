class CompansationHeadersMapping:
    def __init__(self):
        self.mapping = [ {'map': 'ts', 'orig': 'Timestamp', 'type': "timestamp"},
                    {'map': 'employment_type', 'orig': 'Employment Type', 'type': "string"},
                    {'map': 'company_name', 'orig': 'Company Name', 'type': "string"},
                    {'map': 'company_size', 'orig': 'Company Size - # Employees', 'type': "string"},
                    {'map': 'primary_location_country', 'orig': 'Primary Location (Country)', 'type': "string"},
                    {'map': 'primary_location_city', 'orig': 'Primary Location (City)', 'type': "string"},
                    {'map': 'industry', 'orig': 'Industry in Company', 'type': "string"},
                    {'map': 'company_type', 'orig': 'Public or Private Company', 'type': "string"},
                    {'map': 'experience_industry', 'orig': 'Years Experience in Industry', 'type': "string"},
                    {'map': 'experience_company', 'orig': 'Years of Experience in Current Company', 'type': "string"},
                    {'map': 'company_job_title', 'orig': 'Job Title In Company', 'type': "string"},
                    {'map': 'job_level', 'orig': 'Job Level', 'type': "string"},
                    {'map': 'required_hours', 'orig': 'Required Hours Per Week', 'type': "string"},
                    {'map': 'actual_hours', 'orig': 'Actual Hours Per Week', 'type': "string"},
                    {'map': 'education', 'orig': 'Highest Level of Formal Education Completed', 'type': "string"},
                    {'map': 'salary', 'orig': 'Total Base Salary in 2018 (in USD)', 'type': "float64"},
                    {'map': 'bonus', 'orig': 'Total Bonus in 2018 (cumulative annual value in USD)', 'type': "float64"},
                    {'map': 'stock', 'orig': 'Total Stock Options/Equity in 2018 (cumulative annual value in USD)', 'type': "float64"},
                    {'map': 'insurance', 'orig': 'Health Insurance Offered', 'type': "string"},
                    {'map': 'vacation', 'orig': 'Annual Vacation (in Weeks)', 'type': "string"},
                    {'map': 'happy', 'orig': 'Are you happy at your current position?', 'type': "string"},
                    {'map': 'resign', 'orig': 'Do you plan to resign in the next 12 months?', 'type': "string"},
                    {'map': 'direction_thoughts', 'orig': 'What are your thoughts about the direction of your industry?', 'type': "string"},
                    {'map': 'gender', 'orig': 'Gender', 'type': "string"},
                    {'map': 'top_skills', 'orig': 'Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?', 'type': "string"},
                    {'map': 'bootcamp', 'orig': 'Have you ever done a bootcamp? If so was it worth it?', 'type': "string"}]

    def getMapping(self):
        mapping = {}
        for map in self.mapping:
            mapping.update({ map['orig'] : map['map'] })
        return mapping

    def getType(self, key: str) -> str:
        for map in self.mapping:
            if map['map'].lower() == key.lower():
                return map['type']