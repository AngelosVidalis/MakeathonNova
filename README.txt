#Challenge:
	Develop an innovative tool to streamline the process of knowledge management in archival publicity
	material, focusing on the last years' historicity. The tool should leverage advanced algorithms and
	natural language processing (NLP) techniques to automatically categorize, tag, and retrieve relevant
	information based on keywords and meta-description.

	Proposed Keyworks: Nova, BC Partners etc.

#Objectives
	
	Participants are tasked with creating a knowledge management tool. The tool should have thefollowing functionalities:
	• Automated Information Retrieval: Utilize algorithms to extract and organize data from archival publicity material such as press releases, interviews, and articles.
	• Keyword Matching: Develop a system that utilizes keyword and matching to enhance the accuracy and efficiency of information retrieval.
	• Historical Data Access: Enable users to access and retrieve historical data from the past X years with ease and precision.
	• Output Customization: Provide options for users to customize the output format of retrieved information, such as PDF reports or structured data files.

#Data Sources:
	(ideally, every newsletter given => done with API, code doesn't include this option)
	1. https://www.skai.gr/  


#Details:
	1. Took data only from https://www.skai.gr/ with **scraping method**
	2. User picks the category, the number of pages he wants to check or with a bit of change in the code files all the articles till the given year (wanted_year [wy] (<=)). 
	   Example: if wy = 2023, the it takes all data from 2024 and 2023. When one date is found that doesn't match our wy then function stops.
	3. Every category available in https://www.skai.gr/