# Contributing to House of Scraper

🎉 **Welcome!** We're thrilled that you're considering contributing to **House of Scraper**, a modular and lightweight web scraping toolkit designed to extract structured data from real estate websites using Python, BeautifulSoup, CloudScraper, and Requests. Your contributions help make this project better for everyone.​[GitHub](https://github.com/topics/cloudscraper?utm_source=chatgpt.com)

## 📌 Table of Contents

1.  [Forking and Cloning the Repository](#1-forking-and-cloning-the-repository)
2.  [Creating a New Branch](#2-creating-a-new-branch)
3.  [Submitting a Pull Request](#3-submitting-a-pull-request)
4.  [Coding Style Guidelines](#4-coding-style-guidelines)
5.  [Running the Project Locally](#5-running-the-project-locally)
6.  [Finding Issues to Work On](#6-finding-issues-to-work-on)
7.  [Communication and Code of Conduct](#7-communication-and-code-of-conduct)
* * *

## 1\. Forking and Cloning the Repository

To contribute, start by forking the repository and cloning it to your local machine:

```bash
# Fork the repository on GitHub, then clone it
git clone https://github.com/your-username/house_of_scraper.git
cd house_of_scraper`
```
Replace `your-username` with your actual GitHub username.

* * *

## 2\. Creating a New Branch

Before making any changes, create a new branch to work on:

```bash
git checkout -b feature/your-feature-name
```
Use a descriptive name for your branch that reflects the feature or fix you're working on.

* * *

## 3\. Submitting a Pull Request

Once you've made your changes:

1.  Commit your changes with a clear message:

    ```bash
    git add .
    git commit -m "Add feature: your feature description"
    ```
    
2.  Push your branch to your forked repository:
    ```bash
    git push origin feature/your-feature-name`
    ```
    
3.  Open a pull request from your branch to the `main` branch of the original repository.

Please ensure your pull request includes a clear description of the changes and references any relevant issues.

* * *

## 4\. Coding Style Guidelines

While there are no strict coding style guidelines specified, please adhere to the following best practices:

-   **Consistency**: Follow the existing code style in the project.
-   **PEP 8**: Aim to comply with [PEP 8](https://pep8.org/) Python style guide.
-   **Documentation**: Comment your code where necessary to explain complex logic.
-   **Testing**: If applicable, include tests for your changes.
* * *

## 5\. Running the Project Locally

To run the project locally:

1.  Ensure you have Python installed on your machine.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt`
    ```
3.  Run the scraper module with the specified target:
    ```bash
    python -m scraper --module "Folder.sub_folder"`
    ```
    Replace `"Folder.sub_folder"` with the actual module path for your scraping logic.

4.  Check the results in the `/result` directory. This directory is automatically created by the tool if it does not already exist.
* * *

## 6\. Finding Issues to Work On

Looking for something to work on? Check out the [Issues](https://github.com/haydarmiezanie/house_of_scraper/issues) section of the repository. Feel free to comment on an issue to express your interest in working on it.

* * *

## 7\. Communication and Code of Conduct

We are committed to fostering a welcoming and inclusive environment for all contributors. Please adhere to the following guidelines:

-   Be respectful and considerate in all interactions.
-   Provide constructive feedback.
-   Report any unacceptable behavior to the repository maintainers.

By participating in this project, you agree to abide by these guidelines to ensure a positive experience for everyone involved.

* * *

Thank you for your interest in contributing to **House of Scraper**! Your efforts are greatly appreciated. If you have any questions or need assistance, feel free to open an issue or reach out to the maintainers.

Happy coding! 🚀
