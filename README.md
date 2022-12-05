# NSE-stock-data-fetcher-query
Fetching the data from NSE and use Queries to get the results.
1. Programatically fetch “Securities available for Equity segment (.csv)” file From the URL: https://www.nseindia.com/market-data/securities-available-for-trading
2. Programatically get the latest “bhavcopy” csv file from the following URL - https://www.nseindia.com/all-reports
3. Construct a (relational) database with normalized tables & insert both the data files into it
4. In addition to step 2, programmatically get BHAvcopies of the last 30 days instead of just the latest one.
5. The BhavCopies and the database files uploaded in the repo are dated to 2nd Dec 2022 (To show example of how files are downloaded and how the database files are created).To get new files of the date the user running the script that will be downloaded in their current working directory where the user will run the given python scripts ... 
Thank you
Aman
