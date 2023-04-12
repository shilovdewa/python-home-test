class CompansationHeadersMapping:
    mapping = {
                'ts' : {'orig': 'Timestamp', 'type': "timestamp" },
                'employment_type' : {'orig': 'Employment Type', 'type': "string" },
                'company_name' : {'orig': 'Company Name', 'type': "string" },
                'company_size' : {'orig': 'Company Size - # Employees', 'type': "string" },
                'primary_location_country' : {'orig': 'Primary Location (Country)', 'type': "string" },
                'primary_location_city' : {'orig': 'Primary Location (City)', 'type': "string" },
                'industry' : {'orig': 'Industry in Company', 'type': "string" },
                'company_type' : {'orig': 'Public or Private Company', 'type': "string" },
                'experience_industry' : {'orig': 'Years Experience in Industry', 'type': "string" },
                'experience_company' : {'orig': 'Years of Experience in Current Company', 'type': "string" },
                'company_job_title' : {'orig': 'Job Title In Company', 'type': "string" },
                'job_level' : {'orig': 'Job Level', 'type': "string" },
                'required_hours' : {'orig': 'Required Hours Per Week', 'type': "string" },
                'actual_hours' : {'orig': 'Actual Hours Per Week', 'type': "string" },
                'education' : {'orig': 'Highest Level of Formal Education Completed', 'type': "string" },
                'salary' : {'orig': 'Total Base Salary in 2018 (in USD)', 'type': "float64" },
                'bonus' : {'orig': 'Total Bonus in 2018 (cumulative annual value in USD)', 'type': "float64" },
                'stock' : {'orig': 'Total Stock Options/Equity in 2018 (cumulative annual value in USD)', 'type': "float64" },
                'insurance' : {'orig': 'Health Insurance Offered', 'type': "string" },
                'vacation' : {'orig': 'Annual Vacation (in Weeks)', 'type': "string" },
                'happy' : {'orig': 'Are you happy at your current position?', 'type': "string" },
                'resign' : {'orig': 'Do you plan to resign in the next 12 months?', 'type': "string" },
                'direction_thoughts' : {'orig': 'What are your thoughts about the direction of your industry?', 'type': "string" },
                'gender' : {'orig': 'Gender', 'type': "string" },
                'top_skills' : {'orig': 'Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?', 'type': "string" },
                'bootcamp' : {'orig': 'Have you ever done a bootcamp? If so was it worth it?', 'type': "string" }
            }

    def getMapping(self):
        mapping = {}
        for map in self.mapping.keys():
            mapping.update({ self.mapping[map]['orig'] : map })
        return mapping

    def getType(self, key: str) -> str:
        return self.mapping[key.lower()]['type']