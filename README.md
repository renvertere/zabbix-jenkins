<div id="top"></div>

<h1 align="center">Zabbix Jenkins Monitoring Solution</h1>

<br />
<div align="center">

[![YAML][yaml-shield]][yaml-url]
[![Python][python-shield]][python-url]
[![Github Actions][github-actions-shield]][github-actions-url]

![Release Pipeline][test-pipline-badge]

</div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/renaldo-maclons/zabbix-jenkins">
    <img src="resources/img/zabbix_logo.svg" alt="Logo" width="420" height="120">
    <br >
    <img src="resources/img/jenkins_logo.svg" alt="Logo" width="420" height="120">
  </a>

  <h3 align="center">Zabbix Jenkins Monitoring Solution</h3>

  <p align="center">
    This repository houses the required scripts and configuration to implement Zabbix monitoring for Jenkins jobs.
    <br />
    <a href="https://github.com/renaldo-maclons/zabbix-jenkins"><strong>Explore the documentation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/renaldo-maclons/zabbix-jenkins">View Demo</a>
    ·
    <a href="https://github.com/renaldo-maclons/zabbix-jenkins/issues">Report Bug</a>
    ·
    <a href="https://github.com/renaldo-maclons/zabbix-jenkins/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Disclaimer](#disclaimer)
- [Getting Started](#getting-started)
  - [Deployment Steps](#deployment-steps)
- [Usage](#usage)
  - [Monitoring Metrics in Zabbix](#monitoring-metrics-in-zabbix)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

<!-- ABOUT THE PROJECT -->
## About The Project

The Zabbix Jenkins Monitoring Solution enables the discovery and monitoring of Jenkins jobs using Zabbix. This solution integrates Low-Level Discovery (LLD) and a Python-based script to query the Jenkins API, allowing real-time monitoring of job statuses, durations, and results.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Zabbix](https://www.zabbix.com/)
* [Jenkins](https://www.jenkins.io/)
* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DISCLAIMER -->
## Disclaimer

This project is provided "as is" without any warranties or support. Compatibility has been tested with Zabbix 6.0 LTS and Jenkins `latest`, but functionality on other systems may vary. Use at your own risk.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To set up this monitoring solution, upload the Jenkins template to your Zabbix server, configure the Python script for querying the Jenkins API, and set up the required user parameters for Zabbix Agent.

### Deployment Steps

1. **Clone the repository**:
   ```bash
   git clone git@github.com:renaldo-maclons/zabbix-jenkins.git
   cd zabbix-jenkins
   ```

2. **Load the template**:
  - Import the file `resources/zabbix/template/template_app_jenkins.yaml` into your Zabbix server through the Configuration > Templates interface.

3. **Set Up User Parameters**:

  - Copy `resources/zabbix/userparameter/userparameter_jenkins.conf` to your Zabbix Agent configuration directory:

    ```bash
    sudo cp resources/zabbix/userparameter/userparameter_jenkins.conf /etc/zabbix/zabbix_agent2.d/plugins.d
    ```
4. **Restart Zabbix Agent**:

    ```bash
    systemctl restart zabbix-agent2
    ```

5. **Update Python Script**:
  - Edit the zabbix-jenkins.py script to configure the Jenkins API URL, user, and token:

    ```
    JENKINS_URL = "https://jenkins.example.com"
    API_USER = "zabbix.readonly@example.com"
    API_TOKEN = "your_api_token"
    ```
6. **Test the Integration**:
  - Verify that the Python script outputs LLD data by running:

    ```bash
    python3 zabbix-jenkins.py
    ```
  <p align="right">(<a href="#top">back to top</a>)</p>

  <!-- USAGE -->
## Usage

Once the template is applied, the Zabbix Jenkins Monitoring Solution will begin collecting data from the Jenkins API, providing valuable insights into job performance and statuses.

### Monitoring Metrics in Zabbix

- **Job Name**: The name of each Jenkins job.
- **Job URL**: Direct link to the Jenkins job in the Jenkins UI.
- **Job Duration**: The actual time taken for the last build of the job (in seconds).
- **Estimated Duration**: Average time the job is expected to take, based on historical builds (in seconds).
- **Job Result**: The result of the last build (e.g., SUCCESS, FAILURE).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Implement Low-Level Discovery (LLD) for Jenkins jobs.
- [x] Add support for querying job durations and statuses.
- [ ] Implement credential parsing via Zabbix Macros
- [ ] Enhance metrics collection to include build trends and queue times.
- [ ] Add alerting for failed or long-running jobs.
- [ ] Integrate visualization tools for Jenkins job performance.

See the open issues for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to propose changes or improvements. For major changes, open an issue to discuss them first.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Renaldo Maclons - [GitHub](https://github.com/renaldo-maclons)

Project Link: [Zabbix Jenkins Monitoring](https://github.com/renaldo-maclons/zabbix-jenkins)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Zabbix](https://www.zabbix.com/)
- [Jenkins](https://www.jenkins.io/)
- [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[yaml-shield]: https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515
[yaml-url]: https://github.com/renaldo-maclons/zabbix-jenkins
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://github.com/renaldo-maclons/zabbix-jenkins
[github-actions-shield]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white
[github-actions-url]: https://github.com/renaldo-maclons/zabbix-jenkins/actions
[test-pipline-badge]: https://github.com/renaldo-maclons/zabbix-jenkins/actions/workflows/release-ci.yml/badge.svg
