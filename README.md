# ADM-HW3
This repository contains the source code, notebooks, and additional materials related to Assignment 3 of the "Algorithms for Data Mining" course (23/24) from the Data Science Master's program at Sapienza University of Rome. Below, you will find an overview of the contents of this repository.



## Description
In this assignment, Data on available master's degree programs in different regions is being systematically extracted through a meticulous scraping process. The objective is to develop a search engine enabling students to identify the master's degree that aligns with their interests and academic ambitions.

The goal is to carry out the following tasks:

  - **Data Collection:** the data of the master's degrees were scrapped from the first 400 pages on the following [link](https://www.findamasters.com/masters-degrees/msc-degrees/).
  - **Search Engines:** Three distinct search engines have been constructed, each employing a unique approach. The initial engine processes the user's query by searching for the query words within the course description. The second engine, employing TF-IDF and cosine similarity, ranks retrieved data based on the similarity between the course description and the entered query. The third engine executes the query using a custom-defined scoring function.
  - **Complex Querying:** adding filtering capabilities to the search engine for more accurate results.
  - **Command Line Task:** Integrating the scrapped data and providing some statistics using command line prompts only.
  - **Algorithmic Task:** Implementation and Analysis of the time complexity of a certain algorithm. 

For a detailed understanding of the assignment requirements and problems, refer to this [link](https://github.com/Sapienza-University-Rome/ADM/tree/master/2023/Homework_3).



## Dataset
  The information utilized pertains to master's degree programs and has been extracted from the following [link](https://www.findamasters.com/masters-degrees/msc-degrees/). This dataset encompasses details such as course location, country, start date, tuition fees, online modality, availability of part-time and full-time options, along with a comprehensive course description and additional pertinent information.


## Repo content

- **engine.ipynb:** A comprehensive Jupyter notebook that presents a detailed analysis of the data. It includes a systematic breakdown of the analysis process, the resulting insights, and accompanying explanations to give a better understanding of the findings.
- **AQ.py:** The script employed for addressing the algorithmic task. it can also be found in the Jupyter Notebook.
- **crawler.py:** script for scrapping data from the website. it can also be found in the Jupyter Notebook.
- **parser.py:** script for parsing the scrapped data. it can also be found in the Jupyter Notebook.
- **commandline.sh:** A PowerShell script that answers the Command Line Question.


## Usage
- Clone the repo using the command **git clone https://github.com/onurozansunger/ADM-HW3-Group-26/tree/main** in a bash script terminal.
- Open the Jupyter Notebook using your desired IDE and start following the instructions there in order to replicate the results.

## Collaborators
- Hazem Aboulfotouh (aboulfotouh.2105193@studenti.uniroma1.it)
- Jose Angel Mola Audi (molaaudi.2116134@studenti.uniroma1.it)
- Onur Ozan Sunger (sunger.2113119@studenti.uniroma1.it)


