# DM_Midterm
Association rule mining project implementation
By following these steps, you should be able to run the Association Rule Mining project successfully, even if you don't have prior programming knowledge.
This project implements three different algorithms (Apriori, FP-Growth, and Brute Force) to find association rules from a given dataset of transactions. The main script to run is combined_script.py. Follow the steps below to execute the project successfully. 
Prerequisites
Before running the project, ensure you have the following prerequisites installed: 
1.	Python 3.x: You need to have Python 3.x installed on your system. You can download it from the official Python website: https://www.python.org/downloads/ 
2.	Required Python Libraries: The project requires the following Python libraries: 
o	pandas
o	mlxtend
You can install these libraries using pip, the Python package installer. Open your terminal or command prompt and run the following commands: 
pip install pandas
pip install mlxtend
Running the Project
1.	Download the Project Files: Download all the provided Python files (apriori_algorithm.py, fp_growth_algorithm.py, brute_force_algorithm.py, file_input.py, select_database.py, and combined_script.py) and the dataset files (for example: Amazon.csv) to a directory on your local machine. Or you can just extract the zip file provided.
2.	Navigate to the Project Directory: Open your terminal or command prompt and navigate to the directory where you downloaded the project files using the cd command. 
3.	Run the Main Script: In the terminal or command prompt, run the following command: 
python comnined_script.py
4.	Select the Database: The script will prompt you to select a database. Enter the number as shown in the prompt of the dataset file.
5.	Enter Support and Confidence Thresholds: After selecting the database, the script will prompt you to enter the minimum support and confidence thresholds as percentages. These values will be used by the algorithms to find association rules. 
6.	View the Results: The script will execute the three algorithms (Apriori, FP-Growth, and Brute Force) and display the association rules found, along with their confidence and support values. It will also print the execution time taken by each algorithm.
