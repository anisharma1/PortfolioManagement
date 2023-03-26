# PORTFOLIO MANAGEMENT PROJECT
## (ASCEND EduCare Group 3)
* ### ABOUT<br>
   * The portfolio management application is a comprehensive platform that facilitates investment tracking <br> and performance monitoring for users. The application offers a user-friendly interface, which displays<br> the user's holdings, transactions, and performance metrics.
   * It is built on django framework and uses sql database.
   * The portfolio management project has been extended to develop an analysis tool to enable the user to effectively monitor his/her investments and make informed futher investment decisions.
   * The analysis tool has been developed using Google Colab and ipywidgets library.
 <hr>
 
 
* ### TABLE OF CONTENTS
   * [GETTING STARTED WITH THE WEB APP](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#getting-started-with-the-web-app)
   * [GETTING STARTED WITH THE ANALYSIS TOOL](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#getting-started-with-the-analysis-tool)
   * [OVERVIEW OF THE WEB APP](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#overview-of-the-web-app)
   * [OVERVIEW OF THE ANALYSIS TOOL](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#overview-of-the-analysis-tool)
   * [FUTURE SCOPE](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#future-scope)
   * [OUR GROUP](https://github.com/Snehil0603/PortfolioManagement/blob/main/README.md#our-group)
 <hr>  
   
   
* ### GETTING STARTED WITH THE WEB APP
  * #### INSTALLATION
    * We need Python, Django and mysqlclient installed to run this project.
      * Python : <a href="https://www.python.org/downloads/">Python Installation</a>
      * Django : `pip install django`
      * MySQLClient : <a href="http://dev.mysql.com/downloads/shell/">MySQLClient Installation</a>
   * <b>After installing the dependencies -:</b>
      * Clone the repository :
        * `git clone https://github.com/<username>/<forked-repo>.git`
       * Create your own virtual environment : 
         * `python3 -m venv venv`
         * 'source venv/bin/activate'
       * Install your requirements :
         * `pip install -r requirements.txt`
       * open cmd and run the commands to create the database :
         * `mysql -u root -p`
         * `CREATE DATABASE portfoliomanagement;`
         * `USE portfoliomanagement;`
       * To get database files in your PC run this command for all .sql files in database folder :
          * `mysql > source file_path_with_file_name.sql;`
       * Open setting.py file in PortfolioManager folder and change database section to this : 
       <img src="https://user-images.githubusercontent.com/96441611/227181216-391d9495-4f78-4682-9a22-687cf4cf38c1.png"></img>
       * Make your migrations : 
          * python manage.py makemigrations
          * python manage.py migrate
        * Run project on localhost : 
          * python manage.py runserver<br>
<hr>

 * ### GETTING STARTED WITH THE GOOGLE COLAB ANALYSIS TOOL
    * We need to upload analysis csv files into Google Colab to run the notebook.
      * Go to the "Analysis Tool Files" folder
      * Download all the files present in the folder
      * Upload these files into the Google Colab
    * Run the notebook shells one by one
    * The last shell contains the dashboard
 <hr>
 
 * ### OVERVIEW OF THE WEB APP
    * #### HOME PAGE
      <img src="https://user-images.githubusercontent.com/111197294/227778229-afc293f3-4b05-4c80-a6f8-95c64939ec82.png"></img>
    * ### REGISTERATION PAGE
      <img src="https://user-images.githubusercontent.com/111197294/227714950-55ed6f37-df06-4924-b74d-3f066fbe4e61.png" width="1000"></img>
    * #### LOGIN PAGE
      <img src="https://user-images.githubusercontent.com/111197294/227778252-2826f271-9659-48fb-a21f-9f472a7b44ec.png" width="1000"></img>
    * #### LOGOUT PAGE
      <img src="https://user-images.githubusercontent.com/111197294/227778338-8794ecdb-777b-4e76-b75f-8329044e53c6.png" width="1000"></img>
    * #### DASHBOARD
      <img src="https://user-images.githubusercontent.com/111197294/227730536-31f9e9c4-61d8-4731-8ae5-8377e60f3415.png" width="1000"></img>
    * #### ALL_STOCKS_PROFILES
       <img src="https://user-images.githubusercontent.com/111197294/227730227-b7166488-d25b-4211-9cf3-6afac9030d64.png" width="1000"></img>
    * #### MY STOCKS PAGE (to add stocks to the portfolio)
      <img src="https://user-images.githubusercontent.com/96441611/227191119-9d318de5-b9f3-4073-8466-f0c355740034.png" width="400"></img>
    * #### LOGOUT
    <img src="https://user-images.githubusercontent.com/111197294/227778707-995a25cd-be2a-4bf5-b4cb-d686b482ad8c.png" width="400"></img>
<hr>

 * ### OVERVIEW OF THE ANALYSIS TOOL
    * #### STOCK PRICE TRENDS
       <img src="https://user-images.githubusercontent.com/111197294/227778432-92be6458-2d40-47a3-a0e7-364c89dddaa0.png" width="1000"></img>        
    * #### DATASET EXPLORATION
       <img src="https://user-images.githubusercontent.com/111197294/227778488-3c537d67-d79c-4c1d-b03f-30f69613a4ce.png" width="1000"></img>
    * #### STOCK ANALYSIS TAB
       <img src="https://user-images.githubusercontent.com/111197294/227778570-483805b2-c907-4474-be33-bc893b326e25.png" width="1000"></img>
    * #### COMPARISON ANALYSIS TAB
       <img src="https://user-images.githubusercontent.com/111197294/227778635-728796e2-d404-45dd-b12d-ead294d541de.png" width="1000"></img>
<hr>
 
 * ### FUTURE SCOPE
    * The future endeavors associated with the application include integrating analysis of specific stocks with<br> our web app and expanding the range of investment types supported, integrating advanced analytics and reporting, and<br> collaborating with third-party investment tools.
<hr>

 * ### OUR GROUP
   * #### ISHANK JAIN (MENTOR)
   * #### RISHIKA 
   * #### NIHARIKA
   * #### SNEHIL
   * #### ANISHA SHARMA
   * #### KOMAL
