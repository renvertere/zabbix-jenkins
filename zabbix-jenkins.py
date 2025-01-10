#!/usr/bin/env python3

import requests
import json
import re

# Jenkins configuration
JENKINS_URL = "https://jenkins:8443"
API_USER = "zabbix.readonly@exmaple.com"
API_TOKEN = "APItokenhere!"

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Helper function to query Jenkins API
def query_jenkins_api(url):
    try:
        response = requests.get(
            url,
            auth=(API_USER, API_TOKEN),
            verify=False
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

# Function to generate a simplified job name from the URL
def generate_simplified_name(job_url):
    url_path = re.sub(r"https?://[^/]+", "", job_url)
    parts = [part for part in url_path.split("/") if part and part != "job"]
    simplified_name = "-".join(parts)
    return simplified_name

def collect_all_job_urls(url):
    job_list = []
    data = query_jenkins_api(f"{url}/api/json")

    if not data or "jobs" not in data:
        return job_list

    for item in data["jobs"]:
        job_class = item.get("_class", "")
        job_name = item.get("name", "")
        job_url = item.get("url", "")

        if "Folder" in job_class:
            job_list.extend(collect_all_job_urls(job_url))
        else:
            simplified_name = generate_simplified_name(job_url)
            job_info = {
                "job": job_name,
                "jobname": simplified_name,
                "joburl": job_url
            }
            job_list.append(job_info)

    return job_list

def main():
    results = collect_all_job_urls(JENKINS_URL)
    output = {"data": results}
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()