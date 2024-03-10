# CC4-Internship-2024-Div-Tech-Assessment
Assessment Title: Take-home Assignment for Data Engineer Intern
Technical assessment for the role 'Tech - Data Engineer : CareerCoach (CC4.0)'

# Overview

This project involves processing and analyzing restaurant data to aid a travel blogger, Steven, in creating a travel food series. It includes tasks such as extracting restaurant details, filtering restaurants by past events, and analyzing user ratings. The data is sourced from https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json and https://github.com/Papagoat/brain-assessment/blob/main/Country-Code.xlsx?raw=true.

1. 	Extract the following fields and store the data as restaurants.csv.
◦   	Restaurant Id
◦   	Restaurant Name
◦   	Country
◦   	City
◦   	User Rating Votes
◦   	User Aggregate Rating (in float)
◦   	Cuisines

2. 	Extract the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv.
◦   	Event Id
◦   	Restaurant Id
◦   	Restaurant Name
◦   	Photo URL
◦   	Event Title
◦   	Event Start Date
◦   	Event End Date
Note: Populate empty values with "NA".

3. 	From the dataset (restaurant_data.json), determine the threshold for the different rating text based on aggregate rating. Return aggregates for the following ratings only:
◦   	Excellent
◦   	Very Good
◦   	Good
◦   	Average
◦   	Poor

# Assumptions and Interpretations

During the development of this solution, several assumptions and interpretations were made regarding the data and the requirements. These guided the architecture decisions and the approach to data processing.

## Assumptions for Task 1: Restaurant Data Extraction
Restaurant ID Identification: It was assumed that the restaurant ID found within the path Restaurants >> restaurant >> R >> res_id is equivalent to Restaurants >> restaurant >> id. This assumption was based on the observation that both fields are present and seem to represent a unique identifier for each restaurant.

## Assumptions for Task 2: Restaurant Events Extraction
Event Date Interpretation: For the extraction of restaurants that have past events in April 2019, the assumption was made that "past events" refers to any event with an end_date falling within April 2019. This decision was taken to focus on events that concluded in April, regardless of their start date.

## Assumptions for Task 3: Rating Text Threshold Determination
Rating Text Thresholds: It was assumed that Zomato uses minimum and maximum aggregate ratings to determine the threshold for different rating texts (Excellent, Very Good, Good, Average, Poor). This interpretation guided the analysis to categorize restaurants based on their user aggregate ratings into these discrete rating groups.

# Notes on Architecture Decisions
Initial Working: Prelimary work on the tasks was done via Jupyter Notebook due to its interactive environment, which allows for easier experimentation with code, immediate feedback on outputs, and the ability to visualize data directly within the notebook.

Data Processing and Analysis: Pandas was chosen for data manipulation due to its efficiency and ease of use in handling CSV and JSON data formats. It allowed for straightforward data cleaning, transformation, and analysis operations.

Error Handling and Data Consistency: Error handling mechanisms were implemented to manage potential issues in data formats, missing values, and API response inconsistencies. This ensures the robustness of the data extraction and processing pipeline.

Modularity and Scalability: The python codebase was structured to ensure modularity, allowing for easy updates and scalability. Functions were designed to perform specific tasks, which can be reused or modified with minimal impact on the overall system.


# Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- pandas
- requests

# Installation
Step 1. Clone the repository to your local machine:
```bash
git clone https://github.com/neverdivideby0/CC4-Internship-2024-Div-Tech-Assessment.git
```
Step 2. Navigate to the project directory:
```bash
cd CC4-Internship-2024-Div-Tech-Assessment
```

Step 3. Install dependencies

Ensure you have Python installed on your system.
Then, install the required Python packages:
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```
If you are using conda
```bash
conda install pandas
conda install requests
conda install openpyxl
```

Step 4. Running the Code
Finally, run the script using Python
```bash
python CC4_Internship_2024_Div_Assessment.py
```
or
```bash
python3 CC4_Internship_2024_Div_Assessment.py
```

